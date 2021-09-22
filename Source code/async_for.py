import asyncio

async def async_counter(number):
    for i in range(number):
        await asyncio.sleep(1)
        yield i

async def main():
    async for i in async_counter(5):
        print(i)

asyncio.run(main())
