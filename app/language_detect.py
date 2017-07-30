from string import *

# Detect either Javascript, C, or Python

def detect(snippet):
	js_key = ['var', 'let', '=>', '']
	c_key = ['#include', '*', '&']
	py_key = ['def', 'from']

	split_result = snippet.split()
	for w in split_result:
		if w in js_key:
			language = 'Javascript'

		elif w in c_key:
			language = 'C'

		elif w in py_key:
			language = 'Python'

		else:
			language = 'Error: Unable To Detect Language'

	print(language)
