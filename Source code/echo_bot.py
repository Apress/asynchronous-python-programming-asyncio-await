import asyncio

async def handle_echo(reader, writer):
    data = await reader.read(100)
    data = data.upper()
    writer.write(data)
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888
    )

    async with server:
        await server.serve_forever()

asyncio.run(main())
