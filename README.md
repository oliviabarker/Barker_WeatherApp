# Barker's Weather App

A python application that takes a city, state, and country from the user and displays the current weather and a five day forecast for the location using Open Weather API.

## Appearance

Returned Weather Data:

<img width="1465" height="828" alt="Screenshot 2026-08-16 at 12 17 09 AM" src="https://github.com/user-attachments/assets/8f85bac3-996d-4b74-b36c-36391e7107e0" />

Sample Error Messages:

<img width="614" height="130" alt="Screenshot 2026-08-16 at 12 16 30 AM" src="https://github.com/user-attachments/assets/39f52e61-c58d-4b6d-aad9-1ab14c18a9c3" />

<img width="623" height="132" alt="Screenshot 2026-08-16 at 12 16 39 AM" src="https://github.com/user-attachments/assets/2002d5d5-7643-42a1-8511-3a4da39ae21f" />

<img width="616" height="127" alt="Screenshot 2026-08-16 at 12 17 31 AM" src="https://github.com/user-attachments/assets/81e7b9c3-1fba-4915-a101-4a5f4c87e8eb" />

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


