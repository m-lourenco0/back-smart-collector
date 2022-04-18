from sqlalchemy import  Column
from sqlalchemy.dialects.mssql import VARCHAR,DECIMAL,INTEGER,DATETIME2,DATETIME
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Service(Base):
    __tablename__ = "tbdColeta"
    id_Coleta = Column(INTEGER, primary_key=True)
    id_Veiculo = Column(INTEGER)
    vl_Peso = Column(DECIMAL(5,2))
    dt_Saida = Column(DATETIME)
    st_Status = Column(VARCHAR(20))
    dt_Chegada = Column(DATETIME)
    DeletedDate = Column(DATETIME2)