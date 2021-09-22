import asyncio
import random

total = 0

async def counter():
    global total
    await asyncio.sleep(0.1 * random.random())
    in_progress = total
    await asyncio.sleep(0.00001 * random.random())
    in_progress += 1
    await asyncio.sleep(0.00001 * random.random())
    total = in_progress

async def main():
    coroutines = [
        counter()
        for _ in range(1000)
    ]
    await asyncio.gather(*coroutines)
    print('Final result:', total)

asyncio.run(main())
