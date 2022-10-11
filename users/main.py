from asyncio.log import logger
import json
from nameko.rpc import rpc, RpcProxy
from models.base_model import pg_conn
from models.user_model import User as UserModel
from core_business.user_core import UserCore

def create_tables():
    with pg_conn:
        pg_conn.create_tables([UserModel], safe=True)

create_tables()

class HttpService(UserCore):
    name = "user_service"

    @rpc
    def create_user(self, data):
        try:
            self.create_user_core(data)
        except Exception as ex:
            msg_error = "Error in the servic rpc create_user"
            logger.error(ex)
            logger.error(msg_error)
            raise Exception(msg_error)