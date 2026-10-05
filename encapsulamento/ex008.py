class aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.__nota = nota

    def get_nota(self):
        return self.__nota

    def set_nota(self, valor):
        if valor > 0 and valor <= 10:
            self.__nota = valor
        else:
            print("valor inválido")

    def aprovado(self):
        if self.get_nota() >= 7:
            print(f" {self.nome}, {self.__nota} ")
            return True
        else:
            return False

a1 = aluno("luan", 2)

a1.set_nota(9)

print(a1.aprovado())
