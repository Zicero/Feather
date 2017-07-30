import time
from time import clock
import os
import timeit
import getpass
import datetime
import subprocess
from subprocess import call
from memprof import *

def analyze(language):
	f = open(analytics_file, "w")
	start = time.clock()
	runTime = time.time()
    f.write("Language detected: " + language)
    f.write("User: %s" % (getpass.getuser()))
    f.wirte("Boot Time: %s" % (time.asctime(time.localtime(time.time()))))
    f.write("Memory (CPU): %s" % ((time.clock() - start)))
    f.write("Runtime: %s" % ((time.time() - runTime) * 1000))


@memprof(threshold = 1)
def memeproof():
	RAM = ["python3", "-m", "memprof", "text.py"]
	subprocess.call(RAM)


analytics_file = "analytics_file.txt"	

analyze("Python")
memeproof()
