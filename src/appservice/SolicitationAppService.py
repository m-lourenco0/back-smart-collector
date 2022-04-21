from dateutil import parser
import pandas as pd

from src.repository.SolicitationRepository import SolicitationRepository
from src.utils.maps_utils import GoogleMaps

class SolicitationAppService():


    def get_solicitation():
        try:
            solicitations = SolicitationRepository.get_solicitation_list()
            return {'data': solicitations, 'message': f'Success getting vehicle list.'}, 200
        except Exception as e:
            print(e)
        
    def get_solicitation_by_id(id):
        try:
            solicitation = SolicitationRepository.get_solicitation_by_id(id)
            return {'data': solicitation, 'message': f'Success getting vehicle list.'}, 200
        except Exception as e:
            print(e)

    def update_solicitation(id, data):
        try:
            
            if (data['data_chegada'] != ''):
                data_chegada = parser.parse(data['data_chegada'])
            else:
                data_chegada = None

            bd_data = {
               'id_Veiculo': data['veiculo'],
               'vl_Peso': data['peso'],
               'dt_Saida': data['data_saida'],
               'st_Status': data['status'],
               'dt_Chegada': data_chegada,
            }
            solicitation = SolicitationRepository.update_solicitation(id, bd_data)
            return {'message': f'Success updating solicitation.'}, 200
        except Exception as e:
            print(e)

    def add_solicitation(data):
        try:
            bd_data = {
                'id_Pessoa': data['id_Pessoa'],
                'dt_Solicitacao': pd.to_datetime(data['dt_Solicitacao']),
                'vl_LatitudeLongitude': GoogleMaps.get_geocode(data['ds_Endereco'], data['ds_Bairro'], data['nr_Endereco']),
                'ds_Observacao': data['ds_Observacao'],
            }
            solicitation = SolicitationRepository.add_solicitation(bd_data)
            return {'message': f'Success adding solicitation.'}, 200
        except Exception as e:
            print(e)

    def delete_solicitation(data):
        try:
            solicitation = SolicitationRepository.delete_solicitation(data)
            return {'message': f'Success deleting solicitation.'}, 200
        except Exception as e:
            print(e)
        