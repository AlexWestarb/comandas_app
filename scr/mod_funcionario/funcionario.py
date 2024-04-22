from flask import Blueprint, render_template

bp_funcionario = Blueprint('funcionario', __name__, url_prefix="/funcionario", template_folder='templates')

''' rotas dos formulários '''

@bp_funcionario.route('/')
def formListaFuncionario():
    return render_template('formListaFuncionario.html'), 200

'''
Rota antiga de app...
@app.route('/funcionario/')
def formListaFuncionario():
# return "<h1>Rota da página de Funcionários da nossa WEB APP</h1>", 200
return render_template('formListaFuncionario.html'), 200
'''