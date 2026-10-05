class livro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponibilidade = True

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def disponibilidade(self):
        return self.__disponibilidade

    def troca_disp(self):
        self.__disponibilidade = not self.__disponibilidade

    def ver_disp(self):
        print(self.disponibilidade)

    def __str__(self):
        return(f"Título: {self.titulo}, autor: {self.autor}")

class usuario:
    def __init__(self, nome):
        self.__nome = nome
        self.__livros_emprestados = []

    @property
    def nome(self):
        return self.__nome

    @property
    def livros_emprestados(self):
        return self.__livros_emprestados

    def adicionar_livro(self, valor):
        self.livros_emprestados.append(valor)

    def remover_livro(self, valor):
        self.livros_emprestados.remove(valor)

    def listar_livros_pegos(self):
        print(f"nome: {self.nome}\n")
        for c in self.livros_emprestados:
            print(f"Livro: {c.titulo}\n")

class biblioteca:
    def __init__(self):
        self.__lista = []
        self.__listausuarios = []

    @property
    def lista(self):
        return self.__lista

    @property
    def listausuarios(self):
        return self.__listausuarios

    def cadastrar_livro(self, valor):
        self.lista.append(valor)

    def cadastrar_usuarios(self, valor):
        self.listausuarios.append(valor)

    def emprestar_livros(self, usuario, valor):
        if not usuario in self.listausuarios:
            print("usuário não encontrado")
            return

        if not valor in self.lista:
            print("livro não encontrado")
            return

        if valor.disponibilidade == True:
            valor.troca_disp()
            usuario.adicionar_livro(valor)
        else:
            print("livro já foi emprestado")

    def devolver_livro(self, usuario, valor):
        if valor in self.lista:
            if valor in usuario.livros_emprestados:
                if valor.disponibilidade == False:
                    valor.troca_disp()
                    usuario.remover_livro(valor)
                    print("devolvido com sucesso")
        else:
            print("esse livro não pertence a essa biblioteca")

    def verificar_livros_disp(self):
        print("livros disponíveis: ")
        for c in self.lista:
            if c.disponibilidade == True:
                print(f"Título: {c.titulo}, autor: {c.autor}")

    def verificar_livros_emprestados(self):
        print("livros emprestados: ")
        for c in self.lista:
            if c.disponibilidade == False:
                print(f"Título: {c.titulo}, autor: {c.autor}")

    def __len__(self):
        return len(self.__lista)


l1 = livro("harry potter", "j k ")
l2 = livro("senhor dos anéis", "não sei")
l3 = livro("ponte para terabitia", "não sei")

u1 = usuario("luan")

b1 = biblioteca()
b1.cadastrar_livro(l1)
b1.cadastrar_livro(l2)
b1.cadastrar_livro(l3)
b1.cadastrar_usuarios(u1)

b1.emprestar_livros(u1, l1)
b1.emprestar_livros(u1, l2)

b1.devolver_livro(u1, l1)

b1.devolver_livro(u1, l1)