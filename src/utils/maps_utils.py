import requests
import settings
from src.repository.ServiceRepository import ServiceRepository

class GoogleMaps:


    def get_geocode(endereco, bairro, num, cidade, estado):
        # Get the latitude and longitude of the address using google api
        # https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY
        address = f'{endereco}%20{bairro}%20{num}%20{cidade}%20{estado}'
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
        origin = '-22.3790123, -47.3635086'
        destination = '-22.37498309146081, -47.37011743571834'

        waypoints = ''

        for coordinate in coordinates:
            waypoints = waypoints + f'{coordinate}|'

        waypoints = waypoints[:-1]

        # url = f'https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&waypoints=optimize%3Atrue%7C{uniararas}&key={key}'

        return {
            'ds_Origin': origin,
            'ds_Destination': destination,
            'ds_Waypoints': waypoints,
        }

        # url = f'https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={key}'
        
    def calculate_route(id_coleta):

        coleta = ServiceRepository.get_service_by_id(id_coleta)[0]
        origin = coleta['ds_Origin']
        destination = coleta['ds_Destination']
        waypoints = coleta['ds_Waypoints']
        # Get the routes between multiple coordinates using Google API
        key = settings.API_KEY
        url = f'https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&waypoints=optimize%3Atrue%7C{waypoints}&mode=driving&key={key}'
        res = requests.request('GET', url)

        if(res.status_code != 200):
            return False

        result = res.json()

        return result