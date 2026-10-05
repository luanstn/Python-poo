"""
class professor:
    def __init__(self, professor, materia):
        self.__professor = professor
        self.__materia = materia

    @property
    def professor(self):
        return self.__professor

    @property
    def materia(self):
        return self.__materia


class turma:
    def __init__(self, nome):
        self.__nome = nome
        self.__lista = []

    @property
    def nome(self):
        return self.__nome

    @property
    def lista(self):
        return self.__lista

    def add_prof(self, professor):
        for c in self.__lista:
            if c.nome == professor.nome:
                print("existe")
                break
        else:
            self.__lista.append(professor)

    def listar(self):
        for c in self.__lista:
            print(c.professor)

    def procurar_prof(self, nome):
        for c in self.__lista:
            if c.professor == nome:
                print("foi encontrado com sucesso")
                break
        else:
            print("não foi encontrado")

    def total_professores(self):
        total = 0
        for c in self.__lista:
            total = total + 1

        return total

p1 = professor("João", "Matemática")

t1 = turma("3º Ano")

t1.add_prof(p1)

t1.listar()

print("Total:", t1.total_professores())

t1.procurar_prof("Maria")

"""
"""
class livro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor


class usuario:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

class emprestimo:
    def __init__(self, usuario, livro):
        self.usuario = usuario
        self.livro = livro

    def mostrar(self):
        print(f"{self.usuario.nome} \n{self.livro.titulo} \n{self.livro.autor}")

l1 = livro("harry potter", "j.k.")
u1 = usuario("luan")

e1 = emprestimo(u1, l1)
e1.mostrar()
"""

class cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

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

class pedido:
    def __init__(self, cliente, produto):
        self.__cliente = cliente
        self.__produto = produto

    @property
    def cliente(self):
        return self.__cliente

    @property
    def produto(self):
        return self.__produto

    def mostrar(self):
        print(f"cliente: {self.cliente.nome} \nproduto: {self.produto.nome} \nvalor: {self.produto.preco}")

class loja:
    def __init__(self):
        self.__lista = []

    @property
    def lista(self):
        return self.__lista

    def adicionar_pedido(self, pedido):
        self.__lista.append(pedido)

    def lista_pedido(self):
        for c in self.__lista:
            print(f"cliente: {c.cliente.nome} \nproduto: {c.produto.nome} \nvalor: {c.produto.preco}")

    def buscar_cliente(self, nome):
        for c in self.__lista:
            if c.cliente.nome == nome:
                print(f"cliente: {c.cliente.nome} \nproduto: {c.produto.nome} \nvalor: {c.produto.preco}")
                break
        else:
            print("não encontrado")

    def total_pedidos_cliente(self, nome):
        total = 0
        for c in self.__lista:
            if c.cliente.nome == nome:
                total = total + 1
        if total > 0:
            return total

        else:
            return 0

    def remover_pedidos_lista(self, nome):
        for c in self.__lista:
            if c.cliente.nome == nome:
                self.__lista.remove(c)
                break
        else:
            print("não encontrado")

    def remover_todos(self, nome):
        novalista = []
        for c in self.__lista:
            if c.cliente.nome != nome:
                novalista.append(c)

        self.__lista = novalista

    def total_valor(self):
        total = 0
        for c in self.__lista:
            total = total + c.produto.preco

        return total





c1 = cliente("luan")
c2 = cliente("rafael")

p1 = produto("iphone 12", 2600)
p2 = produto("samsung s20", 2800)

pe1 = pedido(c1, p1)
pe2 = pedido(c2, p2)
pe3 = pedido(c1, p2)

l1 = loja()

l1.adicionar_pedido(pe1)
l1.adicionar_pedido(pe2)
l1.adicionar_pedido(pe3)

l1.buscar_cliente("luan")

print(l1.total_pedidos_cliente("luan"))

l1.remover_pedidos_lista("rafael")

print(l1.total_valor())





