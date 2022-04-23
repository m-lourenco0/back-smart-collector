from dateutil import parser
from datetime import datetime
import pandas as pd

from src.repository.ServiceRepository import ServiceRepository
from src.repository.SolicitationRepository import SolicitationRepository
from src.utils.maps_utils import GoogleMaps

class ServiceAppService():


    def get_service():
        try:
            services = ServiceRepository.get_service_list()
            return {'data': services, 'message': f'Success getting vehicle list.'}, 200
        except Exception as e:
            print(e)
        
    def get_service_by_id(id):
        try:
            service = ServiceRepository.get_service_by_id(id)
            return {'data': service, 'message': f'Success getting vehicle list.'}, 200
        except Exception as e:
            print(e)

    def update_service(id, data):
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
            service = ServiceRepository.update_service(id, bd_data)
            return {'message': f'Success updating service.'}, 200
        except Exception as e:
            print(e)

    def add_service(data):
        try:
            id_list = data['id_List']
            geocode_list = []

            service_id = ServiceRepository.add_service({'dt_Solicitacao': datetime.now(), 'st_Status': 'Pendente'})

            for id in id_list:
                SolicitationRepository.update_solicitation(id, {'id_Coleta': service_id})

            s_list = pd.DataFrame(SolicitationRepository.get_solicitation_table())
            s_list = s_list.loc[s_list['id_Solicitacao'].isin(id_list)]
            s_list.apply(lambda x: geocode_list.append(x['vl_LatitudeLongitude']), axis=1)

            route = GoogleMaps.get_routes_by_coordinates(geocode_list)
            
            return {'message': f'Success adding service.'}, 200
        except Exception as e:
            print(e)

    def delete_service(data):
        try:
            service = ServiceRepository.delete_service(data)
            return {'message': f'Success deleting service.'}, 200
        except Exception as e:
            print(e)
        