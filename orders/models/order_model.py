# from peewee import PostgresqlDatabase, Model
from email.policy import default
from peewee import *
from .base_model import BaseModel

# pg_conn = PostgresqlDatabase("nameko", user="postgres", password="admin", host="postgres-nameko-db", port=5432)

class OrderModel(BaseModel):
    description = CharField()
    paid = BooleanField(default=False)

# def create_tables():
#     with pg_conn:
#         pg_conn.create_tables([OrderModel])