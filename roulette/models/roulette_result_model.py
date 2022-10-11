
from email.policy import default
from peewee import BooleanField, ForeignKeyField, IntegerField
from .base_model import BaseModel
from .roulette_model import Roulette

class RouletteResults(BaseModel):
    roulette = ForeignKeyField(Roulette)
    user_id = IntegerField()
    choosen_number = IntegerField(default=0)
    winner_number = IntegerField(default=0)
    is_winner = BooleanField(default=False)
    played = BooleanField(default=False)