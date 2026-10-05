class funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario

    def get_salario(self):
        return self.__salario

    def set_salario(self, valor):
        if valor >= 0:
            self.__salario = valor
        else:
            print("o valor tem que ser positivo")

class gerente(funcionario):
    def __init__(self,nome,salario):
        super().__init__(nome, salario)

    def Calcular_Bonus(self):
        return self.get_salario() + 1000


class estagiario(funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def Calcular_Bonus(self):
       return self.get_salario() + 500

g1 = gerente("Luan", 2000)
e1 = estagiario("Rafael", 1500)

print(g1.Calcular_Bonus())
print(e1.Calcular_Bonus())
