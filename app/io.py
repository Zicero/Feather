from flask import Flask, request, json, jsonify

from language_detect import detect
from unix_compile import codeCompile

app = Flask(__name__)

client = app.test_client()

"""Receives code input/tags and parses data"""
@app.route('/', methods=['POST'])
def parse_request():

    data_receive = request.json
    code_string = data_receive['code']['text']
    code_string.strip()

    code_string = code_string.lstrip()
    print (code_string)

    lang = detect(code_string)
    print (lang)

    test = open("text.py", "w")
    test.write(code_string)
    test.close()

    obj = {}
    codeCompile(lang, ["text.py"])
    obj['code'] = code_string

    with open("compile_file.txt") as f:
        send = f.read()
        obj['output'] = send

    return (jsonify(obj))






"""Sends output/collected data to ext as json"""
# @app.route('/')
# def output_send():
#     data_send = get_data()
#     return jsonify(data_send)

if __name__ == "__main__":
    app.run(debug = True)
