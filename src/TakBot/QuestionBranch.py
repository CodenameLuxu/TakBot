

from src.TakBot.StatementObj import StatementObj
from src.Service.WeatherService import WeatherServiceAPI
from src.TakBot import TakConstants as Tags

def getResponse(statementObj):
    if isObjectContainTag(statementObj,Tags.Tag_Weather):
        return getWeatherResponse(statementObj)

def getWeatherResponse(statementObj):
    weatherapi = WeatherServiceAPI()
    return weatherapi.getWeather()

def isObjectContainTag(statementObj,tag):
    if tag in statementObj.tags:
        return True
    else:
        return False
