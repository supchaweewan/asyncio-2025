import asyncio
import httpx
import json

SERVERS = [
    "https://172.20.49.87:8000",
    "https://172.20.49.15:8000",
    "https://172.20.50.30:8000"
]

async def fetch_students(client, server):
    try:
        resp = await client.get(f"{server}/students", timeout=5.0)
        resp.raise_for_status()
        data = resp.json
        return {"server": server, "student_count": len(data)}
    except Exception as e:
        return {"server": server, "error": str(e)}

async def fetch_group(client, server):
    try:
        resp = await client.get(f"{server}/analytics/group", timeout=5.0)
        resp.raise_for_status()
        data = resp.json
        return {"server": server, "student_count": len(data)}
    except Exception as e:
        return {"server": server, "error": str(e)}

async def fetch_year(client, server):
    try:
        resp = await client.get(f"{server}/analytics/year", timeout=5.0)
        resp.raise_for_status()
        data = resp.json
        return {"server": server, "student_count": len(data)}
    except Exception as e:
        return {"server": server, "error": str(e)}

async def main():
    async with httpx.AsyncClient() as client:
        tasks = []
        for server in SERVERS:
            tasks.append(fetch_students(client, server))
            tasks.append(fetch_group(client, server))
            tasks.append(fetch_year(client, server))

        results = await asyncio.gather(*tasks)

        for result in results:
            print(json.dumps(result, indent=2, ensure_ascii=False))
if __name__ == "__main__":
    asyncio.run(main())