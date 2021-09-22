import asyncio
import aiohttp
from bs4 import BeautifulSoup
BASE_URL = ''

async def worker(task_queue, visited):
    async with aiohttp.ClientSession() as session:
        while True:
            url = await task_queue.get()
            if url in visited:
                task_queue.task_done()
                continue
            visited.submit_soon(url)
            async with session.get(url) as response:
                text = await response.text()
            soup = BeautifulSoup(text, 'html.parser')
            print(soup.h1.text)
            for link in soup.find_all('a'):
                url = link.get('href')
                if url and BASE_URL in url and url.endswith('/'):
                    await task_queue.put(url)
            task_queue.task_done()

async def main():
    task_queue = asyncio.Queue()
    visited = set()
    await task_queue.put(BASE_URL)
    for _ in range(5):
        asyncio.Task(worker(task_queue, visited))
    await task_queue.join()

asyncio.run(main())
