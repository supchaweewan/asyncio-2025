# example of starting many tasks and getting access to all tasks
import time
import asyncio

async def get_image(name, delay):
    print(f"{time.ctime()} {name} is being downloaded...")
    await asyncio.sleep(delay)
    print(f"{time.ctime()} {name} has finished downloading.")

async def main():
    print(f"{time.ctime()} Main coroutine has started.")
    started_tasks = [asyncio.create_task(get_image(i, i)) for i in range(3)]

    await asyncio.sleep(0.1)
    for task in started_tasks:
        await task


asyncio.run(main())