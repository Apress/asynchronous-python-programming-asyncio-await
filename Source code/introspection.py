import asyncio
import random

async def simple_function():
    await asyncio.sleep(random.random() * 5)

async def monitor():
    while True:
        task_count = len(asyncio.all_tasks())
        print(task_count)
        if task_count <= 2:
            asyncio.current_task().print_stack()
            return
        await asyncio.sleep(0.5)

async def main():
    tasks = []
    tasks.append(asyncio.Task(monitor()))
    for _ in range(100):
        tasks.append(asyncio.Task(simple_function()))

    await asyncio.gather(*tasks)

asyncio.run(main())
