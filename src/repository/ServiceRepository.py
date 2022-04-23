from sqlalchemy import insert
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
from datetime import datetime
import numpy as np

from .Base.BaseRepository import BaseRepository
from src.model.ServiceModel import Service
from src.repository.VehicleRepository import VehicleRepository

Base = declarative_base()


class ServiceRepository(BaseRepository):

    def get_service_list():
        query = BaseRepository.context.query(Service).filter(Service.DeletedDate == None)
        df = pd.read_sql(query.statement, BaseRepository.context.bind)

        vehicle_list = pd.DataFrame(VehicleRepository.get_vehicle_list())
        vehicle_list = vehicle_list[['id_Veiculo', 'ds_Veiculo', 'cd_Placa']]

        df = df.merge(vehicle_list, on='id_Veiculo', how='left')

        df = df.where(df.notnull(), None)
        df.replace({np.nan: None}, inplace = True)
        df = df.where(df.notna(), None)


        return df.to_dict(orient='records')

    def get_service_by_id(id):
        try:
            query = BaseRepository.context.query(Service).filter(Service.id_Coleta == id, Service.DeletedDate == None)
            df = pd.read_sql(query.statement, BaseRepository.context.bind)

            vehicle_list = pd.DataFrame(VehicleRepository.get_vehicle_list())
            vehicle_list = vehicle_list[['id_Veiculo', 'ds_Veiculo', 'cd_Placa']]

            df = df.merge(vehicle_list, on='id_Veiculo', how='left')

            return df.to_dict(orient='records')
        except Exception as e:
            print(e)

    def update_service(id, data):
        try:
            query = BaseRepository.context.query(Service).filter(Service.id_Coleta == id)
            query.update(data)
            BaseRepository.context.commit()
        except Exception as e:
            print(e)

    def add_service(data):
        try:
            i = insert(Service).values(data)
            f = BaseRepository.context.execute(i)
            BaseRepository.context.commit()
            return f.inserted_primary_key[0]
        except Exception as e:
            print(e)

    def delete_service(id):
        try:
            data = {
                'DeletedDate': datetime.now()
            }
            query = BaseRepository.context.query(Service).filter(Service.id_Coleta == id)
            query.update(data)
            BaseRepository.context.commit()
        except Exception as e:
            print(e)