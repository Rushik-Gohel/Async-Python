"""
Note: Notice that it takes 4 seconds for the tasks to execute.
This is because the second task does not start until the first one completes.
So we did not get any performance benefit here.
"""

import asyncio

async def fetch_data(delay, id):
    print("Fetching data... id:", id)
    await asyncio.sleep(delay)
    print("Data fetched, id:", id)
    return {"data": "Some data", "id": id}

async def main():
    task1 = fetch_data(2, 1)
    task2 = fetch_data(2, 2)

    result1 = await task1
    print(f"Received result: {result1}")

    result2 = await task2
    print(f"Received result: {result2}")

asyncio.run(main())