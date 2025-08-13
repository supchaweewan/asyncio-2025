import asyncio

async def task_ok(n):
    await asyncio.sleep(n)
    return f"Ok after {n} seconds"

async def task_error(n):
    await asyncio.sleep(n)
    raise ValueError(f"Error after {n} seconds")

async def demo_wait():
    print("\n=== Wait: Check Status ===")
    tasks = {asyncio.create_task(task_ok(1)), asyncio.create_task(task_ok(2))}
    done, pending = await asyncio.wait(tasks)
    print("done", [t.result() for t in done])
    print("pending", pending)

    print("\n=== Wait: handle errors manually ===")
    tasks = {asyncio.create_task(task_ok(1)), asyncio.create_task(task_error(2))}
    done, pending = await asyncio.wait(tasks)
    for t in done:
        if t.exception():
            print("Error:", t.exception())
        else:
            print("results:", t.result())

    print("\n=== Wait: First Completed ===")
    tasks = {asyncio.create_task(task_ok(1)), asyncio.create_task(task_ok(3))}
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print("First done:", [t.result() for t in done])
    print("Still pending:", len(pending), "tasks")

async def main():
    await demo_wait()

asyncio.run(main())