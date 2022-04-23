import requests
from dynaconf import settings
import urllib

class GoogleMaps:


    def get_geocode(endereco, bairro, num):
        # Get the latitude and longitude of the address using google api
        # https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY
        address = urllib.parse.quote(f'{endereco}%20{bairro}%20{num}')
        key = settings.API_KEY
        url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={key}'
        res = requests.request('GET', url)

        if(res.status_code != 200):
            return False

        result = res.json()
        result = result['results'][0]['geometry']['location']
        data = f'{result["lat"]}, {result["lng"]}'

        return data

    def get_routes_by_coordinates(coordinates):
        # Get the routes between multiple coordinates using Google API
        key = settings.API_KEY
        origin = urllib.parse.quote(':-22.3790123 -47.3635086')

        for coordinate in coordinates:
            coordinate = coordinate.replace(',', ' ')
            coordinate = urllib.parse.quote(coordinate)

        destination = coordinates.pop()

        if (len(coordinates) > 0):
            url = f'https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&waypoints={coordinates}&key={key}'
        else:
            url = f'https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={key}'

        url = f'https://maps.googleapis.com/maps/api/directions/json?destination={destination}&origin={origin}waypoints={waypoints}&key={key}'
        # url = f'https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={key}'
        