import asyncio
import random

async def divide(x, y):
    await asyncio.sleep(random.random() * 5)
    result = x / y
    return result

async def main():
    number_pairs = [(1, 2), (2, 5), (5, 0), (2, 0), (6, 3)]
    coroutines = [
        divide(x, y)
        for (x, y) in number_pairs
    ]
    results = await asyncio.gather(*coroutines, return_exceptions=True)
    for ((x, y), result) in zip(number_pairs, results):
        if isinstance(result, Exception):
            print(f'{x}/{y} raised: {result}')
        else:
            print(f'{x}/{y} = {result}')
    await asyncio.sleep(5)

random.seed(42)
asyncio.run(main())
