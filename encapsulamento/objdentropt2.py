"""
class usuario:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

class livro:
    def __init__(self, autor, titulo):
        self.__autor = autor
        self.__titulo = titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def titulo(self):
        return self.__titulo

class emprestimo:
    def __init__(self, usuario, livro):
        self.__usuario = usuario
        self.__livro = livro

    @property
    def usuario(self):
        return self.__usuario

    @property
    def livro(self):
        return self.__livro

class biblioteca:
    def __init__(self):
        self.__lista = []

    @property
    def lista(self):
        return self.__lista

    def adicionar(self, livro):
        self.__lista.append(livro)
        print("adicionado")

    def listar_emprestimos(self):
        for c in self.__lista:
            print(f"{c.usuario.nome} pegou o livro {c.livro.titulo} ({c.livro.autor})")

    def buscar_usuario(self, nome):
        for c in self.__lista:
            if c.usuario.nome == nome:
                print(f"{c.usuario.nome}, {c.livro.titulo} ({c.livro.autor})")

    def contar_emprestimo(self, nome):
        cont = 0
        for c in self.__lista:
            if c.usuario.nome == nome:
               cont = cont + 1
        if cont > 0:
            print(f"fez o total de {cont} empréstimo")
        else:
            print("não fez nenhum empréstimo")
    def verificar_livro_emprestado(self, livro):
        for c in self.__lista:
            if c.livro.titulo == livro:
                print("Este livro foi emprestado")
                break
        else:
            print("o livro não foi emprestado")

u1 = usuario("luan")
l1 = livro( "j.k.", "harry potter")

e1 = emprestimo(u1, l1)

b1 = biblioteca()

b1.adicionar(e1)

b1.listar_emprestimos()

b1.buscar_usuario("luan")

b1.contar_emprestimo("luan")

b1.verificar_livro_emprestado("harry potter")

"""
"""
class jogador:
    def __init__(self, nome, gols):
        self.__nome = nome
        self.__gols = gols

    @property
    def nome(self):
        return self.__nome

    @property
    def gols(self):
        return self.__gols

    def gol(self):
        self.__gols = self.__gols + 1

class time:
    def __init__(self, nome):
        self.__nome = nome
        self.__lista = []

    @property
    def nome(self):
        return self.__nome

    @property
    def lista(self):
        return self.__lista

    def adicionar_jogador(self, jogador):
        for c in self.__lista:
            if c.nome == jogador.nome:
                print(f"jogador já existente")
                break
        else:
            self.__lista.append(jogador)

    def listar_jogadores(self):
        for c in self.__lista:
            print(f"nome: {c.nome} gols: {c.gols}")

    def fazer_gol(self, nome):
        for c in self.__lista:
            if c.nome == nome:
                c.gol()
                break

    def soma_todos_gols(self):
        total = 0
        for c in self.__lista:
            total = total + c.gols

        print(total)

    def jogador_mais_gols(self):
        if self.__lista:
            melhor = self.__lista[0]
            for c in self.__lista:
                if c.gols > melhor.gols:
                    melhor = c

            print(f"o artilheiro é: {melhor.nome} com {melhor.gols}")


j1 = jogador("luan", 5)
j2 = jogador("rafael", 3)

t1 = time("flamengo")

t1.adicionar_jogador(j1)
t1.adicionar_jogador(j2)

t1.listar_jogadores()

t1.fazer_gol("luan")

t1.listar_jogadores()

"""

class filme:
    def __init__(self, nome, duracao):
        self.__nome = nome
        self.__duracao = duracao

    @property
    def nome(self):
        return self.__nome

    @property
    def duracao(self):
        return self.__duracao

class usuario:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


class assistir:
    def __init__(self, usuario, filme):
        self.__usuario = usuario
        self.__filme = filme
        self.__minutos = 0

    @property
    def usuario(self):
        return self.__usuario

    @property
    def filme(self):
        return self.__filme

    @property
    def minutos(self):
        return self.__minutos

    def aumentar_minutos(self, valor):
        if self.filme.duracao >= self.__minutos + valor:
            self.__minutos = self.__minutos + valor
        else:
            print("você já assistiu")

class plataforma:
    def __init__(self):
        self.__lista_ep = []

    @property
    def lista(self):
        return self.__lista_ep

    def adicionar_assistido(self, objeto):
        self.__lista_ep.append(objeto)
        print("adicionado com sucesso!")

    def listar_assistidos(self):
        for c in self.__lista_ep:
            print(f"assistido: {c.filme.nome}")

    def buscar_usuario(self, nome):
        for c in self.__lista_ep:
            if c.usuario.nome == nome:
                print("usuário encontrado")
                break
        else:
            print("usuario não encontrado")

    def total_minutos_usuario(self, nome):
        for c in self.__lista_ep:
            if c.usuario.nome == nome:
                print(f"total assistidos: {c.minutos}")

    def mais_assistido(self):
        mais_assistido = self.__lista_ep[0]
        for c in self.__lista_ep:
            if c.minutos > mais_assistido.minutos:
                mais_assistido = c

        print(f"mais assistido: {mais_assistido.filme.nome}")

    def finalizar_filme(self, usuario, filme):
        for c in self.__lista_ep:
            if c.usuario.nome == usuario and c.filme.nome == filme:
                self.__lista_ep.remove(c)
                print("removido com sucesso")
                break
        else:
            print("nenhum com esses dados encontrado")


f1 = filme("the big bang", 60)

u1 = usuario("luan")

a1 = assistir(u1, f1)
a1.aumentar_minutos(20)

p1 = plataforma()

p1.adicionar_assistido(a1)
p1.listar_assistidos()
p1.buscar_usuario("luan")
p1.total_minutos_usuario("luan")

p1.mais_assistido()
p1.finalizar_filme("luan", "the big bang")


