from flask.views import MethodView
from flask import request, render_template, redirect
from src.db import mysql

class IndexController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("select * from estoque inner join produto on estoque.id_produto = produto.id")
            data = cur.fetchall()
            return render_template('public/index.html', data=data)

class ProdutoController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("select * from produto")
            data = cur.fetchall()
            return render_template('public/produto.html', prod=data)
    
    def post(self):
        #id = request.form['id']
        descricao = request.form['descricao']
        estoque_minimo = request.form['estoque_minimo']
        estoque_maximo = request.form['estoque_maximo']
        
        with mysql.cursor() as cur:
            cur.execute("insert into produto (descricao,estoque_minimo,estoque_maximo) values(%s,%s,%s)",(descricao,estoque_minimo,estoque_maximo))
            cur.connection.commit()
            return redirect('/produto')
        
class DeleteProdutoController (MethodView):
    def post(self, id):
        with mysql.cursor() as cur:
            cur.execute("delete from produto where id = %s",(id))
            cur.connection.commit()
            return redirect('/produto')
        
class UpdateProdutoController (MethodView):
    def get(self, id):
        with mysql.cursor() as cur:
            cur.execute("select * from produto where id = %s",(id))
            produto = cur.fetchone()
            return render_template('public/update.html',produto=produto)
    def post(self, id):
        descricao = request.form['descricao']
        estoque_minimo = request.form['estoque_minimo']
        estoque_maximo = request.form['estoque_maximo']

        with mysql.cursor() as cur:
            cur.execute("update produto set descricao = %s, estoque_minimo = %s, estoque_maximo = %s where id = %s",(descricao,estoque_minimo,estoque_maximo, id))
            cur.connection.commit()
            return redirect('/produto')

class VendaController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("select * from saida_produto inner join produto on saida_produto.id_produto = produto.id")
            data = cur.fetchall()
            cur.execute("select * from produto")
            prod = cur. fetchall()
            return render_template('public/venda.html', data=data,prod=prod)
    
    def post(self):
        id_produto = request.form['id_produto']
        qtde = request.form['qtde']
        data_saida = request.form['data_saida']
        valor_unitario = request.form['valor_unitario']
        
        with mysql.cursor() as cur:
            cur.execute("insert into saida_produto (id_produto,qtde,data_saida,valor_unitario) values(%s,%s,%s,%s)",(id_produto,qtde,data_saida,valor_unitario))
            cur.connection.commit()
            return redirect('/venda')
        
class DeleteVendaController (MethodView):
    def post(self, id):
        with mysql.cursor() as cur:
            cur.execute("delete from saida_produto where id = %s",(id))
            cur.connection.commit()
            return redirect('/venda')
        
class UpdateVendaController (MethodView):
    def get(self, id):
        with mysql.cursor() as cur:
            cur.execute("select * from saida_produto inner join produto on saida_produto.id_produto = produto.id where saida_produto.id = %s",(id))
            venda = cur.fetchone()
            cur.execute("select * from produto")
            produto = cur. fetchall()           
            return render_template('public/vendaupdate.html',venda=venda, produto=produto)
    
    def post(self, id):
        id_produto = request.form['id_produto']
        qtde = request.form['qtde']
        data_saida = request.form['data_saida']
        valor_unitario = request.form['valor_unitario']
        with mysql.cursor() as cur:
            cur.execute("update saida_produto set id_produto = %s, qtde = %s, data_saida = %s, valor_unitario = %s where id = %s",(id_produto,qtde,data_saida,valor_unitario, id))
            cur.connection.commit()
            return redirect('/venda')
        
class CompraController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("select * from entrada_produto inner join produto on entrada_produto.id_produto = produto.id")
            data = cur.fetchall()
            cur.execute("select * from produto")
            prod = cur. fetchall()
            return render_template('public/compra.html', data=data,prod=prod)
    
    def post(self):
        id_produto = request.form['id_produto']
        qtde = request.form['qtde']
        data_entrada = request.form['data_entrada']
        valor_unitario = request.form['valor_unitario']
        
        with mysql.cursor() as cur:
            cur.execute("insert into entrada_produto (id_produto,qtde,data_entrada,valor_unitario) values(%s,%s,%s,%s)",(id_produto,qtde,data_entrada,valor_unitario))
            cur.connection.commit()
            return redirect('/compra')
        
class DeleteCompraController (MethodView):
    def post(self, id):
        with mysql.cursor() as cur:
            cur.execute("delete from entrada_produto where id = %s",(id))
            cur.connection.commit()
            return redirect('/compra')
        
class UpdateCompraController (MethodView):
    def get(self, id):
        with mysql.cursor() as cur:
            cur.execute("select * from entrada_produto inner join produto on entrada_produto.id_produto = produto.id where entrada_produto.id = %s",(id))
            compra = cur.fetchone()
            cur.execute("select * from produto")
            produto = cur. fetchall()           
            return render_template('public/compraupdate.html',compra=compra, produto=produto)
    
    def post(self, id):
        id_produto = request.form['id_produto']
        qtde = request.form['qtde']
        data_entrada = request.form['data_entrada']
        valor_unitario = request.form['valor_unitario']
        with mysql.cursor() as cur:
            cur.execute("update entrada_produto set id_produto = %s, qtde = %s, data_entrada = %s, valor_unitario = %s where id = %s",(id_produto,qtde,data_entrada,valor_unitario, id))
            cur.connection.commit()
            return redirect('/compra')        