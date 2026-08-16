#Import libraries
import requests
from datetime import datetime, timezone, timedelta


#Constructor for weatherDay object to hold forecast data for each day
class weatherDay:
    def __init__(this, city, weekday, date, currtemp, feelslike, tempmin, tempmax, humidity, condition, icon):
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


#Retrieve location's latitude and longitude from user's inputs
def getLatLong(city, state, country, api_key): 
    #Try to fetch latitude and longitude
    try:
        response = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&appid={api_key}', timeout=10)
        data = response.json()

    #Throw exception for errors and return HTTP error
    except requests.exceptions.ConnectionError:
        return None, None, "network"
    except requests.exceptions.Timeout:
        return None, None, "timeout"
    if response.status_code != 200:
        return None, None, response.status_code
    if not data:
        return None, None, 404

    #Return latitude, longitude, and successful status code 
    data = data[0]
    lat = data['lat']
    long = data['lon']
    return lat, long, 200


#Retrieve current weather and forecast data
def getForecast(city, state, country, api_key):
    #Get latitude and longitude for user's inputs
    lat, long, code = getLatLong(city, state, country, api_key)

    #Return for unsuccessful status codes
    if code != 200:
        return None, code

    #Try to fetch current weather and forecast data
    try:
        response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&appid={api_key}&units={"imperial"}', timeout=10)
        response_curr = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}&units={"imperial"}', timeout=10)

    #Throw exceptions for errors and return HTTP error codes
    except requests.exceptions.ConnectionError:
        return None, "network"
    except requests.exceptions.Timeout:
        return None, "timeout"
    if response.status_code != 200:
        return None, response.status_code
    data = response.json()
    if response_curr.status_code != 200:
        return None, response_curr.status_code
    data_curr = response_curr.json()

    code = int(data['cod'])

    #Make a list to contain weatherDay objects for each forecast day
    forecastDays=[]

    #If successful HTTP code, create one object for each forecast day and add it to the list
    if code==200:
        dates=[]

        #Modify the time to match the timezone of the location of the user's input
        today = True
        for item in data['list']:
            utc_date = datetime.fromtimestamp(item['dt'], tz=timezone.utc)
            date = utc_date + timedelta(seconds=data['city']['timezone'])
            date_key = date.strftime("%Y-%m-%d")

            #Verify only one weather object is added each day
            if date_key not in dates:
                dates.append(date_key)

                #Add temperatures for each time in a day to retrieve the minimum and maximum temperature for the entire day later
                day_temps = [item['main']['temp']
                             for item in data['list']
                             if (datetime.fromtimestamp(item['dt'], tz=timezone.utc)+timedelta(seconds=data['city']['timezone'])).strftime('%Y-%m-%d')==date_key]

                #Create the weather object and add it to the list of forecast days
                if today:
                    weather = weatherDay(city.capitalize(),
                                         date.strftime("%A"),
                                         date.strftime("%m/%d"),
                                         int(data_curr['main']['temp']),
                                         int(data_curr['main']['feels_like']),
                                         int(min(day_temps)),
                                         int(max(day_temps)),
                                         data_curr['main']['humidity'],
                                         data_curr['weather'][0]['main'],
                                         data_curr['weather'][0]['icon'])
                else:
                    weather = weatherDay(city.capitalize(),
                                         date.strftime("%A"),
                                         date.strftime("%m/%d"),
                                         int(data_curr['main']['temp']),
                                         int(data_curr['main']['feels_like']),
                                         int(min(day_temps)),
                                         int(max(day_temps)),
                                         item['main']['humidity'],
                                         item['weather'][0]['main'],
                                         item['weather'][0]['icon'])
                today = False
                    
                forecastDays.append(weather)

    #Return the list of forecast days and the status code
    return forecastDays, code

