# Hint:
# โค้ดนี้จะพิมพ์ "All tasks scheduled" แล้วจบ ทันที
# เพราะแม้จะ create_task() แต่ถ้าไม่ await มัน → main() จบก่อน → loop ถูกปิด → task ถูก cancel
# ผลลัพธ์คือไม่มี task ไหนทำงานเสร็จจริง

# Result:
# Task-0 started
# Task-1 started
# Task-2 started
# Task-0 finished
# Task-1 finished
# Task-2 finished
# Results: [1, 2, 3]

import asyncio

async def worker(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished")
    return delay

async def main():
    results = []
    tasks = [asyncio.create_task(worker(f"Task-{i}", i+1)) for i in range(3)]
    for t in tasks:
        await t
        results.append(t.result())
    
    print(f"Results: {results}")
    

asyncio.run(main())

# Finished