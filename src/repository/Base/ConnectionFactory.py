import urllib
import settings
from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey
import pyodbc

class ConnectionFactory(): 

    @staticmethod
    def getInstance():
        #linux
        strConnect = "Driver={driver};SERVER=" + settings.SQL_SERVER + ";DATABASE="+ settings.SQL_DATABASE +";UID="+ settings.SQL_USER+";PWD="+ settings.SQL_PASS
        #windows
        # strConnect = "Driver={SQL Server Native Client 11.0};SERVER=" + settings.SQL_SERVER + ";DATABASE="+ settings.SQL_DATABASE +";UID="+ settings.SQL_USER+";PWD="+ settings.SQL_PASS
        params = urllib.parse.quote_plus(strConnect)
        return create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

    @staticmethod
    def getConnection():
        enginer = Base.getInstance()  
        return enginer.begin() 
