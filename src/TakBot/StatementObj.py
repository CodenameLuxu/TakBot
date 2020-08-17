
from src.TakBot import TakConstants as Tags
from src.TakBot.WordGroup import WordGroup

class StatementObj:

    def __init__(self,tokens=[]):
        self.tokens = tokens
        self.tags = []

    def analyse(self):
        for token in self.tokens:
            # print(token.lemma_.lower())
            if token.lemma_.lower() in WordGroup.Category_Question:
                self.addTag(Tags.Tag_Question)
            elif token.lemma_.lower() in WordGroup.Category_Greeting_All:
                self.addTag(Tags.Tag_Greeting)
            elif token.lemma_.lower() == "weather":
                self.addTag(Tags.Tag_Weather)

    def addTag(self,tag):
        self.tags.append(tag)

    def isGreeting(self):
        return (Tags.Tag_Greeting in self.tags)

    def isQuestion(self):
        return (Tags.Tag_Question in self.tags)
