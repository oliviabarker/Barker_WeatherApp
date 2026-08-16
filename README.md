# Barker's Weather App

A python application that takes a city, state, and country from the user and displays the current weather and a five day forecast for the location using Open Weather API.

## Appearance

## Key Features

* Current temperature and "feels like" temperature
* Minimum and maximum temperature, humidity, and weather condition for each forecast day
* Error handling and messaging for common input and server errors
* Timezone modification for user's location input when selecting weather data

## Pathway

* User inputs a location
* City input is validated
* Location input is converted to latitude and longitude with Open Weather's Geocoding API
* Latitude and longitude are used to get current and forecast weather data with Open Weather's Current Weather and Five Day Forecast APIs
* API repsonses are checked for errors
* Objects are constructed containing current and forecast weather data for each day
* Objects are passed to and HTML file to be rendered back to the user

## Technologies

* Python
* Flask
* Requests
* HTML and CSS
* Jinja2
* Open Weather API


