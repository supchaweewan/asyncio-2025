# Create 2 Tasks with High-Level API
import asyncio

async def get_image(name, delay):
    print(f"{name} is being downloaded")
    await asyncio.sleep(delay)
    print(f"{name} finished downloading")

async def main():
    task1 = asyncio.create_task(get_image("photo 1", 2))
    task2 = asyncio.create_task(get_image("photo 2", 3))

    await task1
    await task2

asyncio.run(main())