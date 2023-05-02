# SuperFastPython.com
# example of gather for many coroutines in a list
import asyncio
from random import random

# coroutine used for a task
async def task_coro(value):
    # report a message
    print(f">task {value} executing")
    # sleep for a moment
    await asyncio.sleep(random())
    return value, random()


# coroutine used for the entry point
async def main():
    # report a message
    print("main starting")
    # create many coroutines
    coros = [task_coro(i) for i in range(10)]
    # run the tasks
    results = await asyncio.gather(*coros)
    # report a message
    print("main done")
    print(f"results: {results}")


# start the asyncio program
asyncio.run(main())
