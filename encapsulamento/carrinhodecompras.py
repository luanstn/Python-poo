class produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

class itemcarrinho:
    def __init__(self, produto, quantidade):
        self.__produto = produto
        self.__quantidade = quantidade

    @property
    def produto(self):
        return self.__produto

    @property
    def quantidade(self):
        return self.__quantidade


class carrinho:
    def __init__(self):
        self.__lista = []

    @property
    def lista(self):
        return self.__lista

    def addproduto(self, produto, quantidade):
        for c in self.__lista:
             if c.produto.nome == produto.nome:
                 c.quantidade = c.quantidade + quantidade
                 break
        else:
            item = itemcarrinho(produto, quantidade)
            self.__lista.append(item)

    def remover_produto(self,produto):
        for c in self.lista:
            if c.produto.nome == produto:
                self.__lista.remove(c)
                break
        else:
            print("produto não existe")


    def calcular(self):
        total = 0
        for c in self.__lista:
            total = total + (c.produto.preco * c.quantidade)

        return total

    def listar_carrinho(self):
        for c in self.__lista:
            print(f"produto: {c.produto.nome} | preço: {c.produto.preco} | quantidade: {c.quantidade} | total: {print(self.calcular)}")

p1 = produto("Celular", 1000)
p2 = produto("Fone", 200)

carrinho = carrinho()

carrinho.addproduto(p1, 2)
carrinho.addproduto(p2, 1)

carrinho.listar_carrinho()
carrinho.calcular()
carrinho.listar_carrinho()




