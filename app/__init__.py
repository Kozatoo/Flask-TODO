import os
import sqlalchemy
from yaml import load,Loader
from flask import Flask
app = Flask(__name__)

def init_connect_engine():
    if os.environ.get('GAE_ENV') != 'standard':
        variables= load(open("app.yaml"),Loader=Loader)
        env_variables=variables['env_variables']
        for var in env_variables:
            os.environ[var]=env_variables[var]

        pool = sqlalchemy.create_engine(
            sqlalchemy.engine.url.URL(
                drivername="mariadb+mariadbconnector",
                username=os.environ.get('MDB_USER'),
                password=os.environ.get("MDB_PASSWORD"),
                database=os.environ.get("MDB_DB"),
                host=os.environ.get("MDB_HOST"),
                port=os.environ.get('MDB_PORT')
            )
        )
        return pool

db= init_connect_engine()

conn=db.connect()
from app import routes