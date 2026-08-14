#Import libraries
from flask import Flask, jsonify, render_template, request, flash
from weatherapp import getForecast as postForecast

#Initializing app
app = Flask(__name__)
app.secret_key = "secretkey"

#Setting home url and adding post method
@app.route('/', methods = ['GET','POST'])

##def post():
##    forecastDays=postForecast()

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
        day1,day2,day3,day4,day5,code = postForecast(city,state,country,"4a75802394effa810779155e1e869d13")

        print("code:", code)

        if code == 429:
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


##def postWeather():
##    forecastDays = postForecast()
##    return jsonify({'day1':day1.__dict__, 'day2':day2.__dict__, 'day3':day3.__dict__, 'day4':day4.__dict__, 'day5':day5.__dict__,})

if __name__ == "__main__":
    app.run()


###ADD A DEFAULT DISPLAY FOR LEXINGTON KENTUCKY SO THE WORDS DONT DISPLAY BY THEMSELVES AT FIRST
