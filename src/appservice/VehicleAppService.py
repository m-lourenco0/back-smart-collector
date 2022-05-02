from src.repository.VehicleRepository import VehicleRepository

class VehicleAppService():


    def get_vehicle():
        try:
            vehicles = VehicleRepository.get_vehicle_list()
            return {'data': vehicles, 'message': f'Success getting vehicle list.'}, 200
        except Exception as e:
            print(e)

    def get_available_vehicle():
        try:
            vehicles = VehicleRepository.get_available_vehicle_list()
            return {'data': vehicles, 'message': f'Success getting vehicle list.'}, 200
        except Exception as e:
            print(e)
        
    def get_vehicle_by_id(id):
        try:
            vehicle = VehicleRepository.get_vehicle_by_id(id)
            return {'data': vehicle, 'message': f'Success getting vehicle list.'}, 200
        except Exception as e:
            print(e)

    def update_vehicle(id, data):
        try:
            bd_data = {
               'ds_Veiculo': data['nome'],
               'vl_CapacidadeKG': data['capacidade'],
               'cd_Placa': data['placa']
            }
            vehicle = VehicleRepository.update_vehicle(id, bd_data)
            return {'message': f'Success updating vehicle.'}, 200
        except Exception as e:
            print(e)

    def add_vehicle(data):
        try:
            bd_data = {
               'ds_Veiculo': data['nome'],
               'vl_CapacidadeKG': data['capacidade'],
               'cd_Placa': data['placa']
            }
            vehicles = VehicleRepository.add_vehicle(bd_data)
            return {'message': f'Success adding vehicle.'}, 200
        except Exception as e:
            print(e)

    def delete_vehicle(data):
        try:
            vehicles = VehicleRepository.delete_vehicle(data)
            return {'message': f'Success deleting vehicle.'}, 200
        except Exception as e:
            print(e)
        