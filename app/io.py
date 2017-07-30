from flask import Flask, request, json, jsonify

app = Flask(__name__)

client = app.test_client()

"""Receives code input/tags and parses data"""
@app.route('/', methods=['POST'])
def parse_request():
    data_receive = request.json
    code_string = data_receive['code']['text']
    code_string.strip()
    print (code_string)
    return 'fuck off'

"""Sends output/collected data to ext as json"""
@app.route('/')
def output_send():
    data_send = get_data()
    return jsonify(data_send)

if __name__ == "__main__":
    app.run(debug = True)
