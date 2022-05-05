from flask_jwt_extended import jwt_required

from src.repository.PersonRepository import PersonRepository
from src.utils.maps_utils import GoogleMaps

class PersonAppService():

    def get_person():
        try:
            person = PersonRepository.get_person_list()
            return {'data': person, 'message': f'Success getting person list.'}, 200
        except Exception as e:
            print(f'Error getting person list. Error: {e}', flush=True)
        
    def get_person_by_id(id):
        try:
            person = PersonRepository.get_person_by_id(id)
            return {'data': person, 'message': f'Success getting person list.'}, 200
        except Exception as e:
            print(f'Error getting person by id. Error: {e}', flush=True)

    def update_person(id, data):
        try:
            bd_data = {
                'ds_Pessoa': data['nome'],
                'ds_Endereco': data['endereco'],
                'ds_Bairro': data['bairro'],
                'nr_Endereco': data['numero'],
                'ds_Cidade': data['cidade'],
                'ds_Estado': data['estado'],
                'ds_Login': data['login'],
                'ds_Senha': data['senha'],
                'vl_LatitudeLongitude': GoogleMaps.get_geocode(data['endereco'], data['bairro'], data['numero'], data['cidade'], data['estado'])
            }
            person = PersonRepository.update_person(id, bd_data)
            return {'message': f'Success updating person.'}, 200
        except Exception as e:
            print(f'Error updating person. Error: {e}', flush=True)

    def add_person(data):
        try:
            bd_data = {
                'ds_Pessoa': data['nome'],
                'ds_Endereco': data['endereco'],
                'ds_Bairro': data['bairro'],
                'nr_Endereco': data['numero'],
                'ds_Cidade': data['cidade'],
                'ds_Estado': data['estado'],
                'ds_Login': data['login'],
                'ds_Senha': data['senha'],
                'tp_TipoUsuario': 'c',
                'vl_LatitudeLongitude': GoogleMaps.get_geocode(data['endereco'], data['bairro'], data['numero'], data['cidade'], data['estado'])
            }
            person = PersonRepository.add_person(bd_data)
            return {'message': f'Success adding person.'}, 200
        except Exception as e:
            print(f'Error adding person. Error: {e}', flush=True)

    def delete_person(data):
        try:
            person = PersonRepository.delete_person(data)
            return {'message': f'Success deleting person.'}, 200
        except Exception as e:
            print(f'Error deleting person. Error: {e}', flush=True)
        