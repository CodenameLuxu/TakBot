from pprint import pprint
import requests
from src.TakBot import TakConstants
from src.SecretKey import SecretKey


class WeatherServiceAPI:

    def __init__(self):
        connectionstr = 'http://api.openweathermap.org/data/2.5/weather?q=Bangkok&APPID=' + SecretKey.WeatherAPIKey
        self.response =requests.get(connectionstr).json()

    def refresh(self):
        connectionstr = 'http://api.openweathermap.org/data/2.5/weather?q=Bangkok&APPID=' + SecretKey.WeatherAPIKey
        self.response =requests.get(connectionstr).json()

    def getvalue(self,key):
        # print(self.response[key])
        return self.response[key]

    def getWeather(self):
        # print(self.getvalue("weather"))
        return self.getvalue("weather")[0]["description"] + " in Bangkok"

    def getTempurature(self):
        return self.toCelcius(self.toCelcius(self.getvalue('main')['temp']))

    def getMaxTemp(self):
        return self.toCelcius(self.getvalue('main')['temp_max'])

    def getMinTemp(self):
        return self.toCelcius(self.getvalue('main')['temp_min'])

    def toCelcius(self,f):
        celcius = (float(f) - 32) * (5/9)
        return round(celcius,2)

    # {u'base': u'cmc stations',
    #  u'clouds': {u'all': 68},
    #  u'cod': 200,
    #  u'coord': {u'lat': 51.50853, u'lon': -0.12574},
    #  u'dt': 1383907026,
    #  u'id': 2643743,
    #  u'main': {u'grnd_level': 1007.77,
    #            u'humidity': 97,
    #            u'pressure': 1007.77,
    #            u'sea_level': 1017.97,
    #            u'temp': 282.241,
    #            u'temp_max': 282.241,
    #            u'temp_min': 282.241},
    #  u'name': u'London',
    #  u'sys': {u'country': u'GB', u'sunrise': 1383894458, u'sunset': 1383927657},
    #  u'weather': [{u'description': u'broken clouds',
    #                u'icon': u'04d',
    #                u'id': 803,
    #                u'main': u'Clouds'}],
    #  u'wind': {u'deg': 158.5, u'speed': 2.36}}
