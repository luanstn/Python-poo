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
    def __init__(self, nome, id):
        self.__nome = nome
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @property
    def id(self):
        return self.__id

class biblioteca:
    def __init__(self):
        self.__biblioteca = []

    @property
    def lista(self):
        return self.__biblioteca

    def adicionar_livro(self, livro):
        self.__biblioteca.append(livro)

    def remover_livro(self, livro):
        if livro in self.__biblioteca:
            self.__biblioteca.remove(livro)
        else:
            print("livro não encontrado")

class emprestimo:
    def __init__(self, usuario, livro):
        self.usuario = usuario
        self.livro = livro

usuario1 = usuario("luan", 1212)
livro1 = livro("harry potter", "J.K.")
b1 = biblioteca()

b1.adicionar_livro(livro1)
b1.remover_livro(livro1)

e1 = emprestimo(usuario1, livro1)
"""
"""
class pessoa:
    def __init__(self, usuario):
        self.__usuario = usuario

    @property
    def usuario(self):
        return self.__usuario

class celular:
    def __init__(self, pessoa):
        self.__pessoa = pessoa

    @property
    def pessoa(self):
        return self.__pessoa

    def mostrar_dono(self):
        print(f"Dono: {self.pessoa.usuario}")

p1 = pessoa("luan")
c1 = celular(p1)

c1.mostrar_dono()

"""
"""
class aluno:
    def __init__(self, aluno, matricula):
        self.__aluno = aluno
        self.__matricula = matricula

    @property
    def aluno(self):
        return self.__aluno

    @property
    def matricula(self):
        return self.__matricula

class curso:
    def __init__(self, aluno):
        self.__aluno = aluno

    @property
    def aluno(self):
        return self.__aluno

    def mostrar(self):
        print(f"aluno: {self.aluno.aluno} matricula: {self.aluno.matricula}")

a1 = aluno("luan", "02929")
c1 = curso(a1)

c1.mostrar()
"""
"""

class cliente:
    def __init__(self, nome, id):
        self.__nome = nome
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @property
    def id(self):
        return self.__id

class produto:
    def __init__(self, produto, valor):
        self.__produto = produto
        self.__valor = valor

    @property
    def produto(self):
        return self.__produto

    @property
    def valor(self):
        return self.__valor


class pedido:
    def __init__(self, cliente, produto):
        self.__cliente = cliente
        self.__produto = produto

    @property
    def produto(self):
        return self.__produto

    @property
    def cliente(self):
        return self.__cliente

    def mostrar(self):
        print(f"Cliente: {self.cliente.nome}    id do cliente: {self.cliente.id}")
        print(f"produto: {self.produto.produto}    valor do produto: {self.produto.valor}")

class loja:
    def __init__(self):
        self.__listaprodutos = []

    @property
    def lista(self):
        return self.__listaprodutos

    def adicionar(self, pedido):
        self.__listaprodutos.append(pedido)
        print("pedido adicionado")

    def remover(self, pedido):
        if pedido in self.__listaprodutos:
            self.__listaprodutos.remove(pedido)
            print("produto removido")
        else:
            print("não encontrado")




c1 = cliente("luan", 2552)
p1 = produto("celular", 1700)

pe1 = pedido(c1, p1)
pe1.mostrar()

loja1 = loja()

loja1.adicionar(pe1)
loja1.remover(pe1)

"""