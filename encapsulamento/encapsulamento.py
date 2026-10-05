"""
class funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario


class gerente(funcionario):
    def __init__(self,nome,salario):
        super().__init__(nome, salario)

    def Calcular_Bonus(self):
        return self.salario + 500


class estagiario(funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def Calcular_Bonus(self):
       return self.salario + 500

g1 = gerente("Luan", 2000)
e1 = estagiario("Rafael", 1500)

g1.Calcular_Bonus()
e1.Calcular_Bonus()
"""

class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco

    def get_preco(self):
        return self.__preco

    def set_preco(self,valor):
        if valor > 0:
            self.__preco = valor
        else:
            print("o preço está inválido")

p = produto("notebook", 2400)

p.set_preco(2000)
p.set_preco(-100)

print(p.get_preco())