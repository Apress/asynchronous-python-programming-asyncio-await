import asyncio
import random

async def divide(x, y):
    await asyncio.sleep(random.random() * 5)
    print(f'{x} / {y} = ', end='')
    result = x / y
    print(result)
    return result

async def main():
    coroutines = [
        divide(x, y)
        for (x, y) in [(1, 2), (2, 5), (5, 0), (2, 0), (6, 3)]
    ]
    first = True
    for coroutine in asyncio.as_completed(coroutines):
        if first:
            await asyncio.sleep(6)
            first = False
        await coroutine

    await asyncio.sleep(5)

random.seed(42)
asyncio.run(main())
