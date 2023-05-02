# SuperFastPython.com
# example of creating and awaiting an asyncio task
import asyncio
from time import perf_counter


# define a coroutine for a task
async def task1_coroutine():
    # report a message
    print("executing the task1")
    # suspend for a moment
    await asyncio.sleep(1)
    print("task1 completed...")
    return 1


async def task2_coroutine():
    # report a message
    print("executing the task2")
    # suspend for a moment
    await asyncio.sleep(2)
    print("task2 completed...")
    return 2


# custom coroutine
async def main():
    # report a message
    start_time = perf_counter()
    print("main coroutine")

    task1 = asyncio.create_task(task1_coroutine())
    task2 = asyncio.create_task(task2_coroutine())

    # still runs one after another
    # await task1
    # await task2

    # to run tasks parallaly
    await asyncio.gather(task1, task2)

    print("main completed...")
    end_time = perf_counter()
    print(f"Time required: {end_time - start_time}")


# start the asyncio program
asyncio.run(main())
