import asyncio

async def function_c(id, delay):
    print(f'  coro C {id} created')
    await asyncio.sleep(delay)
    print(f'  coro C {id} done')

async def function_b(id, delay):
    print(f'coro B {id} created')
    await asyncio.gather(
        function_c((id, 1), delay + 1),
        function_c((id, 2), delay + 2),
    )
    await asyncio.sleep(1)
    print(f'coro B {id} done')

async def function_a():
    await asyncio.gather(
        function_b(1, 1),
        function_b(2, 5),
    )

asyncio.run(function_a())
