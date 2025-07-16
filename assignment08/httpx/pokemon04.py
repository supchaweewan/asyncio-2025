import asyncio
import httpx

async def fetch(name):
    async with httpx.AsyncClient() as client:
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        response = await client.get(url)
        data = response.json()
        return name, data['id'], [t['type']['name'] for t in data['types']]

async def main():
    pokemon_names = ["pikachu", "bulbasaur", "charmander", "squirtle", "eevee", "snorlax", "gengar", "mewtwo", "psyduck", "jigglypuff"]


    get_pokemon = [fetch(name) for name in pokemon_names]
    results = await asyncio.gather(*get_pokemon)
    for name, id, types in results:
        print(f"{name} -> ID: {id}, Type(s): {types}")


asyncio.run(main())

    