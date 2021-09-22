import asyncio
import random
import string

connection_semaphore = None
connections = []

async def get_info(id):
    await asyncio.sleep(0.1 * random.random())

    async with connection_semaphore:
        connections.append(id)
        await asyncio.sleep(0.1 * random.random())
        print('Getting info, open connections: ', connections)
        await asyncio.sleep(0.1 * random.random())
        connections.remove(id)

async def main():
    global connection_semaphore
    connection_semaphore = asyncio.Semaphore(5)
    coroutines = [
        get_info(character)
        for character in string.ascii_lowercase
    ]
    await asyncio.gather(*coroutines)
    print('Done')
    print('Open connections:', connections)

asyncio.run(main())
