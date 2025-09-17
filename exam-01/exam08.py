# Hint:
# โค้ดนี้จะทำงานได้ แต่เกิด ResourceWarning: Unclosed client session
# ให้นักศึกษาแก้ไขโดยใช้ async with aiohttp.ClientSession()
# Result:
# 1256

import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session: # ไม่ปิด
        resp = await session.get(url)
        return await resp.text()

async def main():
    html = await fetch("https://example.com")
    print(len(html))

asyncio.run(main())

# Finished