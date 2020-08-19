
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
            elif token.lemma_.lower() in WordGroup.Category_Action:
                self.addTag(Tags.Tag_Action)
            elif token.lemma_.lower() in WordGroup.Category_Greeting_All:
                self.addTag(Tags.Tag_Greeting)
            elif token.pos_.lower() == "PROPN":
                self.addTag("NAME:"+token.text)
            elif token.lemma_.lower() == "weather":
                self.addTag(Tags.Tag_Weather)

        self.emailAnalytic()
        self.locationAnalytic()

    def emailAnalytic(self):
        text = [token.lemma_.lower() for token in self.tokens]
        for word in WordGroup.Category_Delivery:
            if word in text:
                self.addTag(Tags.Tag_Deliver)

        for word in WordGroup.Category_Medium:
            if word in text:
                self.addTag(Tags.Tag_Email)

    def locationAnalytic(self):
        text = [token.lemma_.lower() for token in self.tokens]
        access = WordGroup.Category_Retrieve
        access.extend(WordGroup.Category_Travel)

        for word in text:
            if word in access:
                self.addTag(Tags.Tag_Get)
            elif word in WordGroup.Category_Place:
                self.addTag(Tags.Tag_Location)


    def addTag(self,tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def isEmailAction(self):
        return Tags.Tag_Email in self.tags and Tags.Tag_Deliver in self.tags

    def isLocationAction(self):
        return Tags.Tag_Get in self.tags and Tags.Tag_Location in self.tags

    def isGreeting(self):
        return (Tags.Tag_Greeting in self.tags)

    def isQuestion(self):
        return (Tags.Tag_Question in self.tags)
