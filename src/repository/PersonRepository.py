from sqlalchemy import insert
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
from datetime import date, datetime


from .Base.BaseRepository import BaseRepository
from src.model.PersonModel import Person

Base = declarative_base()


class PersonRepository(BaseRepository):

    def get_person_list():
        query = BaseRepository.context.query(Person).filter(Person.DeletedDate == None)
        df = pd.read_sql(query.statement, BaseRepository.context.bind)
        return df.to_dict(orient='records')

    def get_person_by_id(id):
        try:
            query = BaseRepository.context.query(Person).filter(Person.id_Pessoa == id, Person.DeletedDate == None)
            df = pd.read_sql(query.statement, BaseRepository.context.bind)
            return df.to_dict(orient='records')
        except Exception as e:
            print(e)

    def update_person(id, data):
        try:
            query = BaseRepository.context.query(Person).filter(Person.id_Pessoa == id)
            query.update(data)
            BaseRepository.context.commit()
        except Exception as e:
            print(e)

    def add_person(data):
        try:
            i = insert(Person).values(data)
            BaseRepository.context.execute(i)
            BaseRepository.context.commit()
        except Exception as e:
            print(e)

    def delete_person(id):
        try:
            data = {
                'DeletedDate': datetime.now()
            }
            query = BaseRepository.context.query(Person).filter(Person.id_Veiculo == id)
            query.update(data)
            BaseRepository.context.commit()
        except Exception as e:
            print(e)