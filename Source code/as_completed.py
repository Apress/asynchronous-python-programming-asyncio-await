import random
import asyncio

async def is_prime_test(x):
    await asyncio.sleep(random.random() * 5)
    for i in range(2, x):
        if x % i == 0:
            return x, False
    return x, True

async def main():
    tasks = []
    for number in range(2, 100):
        tasks.append(asyncio.Task(is_prime_test(number)))

    primes_found = 0
    for coroutine in asyncio.as_completed(tasks):
        x, is_prime = await coroutine
        if not is_prime:
            continue
        primes_found += 1
        print(primes_found, x)
        if primes_found >= 10:
            break

random.seed(42)
asyncio.run(main())
