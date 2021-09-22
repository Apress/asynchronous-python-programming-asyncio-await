import asyncio

async def clock(label):
    for i in range(100_000):
        print(label, i)
        await asyncio.sleep(1)

async def desktop():
    await asyncio.gather(
        clock('bare'),
        asyncio.shield(clock('shielded'))
    )

async def main():
    desktop_task = asyncio.Task(desktop())
    await asyncio.sleep(3)
    desktop_task.cancel()
    await asyncio.sleep(10)

asyncio.run(main())
