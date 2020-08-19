import os
from src.TakBot.Tak import Tak
from src.Service.WeatherService import WeatherServiceAPI as WeatherService
from src.NLP.NLPEngine import NLPEngine
from src.Service.GoogleService import GoogleService
from src.Service.BrowserService import BrowserService
import threading

import nltk
from nltk import WordNetLemmatizer
from multiprocessing import Pool
import spacy

clearConsole = lambda: os.system('cls')

def run():
    terminate = False
    nlp = NLPEngine()
    tak = Tak()
    clearConsole()
    teller = WeatherService()
    while not terminate:
        request = input("User:")
        if not nlp.isTerminateword(request):
            tak.injestStatement(request)
            response = tak.getResponse()
            print("Bot: %s" % response)
        else:
            terminate = True
    postprocess()


def postprocess():
    clearConsole()

def test():
    gmaps = GoogleService()
    found = gmaps.findPlaces('cafe')
    # found = gmaps.findPlaceByID('ChIJxRDmyDx-HTERCnA6S3TC1IA')
    print(found.toString())
    # print(gmaps.findPlaceByID('ChIJxRDmyDx-HTERCnA6S3TC1IA'))
    # print(gmaps.getCurrentIP())
    # nlp = spacy.load("en_core_web_sm")
    # testsentence = 'send deliver drop dispatch post bring pass give'
    # doc = nlp(testsentence)
    # for token in doc:
    #     print(token.lemma_)
    # BrowserService.open('http://net-informations.com/python/net/browser.htm')


if __name__ == '__main__':
    run()
