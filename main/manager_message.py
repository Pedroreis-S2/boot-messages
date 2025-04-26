import datetime
import os
class Destinatario():
    nome = os.getenv('NOMEENVIO')
    numero = os.getenv('NUMEROENVIO')
    pass

    def build_message(self):
        data = (datetime.datetime.now() - datetime.timedelta(hours=3)).strftime("%d/%m/%Y")
        mensagem = f"Bom dia {self.nome},\n\nHoje é {data} e você está recebendo esta mensagem de teste.\n\nAtenciosamente,\nAmor da sua vida" 
        return mensagem

