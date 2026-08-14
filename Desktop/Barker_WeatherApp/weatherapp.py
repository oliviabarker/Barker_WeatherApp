#Import libraries
import requests, json
from datetime import datetime

api_key = "4a75802394effa810779155e1e869d13"

#Constructor for object of weatherDay to store weather information for independent days - both current and forecasted
class weatherDay:
    def __init__(this, city, weekday, date, currtemp, feelslike, tempmin, tempmax, humidity, condition, icon): #add an icon
        this.city = city
        this.weekday = weekday
        this.date = date
        this.currtemp = currtemp
        this.feelslike = feelslike
        this.tempmin = tempmin
        this.tempmax = tempmax
        this.humidity = humidity
        this.condition = condition
        this.icon = icon


#Request city, state, and country from user



#Retrieve location latitudinal and longitudinal data
def getLatLong(city, state, country, api_key): 
    data = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&&appid={api_key}').json()
    # check for errors
    if not data:
        return None, None
    data = data[0]
    lat = data['lat']
    long = data['lon']
    #print (data, lat, long)
    return lat, long


#getLatLong('Frankfort', 'KY', 'US', api_key)

#Request current weather with lat and long
##def getCurrentWeather(city, state, country, api_key):
##    lat, long = getLatLong(city, state, country, api_key)
##    data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}&units={"imperial"}').json()
####CHECK FOR CODE TO MAKE SURE NO ERRORS
##    #converting unix object
##    date = datetime.fromtimestamp(data['dt'])
##    curr_weather = weatherDay(date.strftime("%A"), date.strftime("%m/%d"), data['main']['temp'], \
##                              data['main']['feels_like'], data['main']['temp_min'], data['main']['temp_max'], \
##                              data['main']['humidity'], data['weather'][0]['main'], data['weather'][0]['icon'])
##    #print()
##    return curr_weather


##WILL THE CODE ALWAYS BE THERE IF I ONLY ADD 11 OCLOCK TIMES???
def getForecast(city, state, country, api_key):
    lat, long = getLatLong(city, state, country, api_key)
    data = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&appid={api_key}&units={"imperial"}').json()
    code = int(data['cod'])
    day1 = None
    day2 = None
    day3 = None
    day4 = None
    day5 = None
    forecastDays=[]
    if code==200:
        for item in data['list']:
            date = datetime.fromtimestamp(item['dt'])
            if date.hour == 11:
                weather = weatherDay(data['city']['name'],
                                     date.strftime("%A"),
                                     date.strftime("%m/%d"),
                                     int(item['main']['temp']),
                                     int(item['main']['feels_like']),
                                     int(item['main']['temp_min']),
                                     int(item['main']['temp_max']),
                                     item['main']['humidity'],
                                     item['weather'][0]['main'],
                                     item['weather'][0]['icon'])
                forecastDays.append(weather)
        day1 = forecastDays[0]
        day2 = forecastDays[1]
        day3 = forecastDays[2]
        day4 = forecastDays[3]
        day5 = forecastDays[4]
    return day1, day2, day3, day4, day5, code


def main():
    #getCurrentWeather('Frankfort', 'KY', 'US', api_key)
    #forecastDays = getForecast('Frankfort', 'KY', 'US', api_key)
    #print(forecastDays[0].weekday,forecastDays[1].weekday,forecastDays[2].weekday,forecastDays[3].weekday,forecastDays[4].weekday)
    day1, day2, day3, day4, day5, code= getForecast(city, state, country, api_key)
    return day1, day2, day3, day4, day5, code



##main()
