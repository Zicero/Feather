import time
from time import clock
import os

#python
start = time.clock()
print("Language detected: Python")
print("Runtime: %s" % (time.clock() - start));
print("Memory Usage (CPU): %s" % (time.CLOCK_PROCESS_CPUTIME_ID))
print("CPU TIME CLOCK: %s" % (time.CLOCK_THREAD_CPUTIME_ID))
# print("Memory Usage: %s" % (os.stat)

#javascript
print("Language detected: JavaScript")
print("Runtime: %s" % (time.clock() - start));
print("Memory Usage (CPU): %s" % (time.CLOCK_PROCESS_CPUTIME_ID))
print("CPU TIME CLOCK: %s" % (time.CLOCK_THREAD_CPUTIME_ID))

#C
print("Language detected: C")
print("Runtime: %s" % (time.clock() - start));
print("Memory Usage (CPU): %s" % (time.CLOCK_PROCESS_CPUTIME_ID))
print("CPU TIME CLOCK: %s" % (time.CLOCK_THREAD_CPUTIME_ID))