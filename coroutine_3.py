"""
Note: Notice that all the three tasks get completed within 3 seconds.
create_task helps in running tasks concurrently
"""

import asyncio

async def fetch_data(delay, id):
    print(f"Coroutine {id} fetching data")
    await asyncio.sleep(delay)
    return {"data": f"Some data for {id}", "id": id}

async def main():
    task1 = asyncio.create_task(fetch_data(1, 2))
    task2 = asyncio.create_task(fetch_data(2, 3))
    task3 = asyncio.create_task(fetch_data(3,1))

    result1 = await task1
    result2 = await task2
    result3 = await task3
    
    print(result1, result2, result3)

asyncio.run(main())