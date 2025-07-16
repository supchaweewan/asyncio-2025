import asyncio
import httpx

ability_url = "https://pokeapi.co/api/v2/ability/?limit=20"

async def fetch_details(url, client):
    response = await client.get(url)
    data = response.json()
    ability_name = data["name"]
    pokemon_amnt = len(data["pokemon"])
    return ability_name, pokemon_amnt


async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get(ability_url)
        abilities_data = response.json()["results"]
        first_10 = abilities_data[:10]
        tasks = [
            fetch_details(ability["url"], client)
            for ability in first_10
        ]
        results = await asyncio.gather(*tasks)
        print(f'{"Ability: ":<15} {"Number of Pokemons"}')
        for ability_name, count in results:
            print(f"{ability_name:<15} {count}")


asyncio.run(main())