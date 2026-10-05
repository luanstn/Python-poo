class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco

    def get_preco(self):
        return self.__preco

    def aplica_desconto(self,percentual=0):
        if percentual <= 100 and percentual >= 0:
            desconto = self.__preco * (percentual / 100)
            self.__preco = self.__preco - desconto
            if self.__preco > 0:
                return self.__preco
            else:
                return "valor inválido"

p = produto("celular", 2000)
print(p.aplica_desconto(10))