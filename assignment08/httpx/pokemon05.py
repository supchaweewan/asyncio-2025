import asyncio
import httpx

async def fetch(name):
    async with httpx.AsyncClient() as client:
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        response = await client.get(url)
        data = response.json()
        return name, data['id'], data['base_experience']

    



async def main():
    pokemon_names = ["pikachu", "bulbasaur", "charmander", "squirtle", "eevee", "snorlax", "gengar", "mewtwo", "psyduck", "jigglypuff"]


    get_pokemon = [fetch(name) for name in pokemon_names]
    results = await asyncio.gather(*get_pokemon)
    sorted_results = sorted(results, key=lambda results: results[2], reverse= True)
    
    for name, id, base_xp in sorted_results:
        print(f"{name:<10} -> ID:{id:<4}, Base XP: {base_xp}")


asyncio.run(main())