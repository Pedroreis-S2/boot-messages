from manager_api import ApiManager
from manager_message import Destinatario

def execute():
    destinatario = Destinatario()
    mensagem = destinatario.build_message()

    api_manager = ApiManager(destinatario, mensagem)
    
    if not api_manager.check_connection():
        print("Erro ao conectar com a API")
        return False

    if not api_manager.send_message():
        print("Erro ao enviar mensagem")
        return False
    
    return True