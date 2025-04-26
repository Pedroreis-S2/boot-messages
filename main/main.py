from manager_message import Destinatario, DiaSemana, Mensagem
from manager_api import ApiManager

# alias execute="python main/main.py"
numero = ApiManager.coleta_numero_api("AMOR")
destinatario = Destinatario("Amor", numero, "", DiaSemana.DOMINGO)
mensagem_manager = Mensagem()
mensagem_manager.destinatario = destinatario
mensagem = mensagem_manager.build_message()

print(mensagem)