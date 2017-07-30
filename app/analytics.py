import time
from time import clock
import os
import timeit
import getpass
import datetime

start = time.clock()
runTime = time.time()

#python
print("Language detected: Python")
print("User: %s" % (getpass.getuser()))
print("Date and Time accessed: %s" % (time.asctime(time.localtime(time.time()))))
print("Memory (CPU): %s" % ((time.clock() - start)))
print("Runtime: %s" % (time.time() - runTime))
# print("Status: " % )

#javascript
print("Language detected: JavaScript")
print("User: %s" % (getpass.getuser()))
print("Date and Time accessed: %s" % (time.asctime(time.localtime(time.time()))))
print("Memory (CPU): %s" % (time.clock() - start))
print("Runtime: %s" % (time.time() - runTime))

#C
print("Language detected: C")
print("User: %s" % (getpass.getuser()))
print("Date and Time accessed: %s" % (time.asctime(time.localtime(time.time()))))
print("Memory (CPU): %s" % (time.clock() - start))
print("Runtime: %s" % (time.time() - runTime))
