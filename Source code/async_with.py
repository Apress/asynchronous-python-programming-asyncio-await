import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://example.com') as response:
            print(response.status)

asyncio.run(main())
