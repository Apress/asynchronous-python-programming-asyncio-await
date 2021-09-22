import asyncio

import asynchronous_iterator
import asynchronous_generator

async def iterator_loop():
    async for i in asynchronous_iterator.AsyncCounter(5):
        print('Iterator', i)

async def generator_loop():
    async for i in asynchronous_generator.asynchronous_counter(5):
        print('Generator', i)

async def main():
    await asyncio.gather(iterator_loop(), generator_loop())

asyncio.run(main())
