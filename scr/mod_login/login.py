from functools import wraps
from flask import Blueprint, render_template, request, redirect, url_for, session
import requests
from settings import ENDPOINT_TOKEN
from datetime import datetime, timedelta

bp_login = Blueprint('login', __name__, url_prefix='/', template_folder='templates')

@bp_login.route("/", methods=['GET', 'POST'])
def login():
    return render_template("formLogin.html")

@bp_login.route('/login', methods=['POST'])
def validaLogin():
    try:
        session.clear()
        
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'username': request.form['usuario'],
            'password': request.form['senha'],
            'grant_type': '', 'scope': '', 'client_id': '', 'client_secret': ''
        }
        response = requests.post(ENDPOINT_TOKEN, headers=headers, data=data)
        access_token = response.json()

        print("Antes de imprimir o access_token")
        print(access_token)
        print(type(access_token))
        print(access_token.keys())
        
        if (response.status_code != 200):
            raise Exception(access_token)

        # registra os dados do token e do usuário na sessão, armazenando o login do usuário
        session['access_token'] = access_token['access_token']
        session['expire_minutes'] = access_token['expires_in']
        session['token_type'] = access_token['token_type']
        session['token_validade'] = datetime.timestamp( datetime.now() + timedelta(minutes=access_token['expires_in']) )

        ### futuramente alterar a api para retornar os dados do usuário
        session['nome'] = request.form['usuario']
        session['login'] = request.form['usuario']
        session['grupo'] = "1"

        # abre a aplicação na tela home
        return redirect(url_for('index.formIndex'))
    except Exception as e:
        # retorna para a tela de login
        return redirect(url_for('login.login', msgErro=e.args[0], msgException=e.args[0]))

@bp_login.route("/logoff", methods=['GET'])
def logoff():
    # limpa um valor individual
    session.pop('login', None)
    
    # limpa toda sessão
    session.clear()
    
    # retorna para a tela de login
    return redirect(url_for('login.login'))

# valida se o token esta na sessão e se ainda é 
def validaToken(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
    
        if 'token_validade' in session and session['token_validade'] > datetime.timestamp( datetime.now() ):
            
            # retorna os dados copiados da função original
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login.login', msgErro='Usuário não logado! Token expirado!'))
    # retorna o resultado do if acima
    return decorated_function