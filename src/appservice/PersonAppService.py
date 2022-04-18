from src.repository.PersonRepository import PersonRepository
from src.utils.maps_utils import GoogleMaps

class PersonAppService():

    def get_person():
        try:
            person = PersonRepository.get_person_list()
            return {'data': person, 'message': f'Success getting person list.'}, 200
        except Exception as e:
            print(e)
        
    def get_person_by_id(id):
        try:
            person = PersonRepository.get_person_by_id(id)
            return {'data': person, 'message': f'Success getting person list.'}, 200
        except Exception as e:
            print(e)

    def update_person(id, data):
        try:
            bd_data = {
                'ds_Pessoa': data['nome'],
                'ds_Endereco': data['endereco'],
                'ds_Bairro': data['bairro'],
                'nr_Endereco': data['numero'],
                'ds_Login': data['login'],
                'ds_Senha': data['senha'],
                'vl_LatitudeLongitude': GoogleMaps.get_geocode(data['endereco'], data['bairro'], data['numero'])
            }
            person = PersonRepository.update_person(id, bd_data)
            return {'message': f'Success updating person.'}, 200
        except Exception as e:
            print(e)

    def add_person(data):
        try:
            bd_data = {
               'ds_Pessoa': data['nome'],
               'ds_Endereco': data['endereco'],
               'ds_Bairro': data['bairro'],
               'nr_Endereco': data['numero'],
               'ds_Login': data['login'],
               'ds_Senha': data['senha'],
               'tp_TipoUsuario': 'u',
               'vl_LatitudeLongitude': GoogleMaps.get_geocode(data['endereco'], data['bairro'], data['numero'])
            }
            person = PersonRepository.add_person(bd_data)
            return {'message': f'Success adding person.'}, 200
        except Exception as e:
            print(e)

    def delete_person(data):
        try:
            person = PersonRepository.delete_person(data)
            return {'message': f'Success deleting person.'}, 200
        except Exception as e:
            print(e)
        