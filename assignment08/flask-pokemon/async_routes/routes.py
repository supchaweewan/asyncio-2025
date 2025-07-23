import time
import random
import requests as requests
import asyncio
import httpx
from flask import Blueprint, render_template, current_app

# Create a Blueprint for sync routes
async_bp = Blueprint("async", __name__)

async def get_pokemon(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        print(f"{time.ctime()} - get {url}")
        pokemon = response.json()
        return pokemon

# Helper function to fetch a single POKEMON JSON by URL
async def get_pokemons():
    rand_list=[]
    # Get the number of comics to fetch from app config
    NUMBER_OF_POKEMON = current_app.config["NUMBER_OF_POKEMON"]
    for i in range(NUMBER_OF_POKEMON):
        rand_list.append(random.randint(1,300))
    pokemon_data = []
    for number in rand_list:
        url = f'https://pokeapi.co/api/v2/pokemon/{number}'
        pokemon_json = get_pokemon(url)
        pokemon_data.append(pokemon_json)
    pokemon_data = await asyncio.gather(*pokemon_data)
    return pokemon_data

# Route: GET /sync/
@async_bp.route('/')
def home():
    start_time = time.perf_counter()  # Start performance timer
    pokemons = asyncio.run(get_pokemons())               # Fetch random XKCD comics
    end_time = time.perf_counter()    # End performance timer

    # Log time and count
    print(f"{time.ctime()} - Get {len(pokemons)} xkcd. Time taken: {end_time-start_time} seconds")

    # Render result using Jinja2 template
    return render_template('sync.html'
                           , title="Pokemon Synchronous App"
                           , heading="Pokemon Synchronous Version"
                           , pokemons=pokemons
                           , end_time=end_time
                           , start_time=start_time)
