import time
from time import clock
import os
import timeit

start = time.clock()
runTime = time.time()

#python
print("Language detected: Python")
print("Memory (CPU): %s" % ((time.clock() - start)))
print("Runtime: %s" % (time.time() - runTime))
# print("Memory Usage: %s" % (os.stat)

#javascript
print("Language detected: JavaScript")
print("Memory (CPU): %s" % (time.clock() - start))
print("Runtime: %s" % (time.time() - runTime))

#C
print("Language detected: C")
print("Memory (CPU): %s" % (time.clock() - start))
print("Runtime: %s" % (time.time() - runTime))
