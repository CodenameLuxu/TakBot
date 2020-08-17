
from src.TakBot.GreetingProcessor import GreetingProcessor
from src.TakBot.StatementProcessor import StatementProcessor
import threading
from src.TakBot.WordGroup import WordGroup

class Tak:


    def __init__(self):
        self.greetProcessor = GreetingProcessor()
        self.Statementprocessor = StatementProcessor()

    def greeting(self,user):
        starter = self.greetProcessor.getTimeSpecificGreeting()
        response = "%s , %s" % (starter , user)
        return response

    def injestStatement(self,statement):
        self.Statementprocessor.injest(statement)
        return True

    def getResponse(self):
        return self.Statementprocessor.getResponse()
