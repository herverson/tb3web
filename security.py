from werkzeug.security import safe_str_cmp
from modelos.user import UserModel

def authenticate(username, password):
    user = UserModel.encontrar_por_nome(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.encontrar_por_id(user_id)

