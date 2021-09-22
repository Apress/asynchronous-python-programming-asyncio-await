import asyncio


async def some_timeconsuming_task(id):
    print('Started', id)
    await asyncio.sleep(10)
    print('All done', id)


async def main():
    task1 = asyncio.Task(some_timeconsuming_task(1))
    task2 = asyncio.Task(some_timeconsuming_task(2))

    print('gather - waiting for tasks to finish')
    await asyncio.gather(task1, task2)


asyncio.run(main())
