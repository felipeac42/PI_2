from flask import Flask
from src.routes.routes import *

app = Flask('__name__')

app.add_url_rule(routes["index_route"],view_func=routes["index_controller"])

app.add_url_rule(routes["produto_route"],view_func=routes["produto_controller"])

app.add_url_rule(routes["delete_route"],view_func=routes["delete_controller"])

app.add_url_rule(routes["update_route"],view_func=routes["update_controller"])

app.add_url_rule(routes["venda_route"],view_func=routes["venda_controller"])

app.add_url_rule(routes["deletevenda_route"],view_func=routes["deletevenda_controller"])

app.add_url_rule(routes["updatevenda_route"],view_func=routes["updatevenda_controller"])

app.add_url_rule(routes["compra_route"],view_func=routes["compra_controller"])

app.add_url_rule(routes["deletecompra_route"],view_func=routes["deletecompra_controller"])

app.add_url_rule(routes["updatecompra_route"],view_func=routes["updatecompra_controller"])

app.register_error_handler(routes["notfound_route"],routes["notfound_controller"])