from os import environ
from flask import Flask
# from flask_classy_swagger import swaggerify
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import settings
from datetime import timedelta

#Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = settings.SECRET_KEY
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=5)
# app.config['JWT_TOKEN_LOCATION'] = ['cookies']
jwt = JWTManager(app)
CORS(app)


#Registro no swagger.
# swaggerify(app, 'My-Project', '1.0.0', swagger_path='/swagger')

@app.after_request
def after_request(response):
    # response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Headers', 'access-control-allow-origin, Content-Type, access-control-allow-credentials')
    return response

#Controller Imports
from src.controller.Vehicle import Vehicle
from src.controller.Person import Person
from src.controller.Service import Service
from src.controller.Login import Login
from src.controller.Solicitation import Solicitation
from src.controller.Routes import Routes


#Controllers
app.register_blueprint(Vehicle.vehicle_controller)
app.register_blueprint(Person.person_controller)
app.register_blueprint(Service.service_controller)
app.register_blueprint(Login.login_controller)
app.register_blueprint(Solicitation.solicitation_controller)
app.register_blueprint(Routes.routes_controller)


if __name__ == '__main__':
    # logger = logging.getLogger('waitress')
    # logger.setLevel(logging.DEBUG)
    # run_simple(hostname= settings.SERVICE_HOST, port=settings.SERVICE_PORT, application=app)
    # serve(app, host=settings.SERVICE_HOST, port=settings.SERVICE_PORT)
    app.run()