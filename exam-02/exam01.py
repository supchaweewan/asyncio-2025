# ให้เขียนโปรแกรมหาจำนวนเฉพาะที่ ≤ n แบบ อะซิงโครนัส
# โปรแกรมต้องรองรับการคำนวณ หลายค่า n พร้อมกัน
# นักศึกษาต้องเติมโค้ดที่ทำการ หาจำนวนเฉพาะ และ สร้าง task

# Hint:
# 1. ฟังก์ชัน is_prime(num) → return True ถ้า num เป็น prime, False ถ้าไม่ใช่
# 2. ใน primes_up_to(n) → ใช้ loop หรือ list comprehension เพื่อหา prime numbers 2..n
# 3. ใช้ asyncio.create_task() เพื่อสร้าง task สำหรับแต่ละค่า n
# 4. ใช้ await เพื่อรอผลลัพธ์ของแต่ละ task ก่อนพิมพ์ผลลัพธ์

# Result:
# Primes <= 10: [2, 3, 5, 7]
# Primes <= 20: [2, 3, 5, 7, 11, 13, 17, 19]
# Primes <= 30: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

import asyncio
from typing import List

# ฟังก์ชันตรวจสอบจำนวนเฉพาะ
def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# ฟังก์ชันหาจำนวนเฉพาะ ≤ n แบบ async
async def primes_up_to(n: int) -> List[int]:
    # yield control เพื่อไม่ block event loop
    await asyncio.sleep(0)
    return [x for x in range(2, n + 1) if is_prime(x)]

async def main():
    ns = [10, 20, 30]  # ตัวอย่างหลายค่า
    tasks = []
    values = [asyncio.create_task(primes_up_to(n)) for n in ns]
    for v in values:
        await v
        tasks.append(v.result())
    print("Primes <= 10", tasks[0])
    print("Primes <= 20", tasks[1])
    print("Primes <= 30", tasks[2])
    pass

# เรียก main
asyncio.run(main())

# Finished