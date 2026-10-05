class funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario


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
