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

start = time.clock()
runTime = time.time()
run("Python")

#
@memprof(threshold = 1)
def memeproof():
	RAM = ["python3", "-m", "memprof", "text.py"]
	subprocess.call(RAM)


memeproof()
