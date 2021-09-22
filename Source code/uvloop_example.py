import random
import asyncio

import uvloop

async def random_delay(id):
    delay = 5 * random.random()
    print(f'Started {id} delay = {delay:0.2}')
    await asyncio.sleep(delay)
    return id, delay

async def main():
    tasks = [
        asyncio.Task(random_delay(i)) for i in range(10)
    ]

    for coroutine in asyncio.as_completed(tasks):
        id, delay = await coroutine
        print(f'{id} done after {delay:0.2} seconds')

uvloop.install()
asyncio.run(main())
