class produto:
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor


    @property
    def nome(self):
        return self.__nome

    @property
    def valor(self):
        return self.__valor

    @property
    def quantidade(self):
        return self.__quantidade


class carrinho:
    def __init__(self):
        self.__lista = []

    @property
    def lista(self):
        return self.__lista

    def adicionar_produto(self, produto):
        self.lista.append(produto)

    def remover_produto(self, produto):
        for c in self.lista:
            if produto == c:
                self.lista.remove(c)
                print("produto removido")
                return
        else:
            print("não encontrado")

    def listar(self):
        for c in self.lista:
            print(f"produto: {c.nome} \nvalor: {c.valor}")

    def calcular_total(self):
        total = 0
        for c in self.lista:
            total = total + c.valor

        print(f"valor total: {total}")

    def __len__(self):
        return len(self.__lista)

    def __contains__(self, item):
        for c in self.lista:
            if c.nome == item:
                return True

        return False

p1 = produto("arroz", 20)
p2 = produto("feijão", 12)
p3 = produto("macarrão", 8)

c1 = carrinho()
c1.adicionar_produto(p1)
c1.adicionar_produto(p2)

print("arroz" in c1)