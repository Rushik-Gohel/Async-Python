"""
Note: The first two tasks will be executed concurrently.
The third task will execute only after the first two are completed.

Output:

rushik@Rushiks-MacBook-Pro-3 Asynchronous_Python % python3 coroutine_4.py
Coroutine 1 fetching data
Coroutine 2 fetching data
3.0015690326690674
Coroutine 3 fetching data
7.003252983093262
{'data': 'Some data for 1', 'id': 1} {'data': 'Some data for 2', 'id': 2} {'data': 'Some data for 3', 'id': 3}
"""

import asyncio
import time

async def fetch_data(delay, id):
    print(f"Coroutine {id} fetching data")
    await asyncio.sleep(delay)
    return {"data": f"Some data for {id}", "id": id}

async def main():
    start = time.time()
    task1 = asyncio.create_task(fetch_data(2, 1))
    task2 = asyncio.create_task(fetch_data(3, 2))

    result1 = await task1
    result2 = await task2
    print(time.time() - start)
    task3 = asyncio.create_task(fetch_data(4,3))
    
    result3 = await task3
    print(time.time() - start)
    print(result1, result2, result3)

asyncio.run(main())