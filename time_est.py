import time
from distribute_computation import *


class time_est:
    def __init__(self,database,instance,size):
        self._database = database
        self._instance = instance
        self.size = size

    def time_est(self):

        # Benchmarking 1
        if self._instance = 1 and self._database = "Smaller database":
            if self._size = 1000:
                return 2.96
            elif self._size = 2000:
                return 3.95
            elif self._size = 5000:
                return 4.89
            elif self._size = 15000:
                return 14.01
            elif self._size = 30000:
                return 31.96
            elif self._size = 50000:
                return 35.786
            elif self._size = 100000:
                return 53.866
            elif self._size = 500000:
                return 250.33

        # Benchmarking 2
        if self._instance = 1 and self._database = "Bigger database":
            if self._size = 1000:
                return 53.13
            elif self._size = 2000:
                return 111.54
            elif self._size = 5000:
                return 158.5
            elif self._size = 15000:
                return 304.68
            elif self._size = 30000:
                return None
            elif self._size = 50000:
                return None
            elif self._size = 100000:
                return None
            elif self._size = 500000:
                return None

        # Benchmarking 3
        if self._instance = 1 and self._database = "Protein database":
            if self._size = 1:
                return 3.45
            elif self._size = 5:
                return 8.16
            elif self._size = 10:
                return 69.52
            elif self._size = 100:
                return 578.52

        # Benchmarking 4
        if self._instance = 2 and self._database = "Protein database":
            if self._size = 1:
                return 8.34
            elif self._size = 5:
                return None
            elif self._size = 10:
                return None
            elif self._size = 100:
                return None

        # Benchmarking 5
        if self._instance = 4 and self._database = "Protein database":
            if self._size = 1:
                return 4.94
            elif self._size = 5:
                return 19.63
            elif self._size = 10:
                return 43.37
            elif self._size = 100:
                return None

        # Benchmarking 6
        if self._instance = 8 and self._database = "Protein database":
            if self._size = 1:
                return 0.69
            elif self._size = 5:
                return 0.89
            elif self._size = 10:
                return 1.1
            elif self._size = 50:
                return 6.15
            elif self._size = 100:
                return 19.18
