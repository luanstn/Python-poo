from abc import ABC, abstractmethod

class notificacao(ABC):
    def __init__(self, destinatario):
        self.__destinatario = destinatario

    @property
    def destinatario(self):
        return self.__destinatario

    @abstractmethod
    def enviar(self):
        pass

class email(notificacao):
    def __init__(self, destinatario, assunto):
        super().__init__(destinatario)
        self.__assunto = assunto

    @property
    def assunto(self):
        return self.__assunto

    def enviar(self):
        print(f"enviando e-mail para {self.destinatario} \nAssunto: {self.assunto}")

class sms(notificacao):
    def __init__(self, destinatario, numero):
        super().__init__(destinatario)
        self.__numero = numero

    @property
    def numero(self):
        return self.__numero

    def enviar(self):
        print(f"enviando SMS para {self.numero} \n destinatario: {self.destinatario}")

class notificacaoPush(notificacao):
    def __init__(self, destinatario, aplicativo):
        super().__init__(destinatario)
        self.__aplicativo = aplicativo

    @property
    def aplicativo(self):
        return self.__aplicativo

    def enviar(self):
        print(f"enviando notificação pelo {self.aplicativo} \ndestinatario: {self.destinatario}")

class centralNotificacoes:
    def __init__(self):
        self.__lista = []

    @property
    def lista(self):
        return self.__lista

    def add_notificacao(self, notificacao):
        self.__lista.append(notificacao)

    def enviar_todas(self):
        for c in self.__lista:
            c.enviar()


e1 = email("luan", "um assunto aí")
s1 = sms("camily", "83988881799")
a1 = notificacaoPush("rafael", "whatsapp")

c1 = centralNotificacoes()
c1.add_notificacao(e1)
c1.add_notificacao(s1)
c1.add_notificacao(a1)

c1.enviar_todas()