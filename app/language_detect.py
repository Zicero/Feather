from string import *

#Detect either Javascript, C, or Python
def detect(snippet):
    js_key = ['var', 'let', '=>']
    c_key = ['#include', '*', '&', 'struct', 'typedef']
    py_key = ['def', 'from']
    x = False

    split_result = snippet.split()
    language = "Error: Unable to Detect Language"

    for w in split_result:
        if w in js_key:
            language = 'Javascript'
            break
        elif w in c_key:
            language = 'C'
            break
        elif w in py_key:
            language = 'Python'
            break

    return language
