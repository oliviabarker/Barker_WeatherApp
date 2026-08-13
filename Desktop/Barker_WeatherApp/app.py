#Import libraries
from flask import Flask, jsonify, render_template, request
from weatherapp import getForecast as postForecast

#Initializing app
app = Flask(__name__)

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
        city = request.form.get('city')
        state = request.form.get('state')
        country = request.form.get('country')
###DONT FORGET TO HIDE API KEYS
        day1,day2,day3,day4,day5 = postForecast(city,state,country,"4a75802394effa810779155e1e869d13")

    
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
