from flask import Blueprint, render_template, request, redirect, url_for, jsonify
import requests
from settings import getHeadersAPI, ENDPOINT_FUNCIONARIO

bp_funcionario = Blueprint('funcionario', __name__, url_prefix="/funcionario", template_folder='templates')

''' rotas dos formulários '''

@bp_funcionario.route('/', methods=['GET', 'POST'])
def formListaFuncionario():
    try:
        response = requests.get(ENDPOINT_FUNCIONARIO, headers=getHeadersAPI())
        result = response.json()
        
        print(result) # para teste
        print(response.status_code) # para teste
        
        if (response.status_code != 200):
            raise Exception(result)
        
        return render_template('formListaFuncionario.html', result=result[0])
    except Exception as e:
        return render_template('formListaFuncionario.html', msgErro=e.args[0])

@bp_funcionario.route('/form-funcionario/', methods=['POST'])
def formFuncionario():
    return render_template('formFuncionario.html')