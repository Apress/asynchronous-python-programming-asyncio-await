import asyncio
import time

def delayed_square_calculator(x, result_callback, future):
    time.sleep(1)
    result = x * x
    result_callback(result, future)

def process_result(result, future):
    future.set_result(result)

async def delayed_square(x):
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    asyncio.Task(
        asyncio.to_thread(delayed_square_calculator, x, process_result, future)
    )

    result = await future
    return result

result = asyncio.run(delayed_square(9))
print(result)
