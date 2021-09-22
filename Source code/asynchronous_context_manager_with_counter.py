import asyncio

from asynchronous_context_manager import APIClient

async def client_demo():
    print('started')
    async with APIClient('user:Fred, password:Hello') as client:
        print('client created')
        await client.send('Hello')
        print('End of context')

    print('Done')

async def counting():
    for i in range(5):
        print('counting', i)
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(client_demo(), counting())

asyncio.run(main())
