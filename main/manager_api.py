import os
from dotenv import load_dotenv

class ApiManager():
    
    @classmethod
    def coleta_numero_api(cls, nome_chave):
        load_dotenv()
        return os.getenv(nome_chave)
