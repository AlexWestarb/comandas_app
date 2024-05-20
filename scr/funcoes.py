from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # hash da senha do usuário

class Funcoes(object):

    @staticmethod
    def verify_password(plain_password, password):
        return pwd_context.verify(plain_password, password)

    # sempre gera um hash diferente, mas o método verify criado na API consegue comparar 
    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)
    
    @staticmethod
    def cifraSenha(senha):
        return Funcoes.get_password_hash(senha)