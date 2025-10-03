# configuração do banco de dados
import firebase_admin
from firebase_admin import credentials

def config():
    # guarda a chave e analisa se ta certa
    cred = credentials.Certificate("./chave-firebase.json")

    # inicializa o app
    firebase_admin.initialize_app(cred, { 
        # qual banco de dados vamos usar  
        'databaseURL': 'https://fju-site-default-rtdb.firebaseio.com'                                     
    })