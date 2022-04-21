from sqlalchemy import  Column
from sqlalchemy.dialects.mssql import VARCHAR,DECIMAL,INTEGER,DATETIME
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Solicitation(Base):
    __tablename__ = "tbdSolicitacao"
    id_Solicitacao = Column(INTEGER, primary_key=True)
    id_Pessoa = Column(INTEGER)
    vl_PesoKG = Column(DECIMAL(5,2))
    dt_Solicitacao = Column(DATETIME)
    id_Coleta = Column(INTEGER)
    vl_LatitudeLongitude = Column(VARCHAR(50))
    ds_Observacao = Column(VARCHAR(500))