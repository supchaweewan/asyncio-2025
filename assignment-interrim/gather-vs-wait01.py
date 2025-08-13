import asyncio

async def task_ok(n):
    await asyncio.sleep(n)
    return f"Ok after {n} seconds"

async def task_error(n):
    await asyncio.sleep(n)
    raise ValueError(f"Error after {n} seconds")

async def demo_gather():
    print("\n=== Gather: Return Values ===")
    results = await asyncio.gather(task_ok(1), task_ok(2))
    print("gather results:", results)

    print("\n=== Gather: error stops all ===")
    try:
        await asyncio.gather(task_ok(1), task_error(2))
    except Exception as e:
        print("Caught", repr(e))
    print("\n=== Gather: return_exceptions=True ===")
    results = await asyncio.gather(task_ok(1), task_error(2), return_exceptions=True)
    print("gather results", results)

async def main():
    await demo_gather()

asyncio.run(main())