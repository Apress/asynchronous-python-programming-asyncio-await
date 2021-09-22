import asyncio
import aiohttp
from bs4 import BeautifulSoup

BASE_URL = 'https://en.wikipedia.org'

async def worker(task_queue):
    async with aiohttp.ClientSession() as session:
        for _ in range(2):
            url = await task_queue.get()
            async with session.get(url) as response:
                text = await response.text()
            soup = BeautifulSoup(text, 'html.parser')
            print(soup.title.text)
            main_body = soup.find(id='mw-content-text')
            for link in main_body.find_all('a'):
                if url := link.get('href'):
                    await task_queue.put(BASE_URL + url)

async def main():
    task_queue = asyncio.Queue()
    url = BASE_URL + '/wiki/Python_(programming_language)'
    await task_queue.put(url)
    workers = [
        worker(task_queue)
        for _ in range(5)
    ]
    await asyncio.gather(*workers)

asyncio.run(main())
