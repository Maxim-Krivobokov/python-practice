import time
import asyncio

"""
async is working with co-routines, that are executed in a single thread;
so time.sleep() will hand all program; that's why need to use asyncio.sleep()
By default, coroutines are executed sequentially, one by one; 
Total time is 10 seconds - no advantage of using async module here
"""

async def network_call(wait_for: int):
    await asyncio.sleep(wait_for)

async def main():
    tasks = []
    for i in range(5):
        await network_call(wait_for = i)

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print(f"completed at {time.time() - start_time}")