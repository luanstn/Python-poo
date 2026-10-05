from abc import ABC, abstractmethod

class midia(ABC):
    def __init__(self, titulo, ano):
        self.__titulo = titulo
        self.__ano = ano

    @property
    def titulo(self):
        return self.__titulo

    @property
    def ano(self):
        return self.__ano

    @abstractmethod
    def exibir_info(self):
        pass


class livro(midia):
    def __init__(self, titulo, ano, autor):
        super().__init__(titulo, ano)
        self.__autor = autor

    @property
    def autor(self):
        return self.__autor

    def exibir_info(self):
        print(f"titulo: {self.titulo} \nAutor: {self.autor} \nAno: {self.ano}")

class filme(midia):
    def __init__(self, titulo, ano, diretor):
        super().__init__(titulo, ano)
        self.__diretor = diretor

    @property
    def diretor(self):
        return self.__diretor

    def exibir_info(self):
        print(f"titulo: {self.titulo} \nDiretor: {self.diretor} \nAno: {self.ano}")


class biblioteca:
    def __init__(self):
        self.__lista = []

    @property
    def midias(self):
        return self.__lista

    def adicionar_midias(self, midia):
        self.__lista.append(midia)

    def listar_midia(self):
        for c in self.__lista:
            c.exibir_info()

l1 = livro("harry potter", "2003", "j.k.")
f1 = filme("ponte para terabítia", "2008", "não sei")

b1 = biblioteca()

b1.adicionar_midias(l1)
b1.adicionar_midias(f1)

b1.listar_midia()
