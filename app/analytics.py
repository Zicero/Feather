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
    analytics = {}
    start = time.clock()
    runTime = time.time()
    analytics["Language Detected"] = language
    data = str(getpass.getuser())
    analytics["User"] = data
    data = str(time.asctime(time.localtime(time.time())))
    analytics["Boot Time"] = data
    data = str(time.clock() - start)
    analytics["Memory (CPU)"] = data
    data = str((time.time() - runTime) * 1000)
    analytics["Runtime"] = data
    memeproof()
    return analytics


@memprof(threshold = 1)
def memeproof():
    RAM = ["python3", "-m", "memprof", "-p", "text.py"]
    subprocess.call(RAM)


#analyze("Python")
#memeproof()
