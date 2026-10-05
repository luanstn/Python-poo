class carrinho:
    def __init__(self):
        self.__lista = []

    @property
    def lista(self):
        return self.__lista

    def adicionar_produto(self, produto):
        self.__lista.append(produto)
        print("produto adicionado com sucesso")

    def __getitem__(self, indice):
        return self.lista[indice]

    def __contains__(self, item):
        return item in self.__lista

c1 = carrinho()
c1.adicionar_produto("teclado")
c1.adicionar_produto("celular")
c1.adicionar_produto("fone")

print("teclado" in c1)
print("mouse" in c1)