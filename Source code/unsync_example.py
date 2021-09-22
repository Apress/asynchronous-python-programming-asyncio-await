import asyncio
import time
from unsync import unsync

@unsync
async def some_coroutine_function():
    await asyncio.sleep(1)
    return 'Coroutine done'

@unsync
def some_blocking_function():
    time.sleep(1)
    return 'blocking function done'

@unsync(cpu_bound=True)
def some_cpu_intensive_function():
    x = 1
    for i in range(2, 25_000):
        x *= i
    return x

start_time = time.time()
future_coroutine_result = some_coroutine_function()
future_function_result = some_blocking_function()
future_cpu_intensive_result = some_cpu_intensive_function()

print(future_coroutine_result.result())
print(future_function_result.result())
print(f'{len(str(future_cpu_intensive_result.result()))} digits in 25,000\'s factorial ')
print(time.time() - start_time, 'seconds')
