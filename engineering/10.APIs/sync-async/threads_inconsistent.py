import time
import threading
import queue

"""
Problem with inconsistency:
condition in network call will be True for all 10 threads, because it is checked in the beginning, before sleep and adding to list: calls.append()
To avoid inconsistency, must use Locks
"""
calls = []
def network_call(wait_for: int, q: queue.Queue, calls):
    if len(calls) < 5: # This condition is useless without locks
        print(calls) # always 0 for every run
        time.sleep(wait_for)
        calls.append(wait_for)
        q.put(wait_for)

def main():
    q = queue.Queue()
    threads = []
    for i in range(10):
        thread = threading.Thread(target=network_call, args=(i, q, calls))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    print(q.queue) # returns deque([0, 1, 2, 3, 4])

if __name__ == '__main__':
    start_time = time.time()
    main()
    print(f'Completed at {time.time() - start_time}')
    print(calls)