class funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario

    def get_salario(self):
        return self.__salario


class gerente(funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcula_gerente(self):
        return self.get_salario() + 500

class estagiario(funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcula_func(self):
       return self.get_salario() + 250

ger1 = gerente("luan", 2500)
est1 = estagiario("rafael", 1500)

print(ger1.calcula_gerente())
print(est1.calcula_func())

