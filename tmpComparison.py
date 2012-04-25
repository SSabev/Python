#!/usr/bin/python

import multiprocessing
from multiprocessing import Pool
import threading
import time

def time_it(func):
    def wrapper(*arg):
        init_time = time.time()
        res = func(*arg)
        after_time = time.time()
        print '%s took %0.3f ms' % (func.func_name, (after_time-init_time)*1000.0)
        return res
    return wrapper


def counter():
    for i in xrange(1000000):
        pass

@time_it
def serialrun(x):
    for i in xrange(x):
        counter()

@time_it
def parallelrun(x):
    proclist = []
    for i in xrange(x):
        p = multiprocessing.Process(target=counter)
        proclist.append(p)
        p.start()

    for i in proclist:
        i.join()

@time_it
def parallelpoolrun(x):
    pool = Pool(processes=5)
    result = pool.apply_async(counter, (x,))

@time_it
def threadedrun(x):
    threadlist = []
    for i in xrange(x):
        t = threading.Thread(target=counter)
        threadlist.append(t)
        t.start()

    for i in threadlist:
        i.join()

def main():
    serialrun(50)
    parallelrun(50)
    threadedrun(50)
    parallelpoolrun(50)

if __name__ == '__main__':
    main()
