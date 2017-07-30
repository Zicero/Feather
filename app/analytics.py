import time
from time import clock
import os
import timeit
import getpass
import datetime
import subprocess
from subprocess import call
from memprof import *
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
memeproof()

@memprof(threshold = 1024)
def memeproof():
	ramcom = ["python", "-m", "memprof", "text.py"]
	print("RAM Usage: %s" % (subprocess.call(ramcom, shell=True)))
# memory_profiler

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
