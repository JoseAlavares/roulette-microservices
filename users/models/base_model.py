from peewee import *

pg_conn = PostgresqlDatabase("chubb-user", user="postgres", password="admin", host="postgres-chubb-user", port=5432)

class BaseModel(Model):
    class Meta:
        database = pg_conn