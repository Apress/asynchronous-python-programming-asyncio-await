import asyncio
import random

async def divide(x, y):
    delay = random.random() * 5
    await asyncio.sleep(delay)
    print(f'{x} / {y} = ', end='')
    result = x / y
    print(result)
    return result

async def main():
    coroutines = [
        divide(x, y)
        for (x, y) in [(1, 2), (2, 5), (5, 0), (2, 0), (6, 3)]
    ]
    for coroutine in asyncio.as_completed(coroutines):
        try:
            await coroutine
        except ZeroDivisionError:
            print('Division by zero error')

    await asyncio.sleep(5)

random.seed(42)
asyncio.run(main())
