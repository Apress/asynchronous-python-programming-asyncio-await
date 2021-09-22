import asyncio

random_durations = iter([4, 3, 2, 6])

async def long_running_task():
    print()
    duration = next(random_durations)
    print(f'This will take {duration} seconds')
    await asyncio.sleep(duration)
    print('Done')

async def main():
    while True:
        try:
            await asyncio.wait_for(long_running_task(), 3)
            break
        except asyncio.TimeoutError:
            print('Too long, try again')

asyncio.run(main())
