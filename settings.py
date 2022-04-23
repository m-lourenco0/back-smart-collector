from os import environ

try:
    
    SERVICE_HOST = environ['SERVICE_HOST']
    SERVICE_ADRESS = environ['SERVICE_ADRESS']
    SERVICE_NAME = environ['SERVICE_NAME']
    SERVICE_PORT = int(environ['SERVICE_PORT'])

except Exception as e:

    SERVICE_HOST = '0.0.0.0'
    SERVICE_ADRESS = 'myproject'
    SERVICE_NAME = 'myproject'
    SERVICE_PORT = 81

    SQL_SERVER = '34.95.248.143'
    SQL_DATABASE = 'SmartCollector'
    SQL_USER = 'sqlserver'
    SQL_PASS = 'sa13509'

    API_KEY = 'AIzaSyD175PxUd2mGLbrGd6YYwP35je2hHIuuLI'

    SECRET_KEY = 'minhachavesupersecreta'