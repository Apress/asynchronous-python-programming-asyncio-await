import asyncio
import contextvars

id_var = contextvars.ContextVar('IdVar', default='blank')

async def function_c(id, delay):
    print(f'  coro C {id} created, id_var={id_var.get()}')
    id_var.set(id)
    print(f'  coro C {id} set id_var to {id_var.get()}\n')
    await asyncio.sleep(delay)
    print(f'  coro C {id} done, id_var={id_var.get()}')

async def function_b(id, delay):
    print(f'coro B {id} created set id_var to {id_var.get()}')
    id_var.set(id)
    print(f'coro B {id} started, id_var={id_var.get()}\n')
    await asyncio.gather(
        function_c((id, 1), delay + 1),
        function_c((id, 2), delay + 2),
    )
    await asyncio.sleep(1)
    print(f'coro B {id} done, id_var={id_var.get()}')

async def function_a():
    await asyncio.gather(
        function_b(1, 1),
        function_b(2, 5),
    )

asyncio.run(function_a())
