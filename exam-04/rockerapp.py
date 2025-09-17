# file: rocketapp.py

from fastapi import FastAPI, HTTPException
import asyncio
import random

app = FastAPI(title="Asynchronous Rocket Launcher")

# เก็บ task ของจรวด (optional)
rockets = []

async def launch_rocket(student_id: str):
    """
    TODO:
    - จำลองเวลาจรวดด้วย random delay 1-2 วินาที
    - print log ว่า rocket launched และ reached destination
    """
    delay = random()

    
    print(f"Rocket {student_id} launched! ETA: {delay:.2f} seconds")
    await asyncio.sleep(delay)
    print(f"Rocket {student_id} reached destination after {delay:.2f} seconds")
    return delay
    pass

@app.get("/fire/{student_id}")
async def fire_rocket(student_id: str):
    """
    TODO:
    - ตรวจสอบ student_id ต้องเป็น 10 หลัก
    - สร้าง background task ยิง rocket
    - รอ random delay 1-2 วินาที ก่อนส่ง response
    - return dict {"message": ..., "time_to_target": ...}
    """
    try:
        if student_id.isdigit() == True and len(student_id) == 10:
            launch = asyncio.create_task(launch_rocket(student_id))
            await launch
            return [{"name": student_id, "time_to_target": launch}]
        else:
            raise ValueError("Student ID must be 10 digits")
        



    except Exception as e:
        return[{"Detail": str(e)}]

    pass
