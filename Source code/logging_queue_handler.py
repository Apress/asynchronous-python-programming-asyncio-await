import asyncio
import time
import logging
import logging.handlers
import queue

logger = logging.getLogger('asyncio')
log_queue = queue.SimpleQueue()
queue_handler = logging.handlers.QueueHandler(log_queue)
file_handler = logging.FileHandler('log_file.txt')
listener = logging.handlers.QueueListener(log_queue, file_handler)
listener.start()
logger.addHandler(queue_handler)
logger.setLevel(logging.DEBUG)

async def simple_delay():
    logger.debug('Test log message')
    await asyncio.sleep(1)

async def main():
    start_time = time.time()
    coroutines = []
    for _ in range(10_000):
        coroutines.append(simple_delay())
    await asyncio.gather(*coroutines)
    duration = time.time() - start_time
    print(f'Done, in {duration:.4f} seconds')

asyncio.run(main())
print('Outside of asyncio event loop')
