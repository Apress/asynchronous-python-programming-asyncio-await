import asyncio
import logging

logging.basicConfig(level=logging.DEBUG)

async def test():
    print("Some demo output")

async def main():
    await test()

asyncio.run(main())
