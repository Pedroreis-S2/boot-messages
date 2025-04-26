import os
from manager_message import Destinatario
from manager_api import ApiManager

# alias execute="python main/main.py"
nome_envio = os.environ.get('NOME_ENVIO')
numero = os.environ.get('NUMERO_ENVIO')

instancia = ApiManager(nome_envio, "sla")
instancia.check_connection()