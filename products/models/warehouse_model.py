from email.policy import default
from xmlrpc.client import Boolean
from peewee import *
from .base_model import BaseModel

class WarehouseModel(BaseModel):
    name = CharField(max_length=150)
    location_lat = DecimalField(max_digits=11, decimal_places=8)
    location_long = DecimalField(max_digits=11, decimal_places=8)
    warehouse_type = CharField(max_length=100)
    active = BooleanField(default=True)