import os, requests

class ApiManager():
    base_url = os.environ.get('URLINTEGRACAO')
    token = os.environ.get('TOKEN')

    def __init__(self, destinatario, mensagem: str = None):
        self.numero_envio = destinatario
        self.mensagem = mensagem
        pass
    
    def check_connection(self):
        url = f"{self.base_url}/health"
        headers = {'Authorization': self.token}
        request = requests.get(url, headers=headers)
        print(request)
        
    

        