from flask import Flask, request
import re
import socket
import json 

app = Flask(__name__)

@app.route('/')
def start():
    host = socket.gethostname()
    return "Host ID: {}".format(host)


@app.route('/indata', methods=['POST'])
def insert_data():
    if request.method == "POST":
        raw_data = request.get_data(as_text=True, cache=False)

        raw_data = json.loads(raw_data)

        # remove any whitespace and parse to dictionary
        sensor_data = raw_data['data'].replace(" ", "")  
        sensor_data = (dict(x.split(':') for x in sensor_data.split(',')))

        timestamp = raw_data['published_at']
        sensor_id = raw_data['coreid']

        # TODO - create and manage csv data


        
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5005, debug=True)
