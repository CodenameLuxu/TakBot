
import random
import datetime
from src.TakBot.WordGroup import WordGroup

class GreetingProcessor:



    def __init__(self):
        self.genericGreeting = WordGroup.Category_Greeting_Generic

        self.morningGreeting = WordGroup.Category_Greeting_Morning
        self.morningGreeting.extend(self.genericGreeting)

        self.afternoonGreeting = WordGroup.Category_Greeting_Afternoon
        self.afternoonGreeting.extend(self.genericGreeting)

        self.eveningGreeting = WordGroup.Category_Greeting_Evening
        self.eveningGreeting.extend(self.genericGreeting)

    def getGenericGreeting(self):
        self.selectRandomGreeting(self.genericGreeting)

    def getTimeSpecificGreeting(self):
        time = datetime.datetime.now().hour
        options = []
        if (time >=  18):
            return self.selectRandomGreeting(self.eveningGreeting)
        elif time >= 12:
            return self.selectRandomGreeting(self.afternoonGreeting)
        elif time >= 6:
            return self.selectRandomGreeting(self.morningGreeting)
        else:
            return self.selectRandomGreeting(self.genericGreeting)


    def selectRandomGreeting(self,options):
        selected = random.randint(0,len(options)-1)
        return options[selected]
