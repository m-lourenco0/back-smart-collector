from sqlalchemy import NVARCHAR, Column
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER,VARCHAR,DECIMAL,INTEGER,DATETIME2
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Vehicle(Base):
    __tablename__ = "tbdVeiculo"
    id_Veiculo = Column(INTEGER, primary_key=True)
    ds_Veiculo = Column(VARCHAR(50))
    vl_CapacidadeKG = Column(DECIMAL(5,2))
    cd_Placa = Column(VARCHAR(8))
    DeletedDate = Column(DATETIME2)