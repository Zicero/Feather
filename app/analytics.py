import time
from time import clock


#python
start = time.clock()
print("Language detected: Python")
print("Runtime: %s" % (time.clock() - start));

#javascript
print("Language detected: JavaScript")
print("Runtime: %s" % (time.clock() - start));

#C
print("Language detected: C")
print("Runtime: %s" % (time.clock() - start));