"""
Semaphores are used to limit the number of concurrent tasks from acccessing a resource.
It can be used to throttle the number of concurrent tasks.
For example, throttling an API call to a maximum of 5 concurrent requests.

Output:

rushik@Rushiks-MacBook-Pro-3 Asynchronous_Python % python3 semaphore.py 
Accessing resource 0
Accessing resource 1
Accessing resource 2
Finished accessing resource 0
Finished accessing resource 1
Finished accessing resource 2
Accessing resource 3
Accessing resource 4
Accessing resource 5
Finished accessing resource 3
Finished accessing resource 4
Finished accessing resource 5
Accessing resource 6
Accessing resource 7
Accessing resource 8
Finished accessing resource 6
Finished accessing resource 7
Finished accessing resource 8
Accessing resource 9
Finished accessing resource 9
"""

import asyncio

async def access_resource(semaphore, resource_id):
    async with semaphore:
        print(f"Accessing resource {resource_id}")
        await asyncio.sleep(1)
        print(f"Finished accessing resource {resource_id}")

async def main():
    semaphore = asyncio.Semaphore(3)
    tasks = [access_resource(semaphore, i) for i in range(10)]
    await asyncio.gather(*tasks)

asyncio.run(main())
    
