import time
import threading
import queue

"""
Largest disadwantage of threading - hard to return values from threads;
Need to use queues for that
without Q's return: wait_for is not working;
"""

def network_call(wait_for: int, q: queue.Queue):
    time.sleep(wait_for)
    q.put(wait_for)

def main():
    q = queue.Queue()
    threads = []
    for i in range(5):
        thread = threading.Thread(target=network_call, args=(i, q))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    print(q.queue) # returns deque([0, 1, 2, 3, 4])

if __name__ == '__main__':
    start_time = time.time()
    main()
    print(f'Completed at {time.time() - start_time}')