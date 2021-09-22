import asyncio

class APIClient:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    async def __aenter__(self):
        await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await asyncio.sleep(1)

    async def send(self, data):
        await asyncio.sleep(1)
        print('Sent', data)

async def main():
    print('started')
    async with APIClient('user:Fred, password:Hello') as client:
        print('client created')
        await client.send('Hello')
        print('End of context')

    print('Done')

if __name__ == '__main__':
    asyncio.run(main())
