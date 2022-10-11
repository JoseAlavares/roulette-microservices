
from peewee import CharField, BooleanField, IntegerField
from .base_model import BaseModel

class Roulette(BaseModel):
    roulette_name = CharField(max_length=150)
    open = BooleanField(default=False)