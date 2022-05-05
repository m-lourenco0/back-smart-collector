from heapq import merge
from sqlalchemy import insert
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
from datetime import date, datetime

from .Base.BaseRepository import BaseRepository
from src.model.SolicitationModel import Solicitation
from src.repository.PersonRepository import PersonRepository

Base = declarative_base()


class SolicitationRepository(BaseRepository):

    def get_solicitation():
        query = BaseRepository.context.query(Solicitation).filter(Solicitation.DeletedDate == None)
        df = pd.read_sql(query.statement, BaseRepository.context.bind)
        return df.to_dict(orient='records')

    def get_solicitation_list():
        query = BaseRepository.context.query(Solicitation).filter(Solicitation.id_Coleta == None, Solicitation.DeletedDate == None)
        df = pd.read_sql(query.statement, BaseRepository.context.bind)

        person_list = pd.DataFrame(PersonRepository.get_person_list())
        person_list = person_list[['id_Pessoa', 'ds_Pessoa']]

        df = df.merge(person_list, on='id_Pessoa', how='left')
        df.drop(columns=['vl_PesoKG'], axis=1, inplace=True)
        df['dt_Solicitacao'] = df['dt_Solicitacao'].apply(lambda x: x.strftime('%d/%m/%Y'))

        return df.to_dict(orient='records')

    def get_solicitation_table():
        query = BaseRepository.context.query(Solicitation).filter(Solicitation.DeletedDate == None)
        df = pd.read_sql(query.statement, BaseRepository.context.bind)

        return df.to_dict(orient='records')

    def get_solicitation_by_id(id):
        try:
            query = BaseRepository.context.query(Solicitation).filter(Solicitation.id_Solicitacao == id, Solicitation.DeletedDate == None)
            df = pd.read_sql(query.statement, BaseRepository.context.bind)
            return df.to_dict(orient='records')
        except Exception as e:
            print(e)

    def clean_service_id(id):
        try:
            query = BaseRepository.context.query(Solicitation).filter(Solicitation.id_Coleta == id)
            query.update({'id_Coleta': None})
            BaseRepository.context.commit()
        except Exception as e:
            print(f'Error trying to clean service_id from solicitations. Error: {e}. Id_Coleta: {id}', flush=True)

    def update_solicitation(id, data):
        try:
            query = BaseRepository.context.query(Solicitation).filter(Solicitation.id_Solicitacao == id)
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
            query = BaseRepository.context.query(Solicitation).filter(Solicitation.id_Solicitacao == id)
            query.update(data)
            BaseRepository.context.commit()
        except Exception as e:
            print(e)