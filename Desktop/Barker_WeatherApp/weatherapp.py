#Import libraries
from flask import Flask
import requests, json


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
def getCurrentWeather(city, state, country, api_key):
    lat, long = getLatLong(city, state, country, api_key)
    data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}&units={"imperial"}').json()
    #print(data)
    return currdata

def getForecast(city, state, country, api_key):
    lat, long = getLatLong(city, state, country, api_key)
    data = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&appid={api_key}&units={"imperial"}').json()
    print(data)

    
    

#Parse JSON object


#Request forecast with lat and long
    ##call the method for lat/long retrieval


def main():
    #getCurrentWeather('Frankfort', 'KY', 'US', api_key)
    getForecast('Frankfort', 'KY', 'US', api_key)



main()
