import asyncio
import logging

asyncio_logger = logging.getLogger('asyncio')
stream_handler = logging.StreamHandler()
asyncio_logger.addHandler(stream_handler)

asyncio_logger.setLevel(logging.DEBUG)

async def test():
    print("Some demo output")

async def main():
    await test()

asyncio.run(main())
