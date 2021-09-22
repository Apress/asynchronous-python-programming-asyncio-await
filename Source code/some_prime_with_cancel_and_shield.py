import asyncio
import random

async def prime_checker(n):
    try:
        await asyncio.sleep(random.random() * 5)
    except asyncio.CancelledError:
        return
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return n, False
    return n, True

async def one_prime():
    start = 1_000_000
    coroutines = []
    for i in range(start, start + 1000):
        coroutines.append(prime_checker(i))
    for coroutine in asyncio.as_completed(coroutines):
        number, is_prime = await coroutine
        if is_prime:
            print(number)
            break
    for task in asyncio.all_tasks():
        try:
            task.cancel()
        except asyncio.CancelledError:
            pass

async def main():
    await asyncio.shield(one_prime())

asyncio.run(main())
