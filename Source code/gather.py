import asyncio

async def countdown(name, number):
    print(name, 'started')
    for i in range(number, 0, -1):
        print(name, i)
        await asyncio.sleep(1)

async def main():
    task_a = asyncio.Task(countdown('Task A', 5))
    task_b = asyncio.Task(countdown('Task B', 6))
    await asyncio.sleep(3)
    print('Main done sleeping, about to await .gather')
    await asyncio.gather(task_a, task_b)
    print('All done')

asyncio.run(main())
print('Outside of asyncio event loop')
