class livro:
    def __init__(self,titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.emprestado = False

    def emprestar(self):
        if self.emprestado == False:
            self.emprestado = True
            return "livro emprestado com sucesso"
        else:
            print("livro já emprestado")

    def devolver(self):
        if self.emprestado == True:
            self.emprestado = False
            return "livro devolvido"

    def __str__(self):
        if self.emprestado == False:
            return f"{self.titulo} de {self.autor} - disponível"
        else:
            return f"{self.titulo} de {self.autor} - emprestado"


l1 = livro("harry potter", "lsfj", 300)
l1.emprestar()
l1.emprestar()
print(l1)
