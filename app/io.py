from flask import Flask, request, json, jsonify

from language_detect import detect
from unix_compile import codeCompile
from analytics import analyze

app = Flask(__name__)

client = app.test_client()

extensions = {
    "C": "c",
    "C++": "cpp",
    "Java": "java",
    "JavaScript": "js",
    "Python": "py"
}

"""Receives code input/tags and parses data"""
@app.route('/', methods=['POST'])
def parse_request():

    #Receives and parses code
    data_receive = request.json
    code_string = data_receive['code']['text']

    print(code_string)
    code_string.strip()

    code_string = code_string.lstrip()
    print (code_string)

    #Prepping obj for return
    obj = {}
    obj['code'] = code_string

    #Detects code language
    lang = detect(code_string)
    print (lang)

    if lang == 'Error: Unable to Detect Language':
        obj['error'] = "UNABLE TO DETECT INPUT LANGUAGE."
        return (jsonify(obj))

    files = []
    files.append("text." + extensions[lang])

    #Preps code for compile
    test = open(files[0], "w")
    test.write(code_string)
    test.close()

    #Prepping for return
    obj['output'] = codeCompile(lang, files)
    obj['analytics'] = {}
    if lang == "Python":
        obj['analytics'] = analyze(lang, files[0])

    return (jsonify(obj))

if __name__ == "__main__":
    app.run(debug = True)
