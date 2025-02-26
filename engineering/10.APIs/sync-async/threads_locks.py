import time
import threading
import queue

"""
Problem with inconsistency:
Locks are used to prevent data inconsistency (calls will be empty list for all network calls)
But with locks - totasl time will be the same as with sync code, for 5 iterations = 10sec
"""
calls = []
def network_call(wait_for: int, q: queue.Queue, calls, lock: threading.Lock):
    lock.acquire()
    if len(calls) < 5:
        print(calls) # always 0 for every run
        time.sleep(wait_for)
        calls.append(wait_for)
        q.put(wait_for)
    lock.release()

def main():
    q = queue.Queue()
    threads = []
    lock = threading.Lock()
    for i in range(10):
        thread = threading.Thread(target=network_call, args=(i, q, calls, lock))
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