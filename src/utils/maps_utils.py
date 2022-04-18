import requests
import urllib

class GoogleMaps:


    def get_geocode(endereco, bairro, num):
        # Get the latitude and longitude of the address using google api
        # https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY
        address = urllib.parse.quote(f'{endereco}%20{bairro}%20{num}')
        key = 'AIzaSyD175PxUd2mGLbrGd6YYwP35je2hHIuuLI'
        url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={key}'
        res = requests.request('GET', url)

        if(res.status_code != 200):
            return False

        result = res.json()
        result = result['results'][0]['geometry']['location']
        data = f'{result["lat"]}, {result["lng"]}'

        return data