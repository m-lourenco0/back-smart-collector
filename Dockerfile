# parent image
FROM python:3.7-slim

WORKDIR /app

ADD . /app

ENV SERVICE_HOST 0.0.0.0
ENV SERVICE_PORT 5000
ENV SERVICE_ADRESS myproject
ENV SERVICE_NAME myproject

ENV SQL_SERVER 34.95.248.143
ENV SQL_DATABASE SamrtCollector
ENV SQL_USER sqlserver
ENV SQL_PASS sa13509

ENV API_KEY AIzaSyD175PxUd2mGLbrGd6YYwP35je2hHIuuLI
ENV SECRET_KEY minhachavesupersecreta

# install FreeTDS and dependencies
RUN apt-get update \
 && apt-get install unixodbc -y \
 && apt-get install unixodbc-dev -y \
 && apt-get install freetds-dev -y \
 && apt-get install freetds-bin -y \
 && apt-get install tdsodbc -y \
 && apt-get install --reinstall build-essential -y

# populate "ocbcinst.ini"
RUN echo "[FreeTDS]\n\
Description = FreeTDS unixODBC Driver\n\
Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so\n\
Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so" >> /etc/odbcinst.ini

# install pyodbc (and, optionally, sqlalchemy)
RUN pip install --trusted-host pypi.python.org pyodbc==4.0.26 sqlalchemy==1.3.5
RUN pip install -r requirements.txt

# run app.py upon container launch
CMD ["python", "app.py"]