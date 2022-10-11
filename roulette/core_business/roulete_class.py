from asyncio.log import logger
from models.roulette_model import Roulette as RouletteModel
from models.roulette_result_model import RouletteResults as RouletteResultsModel

class RouletteCore:
    def create_roulette_and_results(self, data):
        try:
            result_roulette = RouletteModel.insert(roulette_name=data["roulette_name"], open=False).execute()
            RouletteResultsModel.insert(roulette=result_roulette, user_id=data["user_id"]).execute()
        except Exception as ex:
            msg_error = "Couldn't create a roulette in the DB"
            logger.error(ex)
            logger.error(msg_error)
            raise Exception(msg_error)

    def open_roulette(self, id):
        try:
            RouletteModel.update(open=True).where(id == id).execute()
        except Exception as ex:
            msg_error = "Couldn't open the roultte with id {}".format(id)
            logger.error(ex)
            logger.error(msg_error)
            raise Exception(msg_error)