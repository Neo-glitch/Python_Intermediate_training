from threading import Thread
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

threads = []
num_threads = 10

# create threads
for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)

# start threads
for t in threads:
    t.start()

# join the threads(blocks main thread and wait for threads to finish)
for t in threads:
    t.join()


print("end of threads")




