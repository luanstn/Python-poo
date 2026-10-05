class livro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__emprestado = True

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def emprestado(self):
        return self.__emprestado

    def emprestar(self):
        self.__emprestado = False

    def devolver(self):
        self.__emprestado = True

    def mostrar_dados(self):
        print(f"título: {self.titulo} \nautor: {self.autor}")

class usuario:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")

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

    def emprestar(self):
        if self.livro.emprestado == True:
            self.livro.emprestar()
            print(f"livro {self.livro.titulo} emprestado para {self.usuario.nome}")
        else:
            print("livro já foi emprestado")

    def devolver(self):
        if self.livro.emprestado == False:
            self.livro.devolver()
            print(f"livro {self.livro.titulo} devolvido por {self.usuario.nome}")
        else:
            print("esse livro não foi emprestado")

l1 = livro("harry potter", "J.K.")
u1 = usuario("Luan santana")

e1 = emprestimo(u1, l1)

e1.emprestar()
e1.emprestar()
e1.devolver()
