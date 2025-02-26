import time
import asyncio

"""
async is working with co-routines, that are executed in a single thread;

By default, coroutines are executed sequentially, one by one; 
we append them to list with "asyncio.create_task()"; 
then we use await to get results
At  last - print the results for every coroutine

Result: Total time is 4 seconds;
"""

async def network_call(wait_for: int):
    await asyncio.sleep(wait_for)
    return wait_for

async def main():
    tasks = []
    for i in range(5):
        tasks.append(asyncio.create_task(network_call(wait_for = i)))
    
    await asyncio.wait(tasks)

    for task in tasks:
        print(task.result())

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print(f"completed at {time.time() - start_time}")