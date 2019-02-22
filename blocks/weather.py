#!/usr/bin/env python
import urllib.request, json, sys
URL = "https://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&appid={}"
KEY = None
country_code = None
city_name = None

weather_icons = {
    '01d':'🌞','01n':'🌞',
    '02d':'🌤️','02n':'🌤️',
    '03d':'⛅','03n':'⛅',
    '04d':'☁️','04n':'☁️',
    '09d':'🌦️','09n':'🌦️',
    '10d':'🌧️','10n':'🌧️',
    '11d':'🌩️','11n':'🌩️',
    '13d':'🌨️','13n':'🌨️',
    '50d':'❄️','50n':'❄️',
}

#   '50d':'🌫️','50n':'🌫️',

try:
    KEY = sys.argv[3]
    country_code = sys.argv[2]
    city_name = sys.argv[1]
except Exception as e:
    print("No API Key")
    sys.exit(1)

try:
    with urllib.request.urlopen(URL.format(city_name,country_code,KEY)) as url:
        data = json.loads(url.read().decode())
        city = data['name']
        temp = data['main']['temp']
        min = data['main']['temp_min']
        max = data['main']['temp_max']
        icon = weather_icons.get(data['weather'][0]['icon'], '')
        print('{} <span foreground="#91E78B">{}</span><sup>°</sup>C'.format(icon,temp))
except IOError as ioe:
    print('Invalid API Key')


