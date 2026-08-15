#Import libraries
from flask import Flask, jsonify, render_template, request, flash
from weatherapp import getForecast as postForecast
import os
from dotenv import load_dotenv

#Initializing app
app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv("APP_SECRET_KEY")

#Setting home url and adding post method
@app.route('/', methods = ['GET','POST'])

##NOT CURRENT TEMP ON FUTRUE

def temp():
    day1 = None
    day2 = None
    day3 = None
    day4 = None
    day5 = None
    if request.method == 'POST':
        city = request.form.get('city', '').strip()
        state = request.form.get('state', '').strip()
        country = request.form.get('country', '').strip()
###DONT FORGET TO HIDE API KEYS/SECRET KEY

        if not city:
            flash('Please enter a valid city name.')
            return render_template('base.html',
                                   day1 = day1,
                                   day2 = day2,
                                   day3 = day3,
                                   day4 = day4,
                                   day5 = day5)
        day1,day2,day3,day4,day5,code = postForecast(city,state,country, os.getenv("OPENWEATHER_APIKEY"))

        print("code:", code)

        if code == "network":
            flash('Connection error. Please check your service and try again.')
            
        elif code == "timeout":
            flash('The server took too long to respond. Please try again later.')
            
        elif code == 429:
            flash('Too many requests. Please try again later.')

        elif code == 404:
            flash('City not found.')

        elif code == 400:
            flash('Please enter a valid city name.')

        elif 500 <= code <= 504:
            flash('There was an issue with the server. Please try again later.')

        elif code != 200:
            flash('Something went wrong. Please try again later.')
                  
    return render_template('base.html',
                            day1 = day1,
                            day2 = day2,
                            day3 = day3,
                            day4 = day4,
                            day5 = day5)



if __name__ == "__main__":
    app.run()
