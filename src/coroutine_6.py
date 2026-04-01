"""
TaskGroup: Key Features and Usage
Structured Concurrency: The primary benefit of TaskGroup is the robust management of the task lifecycle. When the async with block is exited, the program automatically waits for all created tasks to finish.
Automatic Cancellation and Error Handling: If any task within the group raises an exception (other than CancelledError), the TaskGroup automatically cancels the remaining running tasks, preventing "zombie" tasks from running indefinitely in the background. The exception is then re-raised after all other tasks have been cleaned up, often as an ExceptionGroup if multiple errors occurred, which can be handled with the new except* syntax in Python 3.11+.
Dynamic Task Creation: Unlike asyncio.gather(), which requires all awaitables to be specified upfront, TaskGroup allows you to create new tasks dynamically within the async with block (even from within other tasks in the same group).
Simpler Syntax: It uses the async with statement, making the code cleaner and easier to reason about.

Output:
rushik@Rushiks-MacBook-Pro-3 Asynchronous_Python % python3 coroutine_6.py
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
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2,1,3], start=1):
            task = tg.create_task(fetch_data(sleep_time,i))
            tasks.append(task)

    for task in tasks:
        print(task.result())

asyncio.run(main())
