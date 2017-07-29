from flask import request
from flash import jsonify

{Content-Type: application/json}

"""Receives code input/tags and parses data"""
@app.route('/', methods=['GET', 'POST'])
def parse_request():
    data_receive = request.json

"""Sends output/collected data to ext as json"""
@app.route('/')
def send_json:
    data_send = get_data()
    return jsonify(data_send)
