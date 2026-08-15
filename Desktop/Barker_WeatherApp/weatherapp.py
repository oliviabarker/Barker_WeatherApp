#Import libraries
import requests, json
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENWEATHER_APIKEY")

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


#Retrieve location latitudinal and longitudinal data
def getLatLong(city, state, country, api_key): 
    try:
        response = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&appid={api_key}', timeout=10)
        data = response.json()
    except requests.exceptions.ConnectionError:
        return None, None, "network"
    except requests.exceptions.Timeout:
        return None, None, "timeout"
    if response.status_code != 200:
        return None, None, response.status_code
    if not data:
        return None, None, 404
    data = data[0]
    lat = data['lat']
    long = data['lon']
    return lat, long, 200



##WILL THE CODE ALWAYS BE THERE IF I ONLY ADD 11 OCLOCK TIMES???
def getForecast(city, state, country, api_key):
    lat, long, code = getLatLong(city, state, country, api_key)
    if code != 200:
        return None, None, None, None, None, code
    try:
        data = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&appid={api_key}&units={"imperial"}&limit=1', timeout=10).json()
    except requests.exceptions.ConnectionError:
        return None, None, None, None, None, "network"
    except requests.exceptions.Timeout:
        return None, None, None, None, None, "timeout"
    
    code = int(data['cod'])
    day1 = None
    day2 = None
    day3 = None
    day4 = None
    day5 = None
    forecastDays=[]
    if code==200:
        dates=[]
        for item in data['list']:
            date = datetime.fromtimestamp(item['dt'])
            date_key = date.strftime("%Y-%m-%d")
            if date_key not in dates:
                dates.append(date_key)
                weather = weatherDay(city.capitalize(),
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
    return getForecast(city, state, country, api_key)

