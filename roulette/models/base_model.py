from peewee import *

pg_conn = PostgresqlDatabase("chubb-roulette", user="postgres", password="admin", host="postgres-chubb-roulette", port=5432)

class BaseModel(Model):
    class Meta:
        database = pg_conn