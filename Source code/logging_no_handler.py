import asyncio
import time
import logging

async def simple_delay():
    logging.debug('Test log message')
    await asyncio.sleep(0.1)

async def main():
    start_time = time.time()
    coroutines = []
    for _ in range(10_000):
        coroutines.append(simple_delay())
    await asyncio.gather(*coroutines)
    duration = time.time() - start_time
    print(f'Done, in {duration:.4f} seconds')

asyncio.run(main())
print('Outside of asyncio event loop')
