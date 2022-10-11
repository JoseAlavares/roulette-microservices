import json
from math import prod
from nameko.rpc import rpc
from models.base_model import pg_conn
from models.product_model import ProductModel
from models.product_stock import ProductStockModel
from models.warehouse_model import WarehouseModel

def create_tables():
    with pg_conn:
        pg_conn.create_tables([ProductModel, ProductStockModel, WarehouseModel], safe=True)

create_tables()

class HttpService:
    name = "products"

    @rpc
    def status(self, request):
        return json.dumps({ "message": "RPC service product" })

    @rpc
    def create_product(self, name):
        pass

    @rpc
    def get_products(self):
        try:
            products = (ProductModel.select().where(ProductModel.active == True))
            serialize_products = [{ "id": product.id, "name": product.name, "price": product.price } for product in products]
            return serialize_products
        except Exception as e:
            print(e)
            return 0

    @rpc
    def querying_products_in(self, ids):
        result_products = (ProductModel.select(ProductModel.id, ProductModel.name).where(ProductModel.id.in_(ids))).execute()
        products = [{ "id": product.id, "name": product.name } for product in result_products]
        flag = len(ids) == len(products)
        print(products)
        if flag:
            return { "length_equals": flag, "products": products }
        else:
            return { "length_equals": flag }