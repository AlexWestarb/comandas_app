from flask import Blueprint, render_template, request, redirect, url_for

bp_login = Blueprint('login', __name__, url_prefix='/', template_folder='templates')

@bp_login.route("/", methods=['GET', 'POST'])
def login():
    return render_template("formLogin.html")

@bp_login.route('/login', methods=['POST'])
def validaLogin():
    try:
        # dados enviados via FORM
        cpf = request.form['usuario']
        senha = request.form['senha']
        
        if (cpf == "abc" and senha == 'bBolinhas'):
            # abre a aplicação na tela home
            return redirect(url_for('index.formIndex'))
        else:
            raise Exception("Falha de Login! Verifique seus dados e tente novamente!")
    except Exception as e:
        # retorna para a tela de login
        return redirect(url_for('login.login', msgErro=e.args[0]))