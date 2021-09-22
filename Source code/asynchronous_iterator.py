import asyncio


class AsyncCounter:
    def __init__(self, number):
        self.number = number
        self.current = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        self.current += 1
        if self.number == self.current:
            raise StopAsyncIteration
        await asyncio.sleep(1)
        return self.current


async def main():
    async for i in AsyncCounter(5):
        print(i)

if __name__ == '__main__':
    asyncio.run(main())
