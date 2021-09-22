import asyncio
import random

async def divide(x, y):
    await asyncio.sleep(random.random() * 5)
    print(f'{x} / {y} = ', end='')
    result = x / y
    print(result)


async def main():
    coroutines = [
        divide(x, y)
        for (x, y) in [(1, 2), (2, 5), (5, 0), (2, 0), (6, 3)]
    ]
    try:
        await asyncio.gather(*coroutines)
    except ZeroDivisionError:
        print('Division by zero error')

    await asyncio.sleep(6)

random.seed(42)
asyncio.run(main())
