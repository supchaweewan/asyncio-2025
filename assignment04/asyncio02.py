# Create 1 Task with High-Level API
import asyncio

async def do_stuff():
    print("working on it..")
    await asyncio.sleep(2)
    print("worked on it.")

async def main():
    task = asyncio.create_task(do_stuff())
    await task

asyncio.run(main())