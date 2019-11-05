import multiprocessing
import os

import time
from Worker import Worker

core_count = multiprocessing.cpu_count()

worker_lst = []
for i in range (core_count):
    temp_worker = Worker()
    mul = multiprocessing.Process(target=temp_worker)
    worker_lst.append(mul)

for w in worker_lst:
    w.start()

for e in worker_lst:
    w.join()

for c in range (len(worker_lst)):
    print("Worker " + str(c) +" is alive: {}".format(worker_lst[c].is_alive()))
