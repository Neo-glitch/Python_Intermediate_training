from multiprocessing import Process
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

processes = []
num_processes = os.cpu_count()  # number of process to be num of cpus

# create processes
for i in range(num_processes):
    p = Process(target=square_numbers)
    processes.append(p)

# start process
for p in processes:
    p.start()

# join the processes(blocks main thread and wait for processes to finish)
for p in processes:
    p.join()


print("end of processes")




