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
    print(e)
    print('Error: Missing environment variables')
    exit(1)