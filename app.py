from flask import Flask
from flask_classy_swagger import swaggerify
import settings
#from werkzeug.serving import run_simple
from dynaconf import settings
from waitress import serve
import logging

#Controller Imports
from src.controller.Keypress import Keypress
from src.controller.OS import OS

#Configuration
app = Flask(__name__)

#Registro no swagger.
swaggerify(app, 'My-Project', '1.0.0', swagger_path='/swagger')

#Controllers
Keypress.register(app)
OS.register(app)



if __name__ == '__main__':
    logger = logging.getLogger('waitress')
    logger.setLevel(logging.DEBUG)
    #run_simple(hostname= settings.SERVICE_HOST, port=settings.SERVICE_PORT, application=app)
    serve(app, host=settings.SERVICE_HOST, port=settings.SERVICE_PORT)
    #app.run(debug=True)