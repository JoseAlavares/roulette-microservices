import json
from nameko.rpc import rpc, RpcProxy
from models.base_model import pg_conn
from models.order_model import OrderModel
from models.order_detail import OrderDetailModel
from classes.order_class import OrderClass

def create_tables():
    with pg_conn:
        pg_conn.create_tables([OrderModel, OrderDetailModel], safe=True)

create_tables()

class HttpService(OrderClass):
    name = "orders"
    product_proxy = RpcProxy("products")
    # order_instance = OrderClass()

    @rpc
    def status(self, request):
        return json.dumps({ "message": "API REST ready" })

    @rpc
    def create_order(self, order_data):
        # try:
        #     ids = [product for product in order_data["details"]]
        #     exists_products = self.product_proxy.querying_products_in(ids)

        #     if exists_products["length_equals"]  is not True:
        #         print('Se rompio')
        #         return 0

        #     order_id = OrderModel.insert(description=order_data["description"], paid=False).execute()
        #     for product in exists_products["products"]:
        #         OrderDetailModel.insert(order=order_id, product_id=product["id"], product_name=product["name"]).execute()

        #     return True
        # except Exception as e:
        #     print("Creacion de orden", e)
        #     return 0

        try:
            self.create_order_and_details(order_data)
        except:
            print('The method rpc -> create_order fails')
            raise Exception('The method rpc -> create_order fails')


    @rpc
    def get_orders(self):
        # try:
        #     query = (OrderModel.select().where(OrderModel.id == 1))
        #     orders = [{ "id": order.id, "description": order.description } for order in query]
        #     return orders
        # except Exception as e:
        #     print(e)
        #     return "error"
        try:
            orders = self.get_all_orders()
            return orders
        except Exception as e:
            msg_error = "Error in the method get_orders"
            print(msg_error, e)
            raise Exception(msg_error)

    @rpc
    def pay_order(self, order_id):
        try:
            order = (OrderModel.select().where(OrderModel.id == order_id and OrderModel.paid == False).count())
            # order = [item.id for item in query]
            # print(order)
            # if orders:
            #     return True
            # else:
            #     return False

            if not order:
                return False

            OrderModel.update(paid=True).execute()
            return { "valid": True }
        except Exception as e:
            print(e)
            return "error"