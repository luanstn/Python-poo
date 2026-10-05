
class pessoa:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


class pessoas:
    def __init__(self, nome):
        self.__nome = nome

    def get_pessoa(self):
        return self.__nome

pes2 = pessoas("luan")
print(pes2.get_pessoa())

pes1 = pessoa("rafael")
print(pes1.nome)

"como usa o setter em property"

class pessoa:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if valor != "":
            self.__nome = valor

pes1 = pessoa("rafael")
pes1.nome = "luan"

print(pes1.nome)