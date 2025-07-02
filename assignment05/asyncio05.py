import asyncio
from random import random

async def cook(food, t):
    print(f'Microwave ({food}): Cooking for {t} seconds')
    await asyncio.sleep(t)
    print(f'Microwave ({food}): Finished!')
    return f"{food} was completed in{t}."

async def main():
    tasks = [asyncio.create_task(cook('Rice', 1 + random()))
             , asyncio.create_task(cook('Noodles', 1 + random()))
             , asyncio.create_task(cook('Curry', 1 + random()))]
    done,pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print(f'Completed task: {len(done)} tasks!')
    for completed_task in done:
        print(f' - {completed_task.result()}')
    print(f'Uncompleted tasks: {len(pending)} tasks!')

    for uncompleted in pending:
        uncompleted.cancel()
        print(f' - {uncompleted.get_name()}')

if __name__ == '__main__':
    asyncio.run(main())