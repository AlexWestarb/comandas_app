from flask import Blueprint, render_template, request, redirect, url_for, jsonify
import requests
from settings import getHeadersAPI, ENDPOINT_CLIENTE

bp_cliente = Blueprint('cliente', __name__, url_prefix="/cliente", template_folder='templates')

''' rotas dos formulários '''

@bp_cliente.route('/', methods=['GET', 'POST'])
def formListaCliente():
    try:
        response = requests.get(ENDPOINT_CLIENTE, headers=getHeadersAPI())
        result = response.json()
        
        print(result) # para teste
        print(response.status_code) # para teste
        
        if (response.status_code != 200):
            raise Exception(result)
        
        return render_template('formListaCliente.html', result=result[0])
    except Exception as e:
        return render_template('formListaCliente.html', msgErro=e.args[0])

@bp_cliente.route('/form-cliente/', methods=['POST'])
def formCliente():
    return render_template('formCliente.html')