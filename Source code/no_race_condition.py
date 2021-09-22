import asyncio
import random

total = 0

async def counter():
    global total
    await asyncio.sleep(0.1 * random.random())
    total += 1

async def main():
    coroutines = [
        counter()
        for _ in range(1000)
    ]
    await asyncio.gather(*coroutines)
    print('Final result:', total)

asyncio.run(main())
