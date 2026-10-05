class jogador:
    def __init__(self, nome, pontuacao):
        self.__nome = nome
        self.__pontuacao = pontuacao

    @property
    def nome(self):
        return self.__nome

    @property
    def pontuacao(self):
        return self.__pontuacao

    def __gt__(self, outro):
        return self.pontuacao > outro.pontuacao

j1 = jogador("luan", 2022)
j2 = jogador("rafael", 1900)

print(j1 > j2)