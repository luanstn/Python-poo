class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.__idade = idade

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        if idade >= 0 and idade < 120:
            self.__idade = idade
        else:
            print("idade inválida")

p = pessoa("luan", 22)

p.set_idade(22)

print(p.get_idade())