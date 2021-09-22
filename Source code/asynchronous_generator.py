import asyncio


async def asynchronous_counter(number):
    for i in range(1, number):
        yield i
        await asyncio.sleep(1)


async def main():
    async for i in asynchronous_counter(5):
        print(i)

if __name__ == '__main__':
    asyncio.run(main())
