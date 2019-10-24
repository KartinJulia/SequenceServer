#import time_est
#from distribute_computation import *
import time


class Cache:
    def __init__(self,user_id):
        self._catch = []
        self._id = user_id
    def release(self):
        self._cache = []

    def add(self,worker):
        self._cache.append(worker)

    def search(self,worker):
        for i in self._catch:
            if worker._id == i._id:
                return i._result
