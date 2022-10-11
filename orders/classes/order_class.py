from models.order_model import OrderModel
from models.order_detail import OrderDetailModel

class OrderClass(OrderModel):
    """
        author: Jose Francisco Alvarez Valdez<alvaresvaldes89@gmail.com>
        description: Create a order master and their details in the database
        date: 2022-08-10
    """
    # @staticmethod
    def create_order_and_details(self, order_data: dict) -> dict:
        try:
            ids = [product for product in order_data["details"]]
            exists_products = self.product_proxy.querying_products_in(ids)

            if exists_products["length_equals"]  is not True:
                print("Some ids not exists in the database")
                return { "exists": False }

            order_id = OrderModel.insert(description=order_data["description"], paid=False).execute()
            for product in exists_products["products"]:
                OrderDetailModel.insert(order=order_id, product_id=product["id"], product_name=product["name"]).execute()

            return { "exists": True }
        except Exception as e:
            print("Creacion de orden", e)
            return {"error": True }

    """
        author: Jose Francisco Alvarez Valdez<alvaresvaldes89@gmail.com>
        description: Search a order by their id
        date: 2022-08-10
    """
    @staticmethod
    def search_order_by_id(self, id: int) -> dict:
        try:
            result = (OrderModel.select().where(OrderModel.id == id)).execute()

            if not order:
                return { "exists": False }

            order = [item for item in result]

            return { "exusts": True, "data": order }
        except Exception as e:
            print(e)
            return { "exists": True }

    """
        author: Jose Francisco Alvarez Valdez<alvaresvaldes89@gmail.com>
        description: Change the flag paid to True in a order by their id
        date: 2022-08-10
    """
    @staticmethod
    def pay_order_by_id(self, id: int) -> bool:
        try:
            (OrderModel.update(OrderModel.paid == True).where(OrderModel.id == id)).execute()
            return True
        except Exception as e:
            print(e)
            return False

    """
        author: Jose Francisco Alvarez Valdez
        description: Get all orders in the table orders
        date: 2022-08-11
    """
    @staticmethod
    def get_all_orders(self) ->  dict:
        try:
            result = (OrderModel.select()).execute()
            orders = [order for order in result]
            return orders
        except Exception as e:
            print(e)
            raise Exception('Error in the method get_all_orders')