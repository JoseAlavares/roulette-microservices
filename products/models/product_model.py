from email.policy import default
from enum import unique
from xmlrpc.client import Boolean
from peewee import *
from .base_model import BaseModel

class ProductModel(BaseModel):
    name = CharField(max_length=150, unique=True)
    description = TextField()
    price = DecimalField(max_digits=8, decimal_places=2)
    active = BooleanField(default=True)