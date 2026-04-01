"""
Locks in asyncio are used to ensure that only one coroutine can access a shared resource at a time.
The critical section of code is protected by the lock, preventing race conditions.
The lock is acquired before entering the critical section and released after leaving it.
The lock is automatically released when the context manager exits, even if an exception occurs.
"""

import asyncio

shared_resource = 0

lock = asyncio.Lock()

async def modify_shared_resource():
    global shared_resource
    async with lock:
        # Critical section starts
        print("Resource before modification:", shared_resource)
        shared_resource += 1
        await asyncio.sleep(1)
        print("Resource after modification:", shared_resource)
        # Critical section ends
    
async def main():
    tasks = [modify_shared_resource() for _ in range(5)]
    await asyncio.gather(*tasks)
    print("Final value of shared_resource:", shared_resource)

asyncio.run(main())
    
    
