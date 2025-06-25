# example of getting the current task from the main coroutine
import asyncio

async def main():

    print('main coroutine has started')
    task = asyncio.current_task()

    print(task)

asyncio.run(main())