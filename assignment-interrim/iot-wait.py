import asyncio, time, random

async def get_temperature():
    await asyncio.sleep(random.uniform(0.5, 2.0))
    return " Temp: 30 degrees Celsius"

async def get_humidity():
    await asyncio.sleep(random.uniform(0.5, 2.0))
    return " Humidity: 60%"

async def get_weather_api():
    await asyncio.sleep(random.uniform(0.5, 2.0))
    return " Weather: Sunny"


async def main():
    start = time.time()
    temp_task = asyncio.create_task(get_temperature())
    humid_task = asyncio.create_task(get_humidity())
    weather_task =asyncio.create_task(get_weather_api())

    done, pending = await asyncio.wait([temp_task, humid_task, weather_task], return_when=asyncio.ALL_COMPLETED)
    for t in done:
        print(f"{time.ctime()} --> ", t.result())
    print(f"Took {time.time() - start} seconds")



asyncio.run(main())