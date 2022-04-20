from flask import Flask
from flask_classy_swagger import swaggerify
from flask_cors import CORS, cross_origin
import settings
from werkzeug.serving import run_simple
from dynaconf import settings
import logging

#Controller Imports
from src.controller.Vehicle import Vehicle
from src.controller.Person import Person
from src.controller.Service import Service
from src.controller.Login import Login

#Configuration
app = Flask(__name__)
CORS(app)

#Registro no swagger.
swaggerify(app, 'My-Project', '1.0.0', swagger_path='/swagger')

#Controllers
Vehicle.register(app)
Person.register(app)
Service.register(app)
Login.register(app)


if __name__ == '__main__':
    # logger = logging.getLogger('waitress')
    # logger.setLevel(logging.DEBUG)
    run_simple(hostname= settings.SERVICE_HOST, port=settings.SERVICE_PORT, application=app)
    # serve(app, host=settings.SERVICE_HOST, port=settings.SERVICE_PORT)
    #app.run(debug=True)