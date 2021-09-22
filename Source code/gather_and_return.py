import random
import asyncio

async def is_prime_test(x):
    await asyncio.sleep(random.random())
    for i in range(2, x):
        if x % i == 0:
            return x, False
    print(x)
    return x, True

async def main():
    tasks = []
    for number in range(2, 100):
        tasks.append(asyncio.Task(is_prime_test(number)))
    results = await asyncio.gather(*tasks)
    print('Primes: ', end=' ')
    for x, is_prime in results:
        if is_prime:
            print(x, end=' ')

random.seed(42)
asyncio.run(main())
