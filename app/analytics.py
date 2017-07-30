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
    f.write("Language detected: " + language + "\n")
    data = str(getpass.getuser())
    f.write("User: " + data + "\n")
    data = str(time.asctime(time.localtime(time.time())))
    f.write("Boot Time: " + data + "\n")
    data = str(time.clock() - start)
    f.write("Memory (CPU): " + data + "\n")
    data = str((time.time() - runTime) * 1000)
    f.write("Runtime: " + data + "\n")
    f.close()
    with open(analytics_file, "r") as f:
        return f.read()


@memprof(threshold = 1)
def memeproof():
    RAM = ["python3", "-m", "memprof", "text.py"]
    subprocess.call(RAM)


analytics_file = "analytics_file.txt"

analyze("Python")
memeproof()
