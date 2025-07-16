import asyncio
import httpx

async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://pokeapi.co/api/v2/pokemon/pikachu")
        data = response.json()
        print("Name: ", data["name"])
        print("ID: ", data["id"])
        print("Height: ", data["height"])
        print("Weight: ", data["weight"])
        print("Types: ", [t["type"]["name"] for t in data["types"]])

asyncio.run(main())