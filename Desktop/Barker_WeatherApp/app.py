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

        day1,day2,day3,day4,day5 = postForecast(city,state,country,"4a75802394effa810779155e1e869d13")

    
    return render_template('base.html',
                           day1 = day1,
                           day2 = day2,
                           day3 = day3,
                           day4 = day4,
                           day5 = day5)
##                           icon1= day1.icon,
##                           weekday1= day1.weekday,
##                           date1=day1.date,
##                           currtemp1=day1.currtemp,
##                           feelslike1=day1.feelslike,
##                           tempmin1=day1.tempmin,
##                           tempmax1=day1.tempmax,
##                           humidity1=day1.humidity,
##                           condition1=day1.condition,
##                           icon2= day2.icon,
##                           weekday2= day2.weekday,
##                           date2=day2.date,
##                           currtemp2=day2.currtemp,
##                           feelslike2=day2.feelslike,
##                           tempmin2=day2.tempmin,
##                           tempmax2=day2.tempmax,
##                           humidity2=day2.humidity,
##                           condition2=day2.condition,
##                           icon3= day3.icon,
##                           weekday3= day3.weekday,
##                           date3=day3.date,
##                           currtemp3=day3.currtemp,
##                           feelslike3=day3.feelslike,
##                           tempmin3=day3.tempmin,
##                           tempmax3=day3.tempmax,
##                           humidity3=day3.humidity,
##                           condition3=day3.condition,
##                           icon4= day4.icon,
##                           weekday4= day4.weekday,
##                           date4=day4.date,
##                           currtemp4=day4.currtemp,
##                           feelslike4=day4.feelslike,
##                           tempmin4=day4.tempmin,
##                           tempmax4=day4.tempmax,
##                           humidity4=day4.humidity,
##                           condition4=day4.condition,
##                           icon5= day5.icon,
##                           weekday5= day5.weekday,
##                           date5=day5.date,
##                           currtemp5=day5.currtemp,
##                           feelslike5=day5.feelslike,
##                           tempmin5=day5.tempmin,
##                           tempmax5=day5.tempmax,
##                           humidity5=day5.humidity,
##                           condition5=day5.condition)

##def postWeather():
##    forecastDays = postForecast()
##    return jsonify({'day1':day1.__dict__, 'day2':day2.__dict__, 'day3':day3.__dict__, 'day4':day4.__dict__, 'day5':day5.__dict__,})

if __name__ == "__main__":
    app.run()
