import time
import asyncio

def blocking(i):
    time.sleep(1)
    return f'blocking {i}'

async def non_blocking(i):
    await asyncio.sleep(1)
    return f'non-blocking {i}'

async def main():
    start_time = time.time()

    coroutines = []
    for i in range(5):
        coroutines.append(asyncio.to_thread(blocking, i))
        coroutines.append(non_blocking(i))

    for result in await asyncio.gather(*coroutines):
        print(result)

    print(f'Duration {time.time() - start_time:0.3f} seconds')

asyncio.run(main())
