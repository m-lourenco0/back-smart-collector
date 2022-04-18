from sqlalchemy import insert
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
from datetime import date, datetime

from .Base.BaseRepository import BaseRepository
from src.model.ServiceModel import Service

Base = declarative_base()


class ServiceRepository(BaseRepository):

    def get_service_list():
        query = BaseRepository.context.query(Service).filter(Service.DeletedDate == None)
        df = pd.read_sql(query.statement, BaseRepository.context.bind)
        return df.to_dict(orient='records')

    def get_service_by_id(id):
        try:
            query = BaseRepository.context.query(Service).filter(Service.id_Coleta == id, Service.DeletedDate == None)
            df = pd.read_sql(query.statement, BaseRepository.context.bind)
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
            BaseRepository.context.execute(i)
            BaseRepository.context.commit()
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