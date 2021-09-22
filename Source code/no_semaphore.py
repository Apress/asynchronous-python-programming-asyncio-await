import asyncio
import random
import string

connections = []

async def get_info(id):
    await asyncio.sleep(0.1 * random.random())
    connections.append(id)
    await asyncio.sleep(0.1 * random.random())
    print('Getting info, open connections: ', connections)
    await asyncio.sleep(0.1 * random.random())
    connections.remove(id)

async def main():
    coroutines = [
        get_info(character)
        for character in string.ascii_lowercase
    ]
    await asyncio.gather(*coroutines)
    print('Done')
    print('Open connections:', connections)

asyncio.run(main())
