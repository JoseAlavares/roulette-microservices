from email.policy import default
from xmlrpc.client import Boolean
from peewee import *
from models.base_model import BaseModel
from models.order_model import OrderModel

class OrderDetailModel(BaseModel):
    order = ForeignKeyField(OrderModel, backref="product_order")
    product_id = IntegerField()
    product_name = CharField(max_length=150)
    active = BooleanField(default=True)