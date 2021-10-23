from multiprocessing import Process, Lock, \
    Value, Array, Queue  # needed for multiprocess comm
from multiprocessing import Pool
import os
import time


def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1


def add_100_array(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1


def square(numbers, q, lock):
    for i in numbers:
        with lock:
            q.put(i**2)


def make_negative(numbers, q, lock):
    for i in numbers:
        with lock:
            q.put(-1 * i)

def cube(number):
    return number **3


if __name__ == "__main__":

    lock = Lock()
    # shared_number = Value("i", 0)   # data type = int and start val = 0. share just single value
    # print("Number at beginning is ", shared_number.value)
    # p1 = Process(target=add_100, args=(shared_number, lock))
    # p2 = Process(target=add_100, args=(shared_number, lock))

    # shared_array = Array("d", [0.0, 100.0, 200.0])
    # print("array at the beginning is", shared_array[:])

    # p1 = Process(target=add_100_array, args=(shared_array, lock))
    # p2 = Process(target=add_100_array, args=(shared_array, lock))

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    # # print("number at end is ", shared_number.value)
    # print("number at end is ", shared_array[:])

    q = Queue()

    p1 = Process(target=square, args=([1, 2, 3, 4, 5 ,6], q, lock))
    p2 = Process(target=make_negative, args=([1, 2,3, 4, 5,6], q, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())

    ### Processing pool
    print("\n")   

    numbers = range(10)
    pool = Pool()

    # create as many processors on machine and split iterable into chunks for parallel computting
    result = pool.map(cube, numbers) 

    pool.close()
    pool.join()   # wait for pool
    print(result)
    


