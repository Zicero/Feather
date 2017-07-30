from flask import Flask, request, json, jsonify

from language_detect import detect
from unix_compile import codeCompile

app = Flask(__name__)

client = app.test_client()

"""Receives code input/tags and parses data"""
@app.route('/', methods=['POST'])
def parse_request():

    #Receives and parses code
    data_receive = request.json
    code_string = data_receive['code']['text']
    code_string.strip()

    code_string = code_string.lstrip()
    print (code_string)

    #Detects code language
    lang = detect(code_string)
    print (lang)

    #Preps code for compile
    test = open("text.py", "w")
    test.write(code_string)
    test.close()

    #Obj to be shipped
    obj = {}
    obj['code'] = code_string
    obj['output'] = codeCompile(lang, ["text.py"])
    obj['analytics'] = analyze(lang)

    return (jsonify(obj))

if __name__ == "__main__":
    app.run(debug = True)
