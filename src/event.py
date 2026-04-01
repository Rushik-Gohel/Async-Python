"""
Event objects are used to signal between coroutines.
They are useful when you want to wait for a specific condition to be met.

Output:

rushik@Rushiks-MacBook-Pro-3 Asynchronous_Python % python3 event.py    
waiting for the event to be set
event has been set!
event has been set, continuing execution
"""

import asyncio

async def waiter(event):
    print("waiting for the event to be set")
    await event.wait()
    print("event has been set, continuing execution")

async def setter(event):
    await asyncio.sleep(2)  # Simulate doing some work
    event.set()
    print("event has been set!")

async def main():
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))

asyncio.run(main())
