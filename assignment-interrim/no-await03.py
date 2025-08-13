import asyncio, time

async def worker_long():
    print(f'{time.ctime()} [worker_long] is working.')
    try:
        await asyncio.sleep(5)
        print(f'{time.ctime()} [worker_long] worked.')
    except asyncio.CancelledError:
        print(f'{time.ctime()} [worker_long] has been cancelled!')

async def main():
    print(f'{time.ctime()} starting da loop..')
    asyncio.create_task(worker_long())
    await asyncio.sleep(1)
    print(f'{time.ctime()} loop finnished')

asyncio.run(main())