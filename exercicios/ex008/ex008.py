class gamer:
    def __init__(self,nome,nick):
        self.nome = nome
        self.nick = nick

        self.lista = list()

    def add_favoritos(self,jogos):
        self.jogos = jogos
        self.lista.append(self.jogos)

    def ficha(self):
        print(f"jogador {self.nick}")
        print(f"nome real: {self.nick}")
        print("jogos favoritos: \n")
        for c in self.lista:
            print(c)


j1 = gamer("Luan santana", "Luanzin")
j1.add_favoritos("mario bros")
j1.add_favoritos("carros")
j1.add_favoritos("far cry")
j1.ficha()