# SuperFastPython.com
# example of an async context manager via async with
import asyncio
from random import random

# define an asynchronous context manager
class AsyncContextManager:
    # enter the async context manager
    async def __aenter__(self):
        # report a message
        print(">entering the context manager")
        # suspend for a moment
        await asyncio.sleep(0.5)
        return self

    async def call_me(self, arg):
        print(f">inside context manager: call_me({arg=})")
        value = random()
        await asyncio.sleep(0.5)
        print(f"done call_me({arg=})...")
        return arg, value

    # exit the async context manager
    async def __aexit__(self, exc_type, exc, tb):
        # report a message
        print(">exiting the context manager")
        # suspend for a moment
        await asyncio.sleep(0.5)


# define a simple coroutine
async def custom_coroutine():
    # create and use the asynchronous context manager
    async with AsyncContextManager() as manager:
        # report the result
        print("within the manager0")
        res0 = await manager.call_me(0)
    async with AsyncContextManager() as manager:
        # report the result
        print("within the manager1")
        res1 = await manager.call_me(1)
    async with AsyncContextManager() as manager:
        # report the result
        print("within the manager2")
        res2 = await manager.call_me(2)
    print(res0, res1, res2)


# start the asyncio program
asyncio.run(custom_coroutine())
