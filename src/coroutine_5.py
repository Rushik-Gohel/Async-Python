"""
Note: gather runs tasks concurrently.
Important to note that gather does not provide error handling. So if one task fails, it will still execute others.

Output:

rushik@Rushiks-MacBook-Pro-3 Asynchronous_Python % python3 coroutine_5.py
Coroutine 1 fetching data
Coroutine 2 fetching data
Coroutine 3 fetching data
{'data': 'Some data for 1', 'id': 1}
{'data': 'Some data for 2', 'id': 2}
{'data': 'Some data for 3', 'id': 3}
"""

import asyncio


async def fetch_data(delay, id):
    print(f"Coroutine {id} fetching data")
    await asyncio.sleep(delay)
    return {"data": f"Some data for {id}", "id": id}


async def main():
    results = await asyncio.gather(fetch_data(1, 1), fetch_data(2, 2), fetch_data(3, 3))
    
    for result in results:
        print(result)


asyncio.run(main())
