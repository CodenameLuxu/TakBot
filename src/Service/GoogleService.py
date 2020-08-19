
import googlemaps
from src.SecretKey import SecretKey
import requests
import json
import socket
from src.TakBot import TakConstants
from src.Model.GooglePlace import GooglePlace
class GoogleService():

    def __init__(self):
        self.mapsAPI = googlemaps.Client(SecretKey.googleapi)

    def getHere(self):
        send_url = SecretKey.ipstackKey
        send_url = send_url.replace(TakConstants.Replace_IP,self.getCurrentIP())
        r = requests.get(send_url)
        j = json.loads(r.text)
        return j['latitude'],j['longitude']

    def getCurrentIP(self):
        host = socket.gethostname()
        ## getting the IP address using socket.gethostbyname() method
        ip_address = socket.gethostbyname(host)
        return ip_address

    def coordinateToString(self,lat,long):
        return str(lat) + ','+str(long)

    def findPlaces(self,searchTerm):
        searchTerm.replace(' ','%20')
        radius = 2000
        lat , long = self.getHere()

        url ="https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={searchterm}&inputtype=textquery&locationbias=circle:{radius}@{lat},{long}&key={APIKEY}"
        url =url.replace('{searchterm}',searchTerm)
        url =url.replace('{lat}',str(lat))
        url =url.replace('{long}',str(long))
        url =url.replace('{radius}',str(radius))
        url =url.replace('{APIKEY}',SecretKey.googleapi)
        r = requests.get(url)
        result = json.loads(r.text)
        id = result['candidates'][0]['place_id']
        return self.findPlaceByID(id)

    def findPlaceByID(self,id):
        url = "https://maps.googleapis.com/maps/api/place/details/json?placeid={ID}&key={API}"
        fields = "&fields=url,formatted_address,name,website"
        url += fields
        url = url.replace('{ID}',id)
        url = url.replace('{API}',SecretKey.googleapi)
        r = requests.get(url)
        result = json.loads(r.text)
        obj = GooglePlace(result)
        return obj
