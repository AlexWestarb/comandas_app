from flask import Flask
from settings import HOST, PORT, DEBUG

# import blueprint criado
from mod_index.index import bp_index
from mod_funcionario.funcionario import bp_funcionario
from mod_cliente.cliente import bp_cliente
from mod_produto.produto import bp_produto

app = Flask(__name__)

# registro das rotas do blueprint
app.register_blueprint(bp_index)
app.register_blueprint(bp_funcionario)
app.register_blueprint(bp_cliente)
app.register_blueprint(bp_produto)

if __name__ == "__main__":
    """ Inicia o aplicativo WEB Flask """
    app.run(host=HOST, port=PORT, debug=DEBUG)