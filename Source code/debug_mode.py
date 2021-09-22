import asyncio
import logging

async def simple_delay():
    await asyncio.sleep(0.1)

async def main():
    coroutines = []
    for _ in range(10_000):
        coroutines.append(simple_delay())
    await asyncio.gather(*coroutines)

logging.basicConfig(level=logging.DEBUG)
asyncio.run(main(), debug=True)
