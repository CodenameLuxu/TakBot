
import re

class GooglePlace:


    def __init__(self,json):
        selected = json['result']
        self.name = selected['name']
        self.address = selected['formatted_address']
        self.link = selected['url']

    def toString(self):
        returstr =" %s \n %s \n" % (self.name,self.address)
        return returstr
