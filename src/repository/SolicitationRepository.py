from sqlalchemy import insert
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
from datetime import date, datetime

from .Base.BaseRepository import BaseRepository
from src.model.SolicitationModel import Solicitation

Base = declarative_base()


class SolicitationRepository(BaseRepository):

    def get_solicitation_list():
        query = BaseRepository.context.query(Solicitation).filter(Solicitation.DeletedDate == None)
        df = pd.read_sql(query.statement, BaseRepository.context.bind)
        return df.to_dict(orient='records')

    def get_solicitation_by_id(id):
        try:
            query = BaseRepository.context.query(Solicitation).filter(Solicitation.id_Coleta == id, Solicitation.DeletedDate == None)
            df = pd.read_sql(query.statement, BaseRepository.context.bind)
            return df.to_dict(orient='records')
        except Exception as e:
            print(e)

    def update_solicitation(id, data):
        try:
            query = BaseRepository.context.query(Solicitation).filter(Solicitation.id_Coleta == id)
            query.update(data)
            BaseRepository.context.commit()
        except Exception as e:
            print(e)

    def add_solicitation(data):
        try:
            i = insert(Solicitation).values(data)
            BaseRepository.context.execute(i)
            BaseRepository.context.commit()
        except Exception as e:
            print(e)

    def delete_solicitation(id):
        try:
            data = {
                'DeletedDate': datetime.now()
            }
            query = BaseRepository.context.query(Solicitation).filter(Solicitation.id_Coleta == id)
            query.update(data)
            BaseRepository.context.commit()
        except Exception as e:
            print(e)