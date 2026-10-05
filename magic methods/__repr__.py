class livro:
    def __init__(self, titulo, autor, ano):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def ano(self):
        return self.__ano

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.ano})"

    def __repr__(self):
        return f"livro({self.titulo}, {self.autor}, {self.ano})"

l1 = livro("harry potter", "j.k", 2003)

print(l1)
print([l1])