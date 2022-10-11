from asyncio.log import logger
from nameko.rpc import rpc
from models.base_model import pg_conn
from models.roulette_model import Roulette as RouletteModel
from models.roulette_result_model import RouletteResults as RouletteResultsModel
from core_business.roulete_class import RouletteCore

def create_tables():
    with pg_conn:
        pg_conn.create_tables([RouletteModel, RouletteResultsModel], safe=True)

create_tables()

class HttpService(RouletteCore):
    name = "roulette_service"

    @rpc
    def create_roulette_rpc(self, data):
        try:
            self.create_roulette_and_results(data)
        except Exception as ex:
            logger.info(ex)

    @rpc
    def open_roulette_bet_rpc(self, id):
        try:
            self.open_roulette_to_bet(id)
        except Exception as ex:
            logger.error(ex)
            logger.error("Couldn't open a roulette to bet")
