from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# เก็บ service ที่ลงทะเบียนไว้
registry: Dict[str, str] = {}

class RegisterRequest(BaseModel):
    name: str
    url: str

@app.post("/register")
async def register_service(req: RegisterRequest):
    registry[req.name] = req.url
    return {"message": f"{req.name} registered."}

@app.get("/services")
async def list_services():
    return registry