#NOVO EXERCÍCIO — Sistema de Biblioteca
#ENCAPSULAMENTO + CONTROLE DE ESTADO

class livro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__emprestado = False

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
        if self.__emprestado == False:
            self.__emprestado = True
            print("emprestado com sucesso")
        else:
            print("esse livro foi emprestado")

l1 = livro("ponte para terabítia","desconhecido")

l1.emprestar()
