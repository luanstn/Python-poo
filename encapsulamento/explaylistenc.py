class musica:
    def __init__(self, nome, artista, duracao):
        self.__nome = nome
        self.__artista = artista
        self.__duracao = duracao

    @property
    def nome(self):
        return self.__nome

    @property
    def artista(self):
        return self.__artista

    @property
    def duracao(self):
        return self.__duracao


class playlist:
    def __init__(self, nome):
        self.__nome = nome
        self.__lista = []

    @property
    def nome(self):
        return self.__nome

    @property
    def lista(self):
        return self.__lista

    def adicionar_musica(self, musica):
        for m in self.__lista:
            if m.nome == musica.nome:
                self.__lista.append(musica)
                print("musica adicionada!")
            else:
                print("a música já está na sua playlist")

    def remover_musica(self, musica):
        if musica in self.__lista:
            self.__lista.remove(musica)
            print("musica removida")
        else:
            print("essa música não existe na sua playlist")

    def listar_musicas(self):
        for c in self.__lista:
            print(f"música: {c.nome} - {c.artista} ({c.duracao})")

    def duracao_total(self):
        total = 0
        for c in self.__lista:
            total = total + c.duracao
        print(f"o total de duração: {total} segundos")

m1 = musica("drake", "healing", 260)
m2 = musica("luan santana", "te esperando", 220)

p1 = playlist("favoritas")

p1.adicionar_musica(m1)
p1.adicionar_musica(m2)

p1.listar_musicas()

p1.duracao_total()