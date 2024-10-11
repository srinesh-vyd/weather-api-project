import requests
from dotenv import load_dotenv
import os
from pprint import pprint
load_dotenv()

def get_weather_data():
    print("\n******* Current Weather Data *********\n")
    city=input("Enter the city name:")
    try:
        request_url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("weather_api_key")}&units=metric"
        weather_data= requests.get(request_url).json()
        print(f"\nThe current Temperature of {weather_data["name"]} is {weather_data["main"]["temp"]} Celcius")
        print(f"\nThe Temperature feels like {weather_data["main"]["feels_like"]} Celcius and {weather_data["weather"][0]['description']}\n")
    except KeyError as error:
        pprint(weather_data["message"])
    except Exception as e:
        print(e)

if __name__=="__main__":
    get_weather_data()