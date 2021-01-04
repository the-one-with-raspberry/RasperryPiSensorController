import sht21
from flask import Flask, jsonify, render_template
import datetime
app = Flask(__name__, template_folder="templates")

sht21 = sht21.SHT21(1)

@app.route('/getTemperature/json')
def getJsonTemp():

    temp = sht21.read_temperature()
    time = datetime.datetime.now() 

    response = {
        "temperature": temp,
        "timeRegistered": time
        }

    return jsonify(response)

@app.route('/getHumidity')
def getHum():

    humidity = sht21.read_humidity()

    return "The humidity is: " + str(humidity)

@app.route('/getTemperature')
def getTemp():
	
	temp = sht21.read_temperature()
	
	return "The temperature is: " + str(temp)

@app.route('/getHumidity/json')
def getJsonHum():
	
	hum = sht21.read_humidity()
	time = datetime.datetime.now()
	
	respStructure = {
	  "humidity": hum,
	  "timeRegistered": time
	}
	
	return jsonify(respStructure)

@app.route('/search')
def redirect():
	temp = sht21.read_temperature()

	return render_template('search.html', temperature=temp)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
