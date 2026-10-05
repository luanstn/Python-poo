class produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @property
    def quantidade(self):
        return self.__quantidade

    def __str__(self):
        return f"produto: {self.nome} | preço: {self.preco} | quantidade: {self.quantidade}"

p1 = produto("teclado", 220, 2)

print(p1)