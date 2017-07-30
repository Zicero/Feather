import time
from time import clock
import os
import timeit

start = time.clock()
end = time.clock()

#python
print("Language detected: Python")
print("Memory (CPU): %s" % (time.clock() - start))
print("Runtime: %s" % (end - (time.clock() - start))
# print("Memory Usage: %s" % (os.stat)

#javascript
print("Language detected: JavaScript")
print("Memory (CPU): %s" % (time.clock() - start))
print("Runtime: %s" % (end - (time.clock() - start))

#C
print("Language detected: C")
print("Memory (CPU): %s" % (time.clock() - start))
print("Runtime: %s" % (end - (time.clock() - start))
