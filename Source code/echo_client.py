import asyncio

async def chat_with_echo_bot(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888
    )

    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    writer.close()
    await writer.wait_closed()

    return data.decode()

async def main():
    for coroutine in asyncio.as_completed([
        chat_with_echo_bot('Good morning'),
        chat_with_echo_bot('Good afternoon'),
        chat_with_echo_bot('Good evening'),
    ]):
        reply = await coroutine
        print(reply)

asyncio.run(main())
