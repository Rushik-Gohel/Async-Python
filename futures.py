"""
Futures in asyncio represent the result of an asynchronous operation.

Key Points:
1. A Future is a low-level awaitable object that will eventually hold a result or exception
2. When you await a Future, execution pauses until the Future is resolved (done)
3. Once resolved, the Future contains either:
   - A result value (success)
   - An exception (failure)
4. Futures are typically created by the event loop or libraries, not directly by users
5. Modern async code uses async/await syntax instead of directly manipulating Futures

Note: Most developers work with coroutines and Tasks (which wrap Futures) 
rather than Futures directly.
"""


import asyncio

async def set_future_result(future, value):
    await asyncio.sleep(2)
    # Set the result of the future
    future.set_result(value)
    print(f"Set the future's result to: {value}")

async def main():
    # Create a future object
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    # Schedule setting the future's result
    asyncio.create_task(set_future_result(future, "Future result is ready"))

    # Wait for the future's result
    result = await future
    print(f"Received the future's result: {result}")

asyncio.run(main())