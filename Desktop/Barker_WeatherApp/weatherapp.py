#Import libraries
import requests, json
from datetime import datetime

api_key = "4a75802394effa810779155e1e869d13"

#Constructor for object of weatherDay to store weather information for independent days - both current and forecasted
class weatherDay:
    def __init__(this, weekday, date, currtemp, feelslike, tempmin, tempmax, humidity, condition, icon): #add an icon
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

def getForecast(city, state, country, api_key):
    lat, long = getLatLong(city, state, country, api_key)
    data = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&appid={api_key}&units={"imperial"}').json()
    forecastDays=[]
    for item in data['list']:
        date = datetime.fromtimestamp(item['dt'])
        weather = weatherDay(date.strftime("%A"), date.strftime("%m/%d"), item['main']['temp'], \
                            item['main']['feels_like'], item['main']['temp_min'], item['main']['temp_max'], \
                            item['main']['humidity'], item['weather'][0]['main'], item['weather'][0]['icon'])
        forecastDays.append(weather)
    day1= forecastDays[0]
    day2= forecastDays[3]
    day3= forecastDays[6]
    day4= forecastDays[9]
    day5= forecastDays[12]
    print(day1.weekday, day1.date, day1.currtemp, day1.feelslike, day1.tempmin, day1.tempmax, day1.humidity, day1.condition, day1.icon,\
          day2.weekday, day2.date, day2.currtemp, day2.feelslike, day2.tempmin, day2.tempmax, day2.humidity, day2.condition, day2.icon,\
          day3.weekday, day3.date, day3.currtemp, day3.feelslike, day3.tempmin, day3.tempmax, day3.humidity, day3.condition, day3.icon,\
          day4.weekday, day4.date, day4.currtemp, day4.feelslike, day4.tempmin, day4.tempmax, day4.humidity, day4.condition, day4.icon,\
          day5.weekday, day5.date, day5.currtemp, day5.feelslike, day5.tempmin, day5.tempmax, day5.humidity, day5.condition, day5.icon,)
    #return
    

#Parse JSON object


#Request forecast with lat and long
    ##call the method for lat/long retrieval


def main():
    #getCurrentWeather('Frankfort', 'KY', 'US', api_key)
    getForecast('Frankfort', 'KY', 'US', api_key)



main()
