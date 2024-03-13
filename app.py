#import flask library
from flask import Flask,render_template,request
import requests

#initialize flask
app = Flask(__name__)
#route your webpage
@app.route("/")
def visitors():

	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	# Increment the count
	visitors_count = visitors_count + 1

	# Overwrite the count
	counter_write_file = open("count.txt", "w")
	counter_write_file.write(str(visitors_count))
	counter_write_file.close()
	return render_template('index.html',count=visitors_count)
@app.route("/",methods=['POST'])

# Render HTML with count variable


#route your webpage
def weather_stats():
	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()
	latitude = request.form["la"]
	longitude = request.form["lo"]

	api = "https://weather-l6tl.onrender.com/api/getCurrentWeather/" + latitude + "/" + longitude
	response = requests.get(api)
	data = response.json()
	return render_template('index.html',weather=data,count=visitors_count)

if __name__ == "__main__":
	 app.run()




	#complete the code

#add code for executing flask