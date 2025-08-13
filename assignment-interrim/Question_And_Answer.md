# Question
1. ถ้าสร้าง asyncio.create_task(*tasks) ที่ไม่มี await ที่ main() เกิดอะไรบ้าง
   1. เกิด Fire-And-Forget คือการดำเนินการ task ไป และ event loop จะเดินต่อไป
   2. เกิดการที่ จะไม่สามารถรับ task exception ได้ถ้ากำหนดขึ้นมา
   3. main event loop จะดำเนินและเสร็จสิ้นก่อนที่ task จะทำงานสำเร็จได้
2. ความแตกต่างระหว่าง asyncio.gather(*tasks) กับ asyncio.wait(tasks) คืออะไร
   1. gather เก็บผลของ task ทั้งหมดเมื่อเสร็จหมดแล้ว ส่วน wait ทำการรอ task ถ้าเสร็จออกผลเป็น Done + ค่า Return ถ้าไม่เสร็จออกผลเป็น Pending
   2. gather สามารถกำหนดการจับ error ได้ง่าย ให้หยุดถ้าพบ error ส่วน wait ต้องการกำหนดการจับตรวจ error เองแบบ manual
   3. gather สามารถกำหนด return_exceptions ได้ แต่ wait สามารถกำหนดว่าควรคืนค่าได้อย่างไร เช่น FIRST_COMPLETED หรือ ALL COMPLETED
3. สร้าง create_task() และ coroutine ของ http ให้อะไรต่างกัน
   1. create_task() ส่งผล result แบบตามลำดับที่กำหนด ส่วน coroutine ส่งผล result ตามว่าอันไหนเสร็จก่อน
   2. task มีหลาย method ที่สามารถใช้ควบคุมได้ที่ coroutine ไม่มี เช่น result(), cancel(), exception()
   3. create_task() สามารถอาศัยให้เป็น reference ที่จัดการต่อไปได้
