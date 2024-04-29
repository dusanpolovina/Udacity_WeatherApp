# TO DO:
# 1. Have display_weather print the weather report.
# 2. Handle network errors by printing a friendly message.
#
# To test your code, open a terminal below and run:
#   python3 weather.py


import requests
import re

API_ROOT = 'https://api.openweathermap.org'
API_LOCQUERY = '/data/2.5/weather?q='
API_LOCID = '/data/2.5/weather?id='# + woeid
API_KEY = '&appid=d250b027ab4277cd65a5adfc4e5df0bf'
API_FC = '/data/2.5/forecast?id='

def fetch_location(query):
    return requests.get(API_ROOT + API_LOCQUERY + query + API_KEY).json()

def fetch_weather(woeid):
    return requests.get(API_ROOT + API_FC + str(woeid) +API_KEY).json()

def display_weather(weather):
    for entry in weather['list']:
        date = entry['dt_txt'].split(" ")[0]
        time = entry['dt_txt'].split(" ")[1]
        time2 = int(time[:2])
        if time2 == 0:
            timestr = '12am'
        elif int(time2) < 12 and time2 != '00':
            timestr = str(int(time2)) + 'am'        
        elif int(time2) == 12:
            timestr = '12pm'
        elif int(time2) > 12:
            timestr = str(int(time2) % 12) + 'pm'
        else:
            timestr = 'XX'
        temperature = (int((entry['main']['temp']) - 273.15)) * 9 / 5 + 32
        #print(f"Weather for {weather['name']}:")
        #print("Replace this message with the weather report!")
        print(f"On the date {date} and at {timestr}, the temperature will be {temperature} deg F")

def disambiguate_locations(locations):
    print("Ambiguous location! Did you mean:")
    for loc in locations['name']:
        print(f"\t* {loc}")

def weather_dialog():
    where = ''
    while not where:
        where = input("Where in the world are you? ")
    locations = fetch_location(where)
    if len(locations) == 0:
        print("I don't know where that is.")
    #elif len(locations) > 1:
    #    disambiguate_locations(locations)
    else:
        woeid = locations['id']
        display_weather(fetch_weather(woeid))


if __name__ == '__main__':
    while True:
        weather_dialog()
        break