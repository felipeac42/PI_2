from src.controllers.controller import *
from src.controllers.errors import *

routes = {
    "index_route":"/","index_controller":IndexController.as_view("index"),
    "produto_route":"/produto","produto_controller":ProdutoController.as_view("produto"),
    "delete_route":"/delete/produto/<int:id>","delete_controller":DeleteProdutoController.as_view("delete"),
    "update_route":"/update/produto/<int:id>","update_controller":UpdateProdutoController.as_view("update"),
    "venda_route":"/venda","venda_controller":VendaController.as_view("venda"),
    "deletevenda_route":"/delete/venda/<int:id>","deletevenda_controller":DeleteVendaController.as_view("deletevenda"),
    "updatevenda_route":"/update/venda/<int:id>","updatevenda_controller":UpdateVendaController.as_view("updatevenda"),
    "compra_route":"/compra","compra_controller":CompraController.as_view("compra"),
    "deletecompra_route":"/delete/compra/<int:id>","deletecompra_controller":DeleteCompraController.as_view("deletecompra"),
    "updatecompra_route":"/update/compra/<int:id>","updatecompra_controller":UpdateCompraController.as_view("updatecompra"),
    "notfound_route":404,"notfound_controller":NotFoundController.as_view("notfound"),
}
