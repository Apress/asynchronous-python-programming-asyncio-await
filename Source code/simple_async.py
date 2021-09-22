import asyncio

async def slow_calculator(x):
    await asyncio.sleep(1)
    return x * x

async def main():
    for i in range(2, 11):
        square = await slow_calculator(i)
        print(i, square)

main_coroutine = main()
asyncio.run(main_coroutine)
