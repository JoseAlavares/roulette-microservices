from peewee import *

pg_conn = PostgresqlDatabase("nameko-orders", user="postgres", password="admin", host="postgres-nameko-db", port=5432)

class BaseModel(Model):
    class Meta:
        database = pg_conn