from sqlalchemy import NVARCHAR, Column
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER,VARCHAR,DECIMAL,INTEGER,DATETIME2
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Person(Base):
    __tablename__ = "tbdPessoa"
    id_Pessoa = Column(INTEGER, primary_key=True)
    ds_Pessoa = Column(VARCHAR(50))
    ds_Endereco = Column(VARCHAR(50))
    nr_Endereco = Column(VARCHAR(50))
    ds_Bairro = Column(VARCHAR(50))
    ds_Login = Column(VARCHAR(50))
    ds_Senha = Column(VARCHAR(50))
    tp_TipoUsuario = Column(VARCHAR(1))
    vl_LatitudeLongitude = Column(VARCHAR(50))
    DeletedDate = Column(DATETIME2)