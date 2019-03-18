from flask import Flask, request
from database import session, Users, Airdata
import socket
import json
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def start():
    host = socket.gethostname()
    return "Host ID: {}".format(host)


def insert_data(request):
    """Parse request json data and insert into db"""
    raw_data = request.get_data(as_text=True, cache=False)
    raw_data = json.loads(raw_data)

    # remove any whitespace and parse to dictionary
    sensor_data = raw_data['data'].replace(" ", "")
    sensor_data = (dict(x.split(':') for x in sensor_data.split(',')))
    
    # convert to floats and remove chars after '_'
    sensor_data = {k:float(v[:v.index('_')]) for k, v in sensor_data.items() if k != "minSinceStart"}
    
    print(sensor_data)

    # this timestamp is the time at which the sensor
    # pushed the data
    timestamp = raw_data['published_at']

    particle_id = raw_data['coreid']

    # get the sensor id from the users table if it exists
    sensor_owner = session.query(Users).filter_by(particle_str=particle_id).first()

    data_insert = Airdata(
            device_time=timestamp,
            temperature_C=sensor_data["Temp"],
            pressure_hPa=sensor_data["Press"],
            humidity_perc=sensor_data["Hum"],
            user=sensor_owner
    )

    session.add(data_insert)
    session.commit()


@app.route('/indata', methods=['POST'])
def indata():
    if request.method == "POST":
        insert_data(request)
        return "200-OK"


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5005, debug=True)
