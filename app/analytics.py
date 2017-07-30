import time
from time import clock
import os
import timeit
import getpass
import datetime
# import cProfile
# import re

start = time.clock()
runTime = time.time()

#python
print("Language detected: Python")
print("User: %s" % (getpass.getuser()))
print("Boot Time: %s" % (time.asctime(time.localtime(time.time()))))
print("Memory (CPU): %s" % ((time.clock() - start)))
print("Runtime: %s" % (time.time() - runTime))
print("RAM Usage: %s" % str(os.popen('free -t -m').readlines()))
# print("Status: %s" % cProfile.run('re.compile()')

#javascript
print("Language detected: JavaScript")
print("User: %s" % (getpass.getuser()))
print("Boot Time: %s" % (time.asctime(time.localtime(time.time()))))
print("Memory (CPU): %s" % (time.clock() - start))
print("Runtime: %s" % (time.time() - runTime))
print("RAM Usage: %s" % str(os.popen('free -t -m').readlines()))

#C
print("Language detected: C")
print("User: %s" % (getpass.getuser()))
print("Boot Time: %s" % (time.asctime(time.localtime(time.time()))))
print("Memory (CPU): %s" % (time.clock() - start))
print("Runtime: %s" % (time.time() - runTime))
print("RAM Usage: %s" % str(os.popen('free -t -m').readlines()))
