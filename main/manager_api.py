import os, requests

class ApiManager():
    base_url = os.environ.get('URLINTEGRACAO')
    token = os.environ.get('TOKEN')

    def __init__(self, destinatario, mensagem: str = ''):
        self.numero_envio = destinatario.numero
        self.mensagem = mensagem
        print(self.base_url, type(self.base_url))
        pass
    
    def check_connection(self):
        url = f"{self.base_url}/health"
        headers = {'Authorization': self.token}
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print("Erro ao conectar com a API")
            return False
        
        print("Conectado com sucesso")
        return True
    
    def send_message(self):
        url = f"{self.base_url}/messages/text"
        headers = {'Authorization': self.token}

        if not self.mensagem:
            print("Mensagem não encontrada")
            return False
        print(self.numero_envio, type(self.numero_envio))
        print(self.mensagem, type(self.mensagem))
        data = {
            "to": str(self.numero_envio),
            "body": self.mensagem
        }
        
        response = requests.post(url, headers=headers, json=data)
        print(response.__dict__)
        if response.status_code != 200:
            print("Erro ao enviar mensagem")
            return False
        
        print("Mensagem enviada com sucesso")
        return True
        
        
    

        