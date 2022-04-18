from sqlalchemy import insert
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
from datetime import date, datetime

from .Base.BaseRepository import BaseRepository
from src.model.VehicleModel import Vehicle

Base = declarative_base()


class VehicleRepository(BaseRepository):

    def get_vehicle_list():
        query = BaseRepository.context.query(Vehicle).filter(Vehicle.DeletedDate == None)
        df = pd.read_sql(query.statement, BaseRepository.context.bind)
        return df.to_dict(orient='records')

    def get_vehicle_by_id(id):
        try:
            query = BaseRepository.context.query(Vehicle).filter(Vehicle.id_Veiculo == id, Vehicle.DeletedDate == None)
            df = pd.read_sql(query.statement, BaseRepository.context.bind)
            return df.to_dict(orient='records')
        except Exception as e:
            print(e)

    def update_vehicle(id, data):
        try:
            query = BaseRepository.context.query(Vehicle).filter(Vehicle.id_Veiculo == id)
            query.update(data)
            BaseRepository.context.commit()
        except Exception as e:
            print(e)

    def add_vehicle(data):
        try:
            i = insert(Vehicle).values(data)
            BaseRepository.context.execute(i)
            BaseRepository.context.commit()
        except Exception as e:
            print(e)

    def delete_vehicle(id):
        try:
            data = {
                'DeletedDate': datetime.now()
            }
            query = BaseRepository.context.query(Vehicle).filter(Vehicle.id_Veiculo == id)
            query.update(data)
            BaseRepository.context.commit()
        except Exception as e:
            print(e)