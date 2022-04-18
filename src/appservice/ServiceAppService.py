from dateutil import parser

from src.repository.ServiceRepository import ServiceRepository

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
            bd_data = {
               'id_Veiculo': data['veiculo'],
               'vl_Peso': data['peso'],
               'dt_Saida': data['saida'],
               'st_Status': data['status'],
               'dt_Chegada': data['chegada'],
            }
            service = ServiceRepository.add_service(bd_data)
            return {'message': f'Success adding service.'}, 200
        except Exception as e:
            print(e)

    def delete_service(data):
        try:
            service = ServiceRepository.delete_service(data)
            return {'message': f'Success deleting service.'}, 200
        except Exception as e:
            print(e)
        