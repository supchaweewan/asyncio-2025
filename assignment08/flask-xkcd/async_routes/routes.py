import time
import random
import requests as requests
import asyncio
import httpx
from flask import Blueprint, render_template, current_app

# Create a Blueprint for async routes
async_bp = Blueprint("async", __name__)

# Helper function to fetch a single XKCD JSON by URL
async def get_xkcd(url):
    async with httpx.AsyncClient() as client:
        
        response = await client.get(url)
        print(f"{time.ctime()} - get {url}")
        return response.json()

    """    response = requests.get(url)
    print(f"{time.ctime()} - get {url}")    # Log the request time and URL
    return response.json()
    """

# Helper function to fetch multiple XKCD comics
async def get_xkcds():
    # Get the number of comics to fetch from app config
    NUMBER_OF_XKCD = current_app.config["NUMBER_OF_XKCD"]

    # Generate a list of random comic numbers (0–300)
    rand_list=[]
    for i in range(NUMBER_OF_XKCD):
        rand_list.append(random.randint(0,300))

    xkcd_data = []

    for numbers in rand_list:
        url = f"https://xkcd.com/{numbers}/info.0.json"
        xkcd_json = get_xkcd(url)
        xkcd_data.append(xkcd_json)

    xkcd_data = await asyncio.gather(*xkcd_data)
    return xkcd_data

    """
    for number in rand_list:
        url = f'https://xkcd.com/{number}/info.0.json'
        xkcd_json = get_xkcd(url)   # Fetch comic JSON
        xkcd_data.append(xkcd_json)
    return xkcd_data
    """

# Route: GET /sync/
@async_bp.route('/')
def home():
    start_time = time.perf_counter()  # Start performance timer
    xkcds = asyncio.run(get_xkcds())               # Fetch random XKCD comics
    end_time = time.perf_counter()    # End performance timer
    

    # Log time and count
    print(f"{time.ctime()} - Got {len(xkcds)} xkcd. Time taken: {end_time-start_time} seconds")

    # Render result using Jinja2 template
    return render_template('async.html'
                           , title="XKCD Asynchronous Flask"
                           , heading="XKCD Asynchronous Version"
                           , xkcds=xkcds
                           , end_time=end_time
                           , start_time=start_time)
