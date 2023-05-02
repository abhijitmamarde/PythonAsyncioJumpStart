# SuperFastPython.com
# example of creating and awaiting an asyncio task
import asyncio

# define a coroutine for a task
async def task_coroutine():
    # report a message
    print("executing the task")
    # suspend for a moment
    await asyncio.sleep(1)
    print("task completed...")


# custom coroutine
async def main():
    # report a message
    print("main coroutine")
    # create and schedule the task
    task = asyncio.create_task(task_coroutine())
    # wait for the task to complete
    await task
    print("main completed...")


# start the asyncio program
asyncio.run(main())
