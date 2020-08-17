
from src.NLP.NLPEngine import NLPEngine
from src.TakBot.StatementObj import StatementObj
from src.TakBot import QuestionBranch
from src.TakBot import TakConstants as Tags
from src.TakBot.GreetingProcessor import GreetingProcessor
from src.TakBot.WordGroup import WordGroup

class StatementProcessor:

    def __init__(self):
        self.nlp = NLPEngine()
        self.statementObj = StatementObj()

    def injest(self, statement):
        self.tokens = self.nlp.tokenize(statement)
        self.statementObj = StatementObj(self.tokens)
        self.statementObj.analyse()

    def getText(self):
        texts = [token.text for token in self.tokens ]
        return texts

    def getResponse(self):
        if self.statementObj.isQuestion():
            return QuestionBranch.getResponse(self.statementObj)

        else:
            greetingprocess = GreetingProcessor()
            return greetingprocess.getTimeSpecificGreeting()
