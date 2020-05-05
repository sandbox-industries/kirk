import math
import time

def pathCounter(gridSize):
    p = math.factorial(gridSize*2) / (math.factorial(gridSize)**2)
    return p

start = time.time()
n = pathCounter(20)
stop = time.time()
timeTotal = stop - start
print(n, timeTotal)