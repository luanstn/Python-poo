class livro:
    def __init__(self, titulo, paginas = 0):
        self.titulo = titulo
        self.paginas = paginas

        self.pagina_atual = 1
        print(f"você acabou de abrir o livro {self.titulo} que tem o total de {self.paginas} páginas\nvocê agora está na página 1")

    def avancar_paginas(self, quantidade):
        print ("estamos na página ", end="")

        for c in range(quantidade):
            if self.pagina_atual < self.paginas:
                self.pagina_atual = + self.pagina_atual + 1
                print(f"{self.pagina_atual}", end = "...")
            else:
                print(f"\nvocê chegou ao final do livro {self.titulo}")
                break

        if self.pagina_atual < self.paginas:
            self.identificador_paginas(quantidade)

    def identificador_paginas(self,quantidade):
        print(f"você avançou {quantidade} páginas e agora está na página {self.pagina_atual}")

l1 = livro("harry potter", 20)
l1.avancar_paginas(10)
l1.avancar_paginas(3)
l1.avancar_paginas(20)