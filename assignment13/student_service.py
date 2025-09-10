from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse
from pydantic import BaseModel
import httpx, os, asyncio
from dotenv import load_dotenv
import folium
from typing import Optional

# โหลด config จาก .env
load_dotenv()
app = FastAPI()

CITY = os.getenv("CITY", "Bangkok,TH")
LAT = float(os.getenv("LAT", 13.7563))
LON = float(os.getenv("LON", 100.5018))
OWM_API_KEY = os.getenv("OWM_API_KEY", "")
SERVICE_REGISTRY_URL = os.getenv("SERVICE_REGISTRY_URL", "http://localhost:9000")
STUDENT_NAME = os.getenv("STUDENT_NAME", "65123456789")
SELF_URL = os.getenv("SELF_URL", "http://localhost:8001/weather")

# ----------- Pydantic Models -----------
class WeatherResponse(BaseModel):
    student: str
    city: str
    temperature: float
    lat: float
    lon: float

class ErrorResponse(BaseModel):
    error: str


# ----------- Startup Register -----------
@app.on_event("startup")
async def register_service():
    async with httpx.AsyncClient() as client:
        try:
            await client.post(f"{SERVICE_REGISTRY_URL}/register", json={
                "name": STUDENT_NAME,
                "url": SELF_URL
            })
            print(f"[REGISTERED] {STUDENT_NAME} -> {SERVICE_REGISTRY_URL}")
        except Exception as e:
            print(f"[ERROR] Failed to register: {e}")


# ----------- /weather Endpoint -----------
@app.get("/weather", response_model=WeatherResponse, responses={500: {"model": ErrorResponse}})
async def get_weather():
    async with httpx.AsyncClient() as client:
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={OWM_API_KEY}&units=metric"
            r = await client.get(url)
            data = r.json()
            temp = data.get("main", {}).get("temp", None)
            if temp is None:
                return JSONResponse(status_code=500, content={"error": "Invalid response from OpenWeatherMap"})

            return WeatherResponse(
                student=STUDENT_NAME,
                city=CITY,
                temperature=temp,
                lat=LAT,
                lon=LON
            )

        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})


# ----------- /aggregate Endpoint -----------
@app.get("/aggregate")
async def aggregate_weather():
    async with httpx.AsyncClient() as client:
        try:
            r = await client.get(f"{SERVICE_REGISTRY_URL}/services")
            service_list = r.json()

            tasks = [fetch_weather(client, url) for url in service_list.values()]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            weather_data = [d for d in results if isinstance(d, dict)]

            if not weather_data:
                return {"message": "No data available"}

            avg_lat = sum([float(d["lat"]) for d in weather_data]) / len(weather_data)
            avg_lon = sum([float(d["lon"]) for d in weather_data]) / len(weather_data)

            m = folium.Map(location=[avg_lat, avg_lon], zoom_start=6)
            for data in weather_data:
                folium.Marker(
                    location=[data["lat"], data["lon"]],
                    popup=f"{data['student']} - {data['temperature']}°C",
                    tooltip=data["student"]
                ).add_to(m)

            m.save("map.html")
            return JSONResponse(content={
                "message": "Map generated",
                "file": "map.html",
                "data": weather_data
            })

        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})


# ----------- Fetch weather from peer -----------
async def fetch_weather(client: httpx.AsyncClient, url: str) -> Optional[dict]:
    try:
        r = await client.get(url, timeout=5)
        return r.json()
    except Exception:
        return None


# ----------- /map View -----------
@app.get("/map", response_class=HTMLResponse)
async def view_map():
    if os.path.exists("map.html"):
        with open("map.html", "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Map not found</h1>"