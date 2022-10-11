from asyncio.log import logger
import json
from werkzeug.wrappers import Response
from nameko.web.handlers import http
from nameko.rpc import RpcProxy

class HttpService:
    name = "api-rest-chubb"
    roulette_proxy = RpcProxy("roulette_service")
    user_proxy = RpcProxy("user_service")

    @http("GET", "/api/status")
    def status(self, request):
        return json.dumps({ "message": "API REST with NAMEKO ready" })

    # Roulette services
    @http("POST", "/api/roulette")
    def create_roulette(self, request):
        if request.get_json() is None or request.get_json() == {}:
            return Response("Bad request", 400)

        try:
            result = self.roulette_proxy.create_roulette_rpc(request.get_json())
            print(result)
            res = Response("OK")
            # res.data = json.dumps({ "message": "OK", "data": result })
            # res.headers["content-type"] = "application/json"
            return res
        except Exception as ex:
            logger.error(ex)
            logger.error("Error in the http service roulette")
            return Response("Internal server error", 500)

    # User services
    @http("POST", "/api/user")
    def create_user(self, request):
        try:
            self.user_proxy.create_user(request.get_json())
            res = Response("OK")
            res.headers["content-type"] = "application/json"

            return res
        except Exception as ex:
            logger.error(ex)
            logger.error("Error in the http service create_user")
            return Response("Internal server error", 500)

    @http("PATCH", "/api/roulette")
    def open_roulette_bet(self, request):
        if request.get_json() is None or request.get_json() == {}:
            return Response("Bad request", 400)

        if "id" not in request.get_json():
            return Response("Bad request", 400)

        id: int = int(request.get_json()["id"])

        try:
            self.roulette_proxy.open_roulette_bet_rpc(id)
            return Response("OK", 200)
        except Exception as ex:
            logger.error(ex)
            logger.error("Could'nt open the roulette with id: {} to play".format(id))
            return Response("Internal server error", 500)

    # @http("GET", "/api/order")
    # def get_orders(self, request):
    #     orders = self.order_proxy.get_orders()
    #     res = Response("OK")
    #     res.data = json.dumps({ "message": "ok", "data": orders })
    #     res.headers["content-type"] = "application/json"
    #     return res

    # @http("GET", "/api/product")
    # def get_products(self, request):
    #     try:
    #         products = self.product_proxy.get_products()
    #         res = Response("OK")
    #         res.data = json.dumps(products)
    #         res.headers["content-type"] = "application/json"
    #         return res
    #     except Exception as e:
    #         print(e)
    #         return Response("Internal server error", 500)

    # @http("PATCH", "/api/order")
    # def pay_order(self, request):
    #     body = request.get_json()

    #     if not body["order_id"]:
    #         return Response("Bad request", 400)

    #     result = self.order_proxy.pay_order(body["order_id"])

    #     if result == "error" or result == False:
    #         return Response("Internal server error", 500)

    #     return Response("OK", 200)