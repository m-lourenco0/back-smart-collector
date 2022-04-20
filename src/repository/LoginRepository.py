from sqlalchemy import insert
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
from datetime import date, datetime

from .Base.BaseRepository import BaseRepository
from src.model.PersonModel import Person

Base = declarative_base()


class LoginRepository(BaseRepository):

    def login(login, senha):
        query = BaseRepository.context.query(Person).filter(Person.ds_Login == login, Person.ds_Senha == senha, Person.DeletedDate == None)
        df = pd.read_sql(query.statement, BaseRepository.context.bind)
        return df.to_dict(orient='records')