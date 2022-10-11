from asyncio.log import logger
import json
from nameko.rpc import rpc, RpcProxy
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