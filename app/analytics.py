import time
from time import clock
import os
import timeit
import getpass
import datetime
import subprocess
from subprocess import call
from memprof import *

def analyze(language, input_file):
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
    memeproof(input_file)
    return analytics


@memprof(plot = True)
def memeproof(input_file):
    RAM = ["python3", "-m", "memprof", input_file]
    subprocess.call(RAM)


#analyze("Python")
#memeproof()
