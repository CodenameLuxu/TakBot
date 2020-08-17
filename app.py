import os
from src.TakBot.Tak import Tak
from src.TakBot.WeatherService import WeatherServiceAPI as WeatherService
from src.NLP.NLPEngine import NLPEngine
import threading

clearConsole = lambda: os.system('cls')

def run():
    terminate = False
    nlp = NLPEngine()
    tak = Tak()
    clearConsole()
    teller = WeatherService()
    while not terminate:
        # print("Enter a name:")
        request = input("User:")
        if not nlp.isTerminateword(request):
            tak.injestStatement(request)
            response = tak.getResponse()
            print("Bot: %s" % response)
            # tokens = nlp.tokenize(request)
            # print(noun)
            # print(verb)
        else:
            terminate = True
    postprocess()


def postprocess():
    clearConsole()

if __name__ == '__main__':
    run()
