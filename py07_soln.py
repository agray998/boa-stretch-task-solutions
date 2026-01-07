#! venv/bin/python3
import requests
import asyncio
import aiohttp

async def process_data(queue):
    book = await queue.get()
    outstr = ""
    for k in book.keys():
        outstr += f"{k.upper()}: {str(book.get(k))}\n"
    await asyncio.sleep(1)
    print(outstr)

async def main():
    books_queue = asyncio.Queue()
    authors_queue = asyncio.Queue()
    async with aiohttp.ClientSession('http://localhost:5000') as session:
        async with session.get('/api/books') as books:
            books = await books.json()
            for book in books:
                await books_queue.put(book)
            procs = [process_data(books_queue) for book in books]
            await asyncio.gather(*procs)
        async with session.get('/api/authors') as authors:
            authors = await authors.json()
            for author in authors:
                await authors_queue.put(author)
            procs = [process_data(authors_queue) for author in authors]
            await asyncio.gather(*procs)

if __name__ == '__main__':
    asyncio.run(main())