from string import *

#Detect either Javascript, C, or Python
def detect(snippet):
    js_key = ['var', 'let', '=>', 'console.log']
    c_key = ['#include', '*', '&', 'struct', 'typedef']
    py_key = ['def', 'from']
    x = False

    split_result = snippet.split()
    language = "Error: Unable to Detect Language"

    for w in split_result:
        print (w)
        for k in js_key:
            if k in w:
                language = 'JavaScript'
                return language
        if w in c_key:
            language = 'C'
            break
        elif w in py_key:
            language = 'Python'
            break

    return language
