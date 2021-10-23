from threading import Thread, Lock, current_thread
from queue import Queue  
import time


def worker(q, lock):
    while True:
        value = q.get()   # waits for queue to have element

        with lock:
            #processing..
            print(f"in {current_thread().name} got {value}\n")
        q.task_done()

if __name__ == '__main__':

    q = Queue()
    # q.put(1)
    # q.put(2)
    # q.put(3)

    # first = q.get()
    # print(first)

    # q.task_done()
    # q.join()   # wait on queue until all elements processed
    # # print(q.empty())    # check if queue is empty

    num_threads = 10
    lock = Lock()

    for i in range(num_threads):
        thread = Thread(target=worker, args =(q,lock))
        thread.daemon = True   # means die when main thread is dead
        thread.start()

    for i in range(1, 21):
        q.put(i)

    q.join()

    print("end main")