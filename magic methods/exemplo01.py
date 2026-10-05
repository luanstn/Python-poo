class livro:
    def __init__(self, titulo, autor, num_pages):
        self.__titulo = titulo
        self.__autor = autor
        self.__num_pages = num_pages

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def num_pages(self):
        return self.__num_pages

    def __str__(self):
        return f"livro {self.titulo} de {self.autor}"

l1 = livro("O hobbit", "J.R.R Tolkien", 310)
l2 = livro("harry potter", "J.K. Rowling", 322)
l3 = livro("O rei leão", "não sei", 110)

print(l1)

