import time
from time import clock
import os
import timeit
import getpass
import datetime
import subprocess
from subprocess import call
# import cProfile
# import re

def run(language):
	print("Language detected: " + language)
	print("User: %s" % (getpass.getuser()))
	print("Boot Time: %s" % (time.asctime(time.localtime(time.time()))))
	print("Memory (CPU): %s" % ((time.clock() - start)))
	print("Runtime: %s" % ((time.time() - runTime) * 1000))
	print("RAM Usage: %s" % str(os.popen('free -t -m').read()))

start = time.clock()
runTime = time.time()
run("Python")


RAMCOM = ["python", "-m", "memory_profiler", "text.py"]
print("RAM Usage: %s" % (subprocess.call(RAMCOM, shell=True)))

# #python
# print("Language detected: Python")
# print("User: %s" % (getpass.getuser()))
# print("Boot Time: %s" % (time.asctime(time.localtime(time.time()))))
# print("Memory (CPU): %s" % ((time.clock() - start)))
# print("Runtime: %s" % ((time.time() - runTime) * 1000))
# print("RAM Usage: %s" % str(os.popen('free -t -m').read()))

# # print("Status: %s" % cProfile.run('re.compile()')

# #javascript
# print("Language detected: JavaScript")
# print("User: %s" % (getpass.getuser()))
# print("Boot Time: %s" % (time.asctime(time.localtime(time.time()))))
# print("Memory (CPU): %s" % (time.clock() - start))
# print("Runtime: %s" % ((time.time() - runTime) * 1000))
# print("RAM Usage: %s" % str(os.popen('free -t -m').read()))

# #C
# print("Language detected: C")
# print("User: %s" % (getpass.getuser()))
# print("Boot Time: %s" % (time.asctime(time.localtime(time.time()))))
# print("Memory (CPU): %s" % (time.clock() - start))
# print("Runtime: %s" % ((time.time() - runTime) * 1000))
# print("RAM Usage: %s" % str(os.popen('free -t -m').read()))
