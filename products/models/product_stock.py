from decimal import Decimal
from email.policy import default
from itertools import product
from xmlrpc.client import Boolean
from peewee import *
from .base_model import BaseModel
from .product_model import ProductModel
from .warehouse_model import WarehouseModel

class ProductStockModel(BaseModel):
    product = ForeignKeyField(ProductModel, field="id", backref="product_in_stock")
    warehouse = ForeignKeyField(WarehouseModel, field="id", backref="location_product")
    quantity = DecimalField(max_digits=11, decimal_places=2)
    min_quantity = DecimalField(max_digits=11, decimal_places=2)
    max_quantity = DecimalField(max_digits=11, decimal_places=2)
    active = BooleanField(default=True)