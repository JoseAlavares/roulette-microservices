from peewee import CharField, BooleanField, TextField, DecimalField
from .base_model import BaseModel

class User(BaseModel):
    name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    email = CharField(max_length=255)
    user = CharField(max_length=255)
    password = TextField()
    credit = DecimalField(max_digits=10, decimal_places=2)
    active = BooleanField(default=True)
    