from asyncio.log import logger
from models.user_model import User as UserModel

class UserCore(UserModel):
    def create_user_core(self, data):
        try:
            self.insert(
                name=data["name"], last_name=data["last_name"], email=data["email"],
                user=data["user"], password=data["password"], credit=data["credit"],
                active=["active"]
            ).execute()
        except Exception as ex:
            msg_error = "Couldn't create a user in the DB"
            logger.error(ex)
            logger.error(msg_error)
            raise Exception(msg_error)