class playlist:
    def __init__(self, nome):
        self.__nome = nome
        self.__lista = []

    @property
    def nome(self):
        return self.__nome

    def adicionar_musica(self, musica):
        self.__lista.append(musica)

    def __len__(self):
        return len(self.__lista)

p1 = playlist("minha play")
p1.adicionar_musica("supernova")
print(len(p1))