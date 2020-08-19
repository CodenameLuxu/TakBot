
from src.SecretKey import SecretKey
import smtplib, ssl
from src.TakBot import TakConstants as Tags
import re

class EmailService:


    def sendEmailTo(self, client,message):
        sent_from = SecretKey.Sender_email
        to = [client]
        subject = 'TakBot Message'
        body = message

        email_text = """\
        Tak Bot message
        Subject: %s

        %s
        """ % ( subject, body)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(SecretKey.Sender_email, SecretKey.Sender_password)
            server.sendmail(SecretKey.Sender_email, to, email_text)
            server.close()
        except Exception as e:
            print('Exception : {0}'.format(str(e)))

    def isValidEmail(self, email):
        format = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        return re.search(format,email)
