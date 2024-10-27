import datetime

class DiaSemana:
    # Definindo constantes para os dias da semana
    SEGUNDA = 0
    TERCA = 1
    QUARTA = 2
    QUINTA = 3
    SEXTA = 4
    SABADO = 5
    DOMINGO = 6

class Destinatario():
    nome     = None,
    numero   = None,
    mensagem = "",

    def __init__(self, nome = None, numero = "", mensagem = None, data_encontro = DiaSemana.DOMINGO):
        self.nome           = nome,
        self.numero         = numero,
        self.mensagem       = mensagem
        self.data_encontro  = data_encontro

class Mensagem():
    destinatario = Destinatario()   

    def days_counter(self):
        agora = datetime.datetime.now().weekday()
        dias_restantes = self.destinatario.data_encontro - agora

        if dias_restantes < 0:
            dias_restantes += 7

        return dias_restantes
    
    def build_message(self):
        dias_restantes = self.days_counter()
        return f"Faltam {dias_restantes} dias para te encontrar"

