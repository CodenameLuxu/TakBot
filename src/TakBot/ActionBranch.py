from src.SecretKey import SecretKey
import smtplib, ssl
from src.TakBot import TakConstants as Tags

class ActionBranch:

    def getResponse(statementObj):
        print('Getting response.')
        if (Tags.Tag in statementObj.tags and  Tags.Tag_Email in statementObj.tags):
            return "Sending email"
