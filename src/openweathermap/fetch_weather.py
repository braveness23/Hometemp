import requests
import sqlite3
from datetime import datetime
import os

# Replace with your actual API key
API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
if not API_KEY:
    raise ValueError("No API key found. Please set the OPENWEATHERMAP_API_KEY environment variable.")

# Replace with your location
CITY_NAME = 'Cincinnati'

# Base URL for OpenWeatherMap API
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def fetch_weather(api_key, city_name):
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

def parse_weather_data(data):
    try:
        main = data['main']
        wind = data['wind']
        weather_desc = data['weather'][0]['description']

        weather_info = {
            'temperature': main['temp'],
            'feels_like': main['feels_like'],
            'humidity': main['humidity'],
            'pressure': main['pressure'],
            'wind_speed': wind.get('speed', 0),
            'wind_deg': wind.get('deg', 0),
            'weather_description': weather_desc
        }
        return weather_info
    except KeyError as e:
        print("Key error: {e}")
        return None

def insert_weather_data(db_path, weather_info):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO weather_data (
            temperature, feels_like, humidity, pressure,
            wind_speed, wind_deg, weather_description
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        weather_info['temperature'],
        weather_info['feels_like'],
        weather_info['humidity'],
        weather_info['pressure'],
        weather_info['wind_speed'],
        weather_info['wind_deg'],
        weather_info['weather_description']
    ))
    conn.commit()
    conn.close()

def main():
    api_key = API_KEY
    city_name = CITY_NAME
    db_path = '../../database/hometemp.db'

    weather_data = fetch_weather(api_key, city_name)
    if weather_data['cod'] == 200:
        weather_info = parse_weather_data(weather_data)
        if weather_info:
            print(weather_data)
            insert_weather_data(db_path, weather_info)
            print("Weather data for {city_name} inserted into database.")
        else:
            print("Failed to parse weather data.")
    else:
        print("Error fetching weather data: {weather_data.get('message', '')}")

if __name__ == '__main__':
    main()
