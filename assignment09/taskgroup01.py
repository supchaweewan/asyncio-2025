import asyncio

async def task1():
    print("Hello from coroutine 1")
    await asyncio.sleep(1)

async def task2():
    print("Hello from coroutine 2")
    await asyncio.sleep(1)

async def task3():
    print("Hello from coroutine 3")
    await asyncio.sleep(1)

async def main():
    async with asyncio.TaskGroup() as group:
        group.create_task(task1())
        group.create_task(task2())
        group.create_task(task3())
    print("Done")

asyncio.run(main())