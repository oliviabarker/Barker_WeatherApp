#Import libraries
import os
from flask import Flask, jsonify, render_template, request, flash
from weatherapp import getForecast as postForecast
from dotenv import load_dotenv

#Initializing app and retrieving app key
app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv("APP_SECRET_KEY")

#Defining methods
@app.route('/', methods = ['GET','POST'])


def temp():
    forecastDays = None
    #Recieving and cleaning inputs
    if request.method == 'POST':
        city = request.form.get('city', '').strip()
        state = request.form.get('state', '').strip()
        country = request.form.get('country', '').strip()

        #Verifying city name was entered
        if not city:
            flash('Please enter a valid city name.')
            return render_template('base.html',
                                   forecastDays = forecastDays)

        #Recieving list of objects containing weather forecast data and HTTP status code
        forecastDays,code = postForecast(city,state,country, os.getenv("OPENWEATHER_APIKEY"))

        #Checking for errors and flashing messages for expected errors
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

    #Rendering HTML file and passing it forecast data         
    return render_template('base.html',
                            forecastDays=forecastDays)

#Running the application
if __name__ == "__main__":
    app.run()
