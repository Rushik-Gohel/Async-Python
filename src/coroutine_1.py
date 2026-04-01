"""
Note: Notice that the coroutine does not start executing immediately when it is created.
It only starts executing when it is awaited.
"""

import asyncio

async def fetch_data(delay):
    print('Fetching data ...')
    await asyncio.sleep(delay)
    print('Data fetched')
    return {'data': 'some data'}

async def main():
    print("Start of main coroutine")
    task = fetch_data(2)
    print("End of main coroutine")
    result = await task
    print("Received result:", result)

asyncio.run(main())
