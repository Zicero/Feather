from string import *

#Detect either Javascript, C, or Python
def detect(snippet):
    js_key = ['var', 'let', '=>']
    c_key = ['#include', '*', '&', 'struct', 'typedef']
    py_key = ['def', 'from']
    x = False

    split_result = snippet.split()
    for w in split_result:
        if w in js_key:
            language = 'Javascript'
            x = True
        elif w in c_key:
            language = 'C'
            x = True
        elif w in py_key:
            language = 'Python'
            x = True
        else :
            if (x == False):
                language = 'Error: Unable To Detect Language'

    return language
