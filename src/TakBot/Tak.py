
from src.TakBot.GreetingProcessor import GreetingProcessor
from src.TakBot.StatementProcessor import StatementProcessor
from src.Service.EmailService import EmailService
from src.Service.GoogleService import GoogleService
from src.Service.BrowserService import BrowserService
import threading
from src.TakBot.WordGroup import WordGroup
from src.Model.GooglePlace import GooglePlace
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
        if self.Statementprocessor.isEmailConveration():
            return self.emailConversation()
        elif self.Statementprocessor.isLocationConversation():
            return self.locationConversation()
        return self.Statementprocessor.getResponse()

    def emailConversation(self):
        try:
            emailservice = EmailService()
            # Get destination email
            self.say(' to who(email)?')
            email = self.getUserResponse('email')
            while not emailservice.isValidEmail(email):
                self.say('Invalid email please try again')
                email = self.getUserResponse('email')
            # Get Content
            body = self.getUserResponse('body')
            emailservice.sendEmailTo( email,body)
            return 'Mail sent'
        except:
            return 'Mail not sent'

    def locationConversation(self):
        try:
            gmaps = GoogleService()
            self.say('Where would you like to search:')
            searchTerm = self.getUserResponse('Place')
            placeObj = gmaps.findPlaces(searchTerm)
            self.say('Place found:')
            self.say(placeObj.toString())
            self.say('Would you like to open google map?')
            response = self.getUserResponse('Yes/No')
            if self.Statementprocessor.isAgreeWord(response.strip()):
                BrowserService.open(placeObj.link)
            return 'Complete'
        except Exception as e:
            print(e)
            return 'Place not found'


    def say(self, sentence):
        print('Bot : %s' % sentence)

    def getUserResponse(self,format):
        return input('User [%s]: '% format)
