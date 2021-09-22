import asyncio

async def event_listener_a(some_event):
    print('Listener A, waiting for the event')
    await some_event.wait()
    print('Listener A, the event happened')

async def event_listener_b(some_event):
    print('Listener B, also waiting')
    await some_event.wait()
    print('Listener B, got it, thanks')

async def event_trigger(some_event):
    await asyncio.sleep(2)
    print('About to trigger the event')
    some_event.set()
    print('Event triggered, time of a nap')
    await asyncio.sleep(0.001)

async def main():
    some_event = asyncio.Event()
    coroutines = [
        event_listener_a(some_event),
        event_listener_b(some_event),
        event_trigger(some_event)
    ]
    await asyncio.gather(*coroutines)
    print('All done')

asyncio.run(main())
