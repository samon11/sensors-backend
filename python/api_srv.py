from flask import Flask, request
from database import Airdata, session
import re
from Dict import parse

app = Flask(__name__)

@app.route('/')
def start():
    return "hiiiii"

@app.route('/indata', methods=['POST'])
def insert_data():
    if request.method == "POST":
        data = request.get_data(as_text=True, cache=False)
        
        parsed_data = parse(data)
	
        # insert parsed data into database
        new_insert = Airdata(light=parsed_data['light'],
                            temperature=parsed_data['temp'],
                            temp_barom=parsed_data['temp_barom'],
                            pressure=parsed_data['pressure'],
                            humidity=parsed_data['humidity']
                            )
        try:
                session.add(new_insert)
                session.commit()
                return "SUCCESS"
        except:
                return "ERROR DATA NOT COMMITED"

        
        


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5005, debug=True)
