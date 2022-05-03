from os import environ

try:
    
    SERVICE_HOST = environ['SERVICE_HOST']
    SERVICE_ADRESS = environ['SERVICE_ADRESS']
    SERVICE_NAME = environ['SERVICE_NAME']
    SERVICE_PORT = int(environ['SERVICE_PORT'])

    SQL_SERVER = environ['SQL_SERVER']
    SQL_DATABASE = environ['SQL_DATABASE']
    SQL_USER = environ['SQL_USER']
    SQL_PASS = environ['SQL_PASS']

    API_KEY = environ['API_KEY']

    SECRET_KEY = environ['SECRET_KEY']

    COOKIE_DOMAIN = environ['COOKIE_DOMAIN']

except Exception as e:

    SERVICE_HOST = '0.0.0.0'
    SERVICE_ADRESS = 'myproject'
    SERVICE_NAME = 'myproject'
    SERVICE_PORT = 5000

    SQL_SERVER = '34.95.248.143'
    SQL_DATABASE = 'SmartCollector'
    SQL_USER = 'sqlserver'
    SQL_PASS = 'sa13509'

    API_KEY = 'AIzaSyD175PxUd2mGLbrGd6YYwP35je2hHIuuLI'

    SECRET_KEY = 'minhachavesupersecreta'

    COOKIE_DOMAIN = 'https://smart-collector-app.vercel.app'