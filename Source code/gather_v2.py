import asyncio

async def countdown(name, number):
    print(name, 'started')
    for i in range(number, 0, -1):
        print(name, i)
        await asyncio.sleep(1)

async def main():
    tasks = [
        asyncio.Task(countdown('Task A', 5)),
        asyncio.Task(countdown('Task B', 4)),
        asyncio.Task(countdown('Task C', 3))
    ]
    await asyncio.sleep(3)
    print('Main done sleeping, about to await .gather')
    await asyncio.gather(*tasks)
    print('All done')

asyncio.run(main())
print('Outside of asyncio event loop')
