import time
import asyncio
import aiohttp

student_id = "6610301014"

async def fire_rocket(name: str, t0: float):
    url = f"http://172.16.2.117:8088/fire/{student_id}"
    start_time = time.perf_counter() - t0  # เวลาเริ่มสัมพัทธ์
    """
    TODO:
    - ส่ง GET request ไปยัง rocketapp ที่ path /fire/{student_id}
    - อ่านค่า time_to_target จาก response
    - return dict ที่มี:
        {
            "name": name,
            "start_time": start_time,
            "time_to_target": time_to_target,
            "end_time": end_time
        }
    """
    rocket = {
        "name": name,
        "start_time": start_time,
        "time_to_target": 0,
        "end_time": 0
    }
    async with aiohttp.ClientSession() as Client:
        resp = await Client.get(url)
        info = await resp.json()
        rocket["time_to_target"] = info["time_to_target"]
        rocket["end_time"] = info["time_to_target"]-start_time
        return(rocket["name"], rocket["start_time"], rocket["time_to_target"], rocket["end_time"])
    

async def main():
    t0 = time.perf_counter()  # เวลาเริ่มของชุด rockets
    rockets = [1, 2, 3]
    total_time = []

    print("Rocket prepare to launch ...")  # แสดงตอนเริ่ม main

    # TODO: สร้าง task ยิง rocket 3 ลูกพร้อมกัน
    tasks = [asyncio.create_task(fire_rocket(i, t0)) for i in rockets]

    # TODO: รอให้ทุก task เสร็จและเก็บผลลัพธ์ตามลำดับ task
    results = await asyncio.gather(*tasks)

    # TODO: แสดงผล start_time, time_to_target, end_time ของแต่ละ rocket ตามลำดับ task
    print("Rockets fired:\n")

    for r in results:
        print(f"Rocket-{r[0]} | start_time: {r[1]:.2f} sec | time_to_target: {r[2]:.2f} sec | end_time: {r[3]:.2f} sec")
        pass  # แสดงผล rocket

    # TODO: แสดงเวลารวมทั้งหมดตั้งแต่ยิงลูกแรกจนลูกสุดท้ายถึงจุดหมาย
    total_time.append(r[3])
    total_time.sort()
    t_total = total_time[0] # คำนวณ max end_time
    print(f"\nTotal time for all rockets: {t_total:.2f} sec")


asyncio.run(main())