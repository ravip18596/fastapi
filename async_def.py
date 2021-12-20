import asyncio


async def do_something():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')