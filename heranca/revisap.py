from abc import ABC, abstractmethod

class funcionario(ABC):
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    @property
    def nome(self):
        return self.__nome

    @property
    def salario(self):
        return self.__salario

    @abstractmethod
    def calcular_pagamento(self):
        pass

    def mostrar_dados(self):
        print(f"Nome: {self.__nome}\nSalário: {self.__salario}")

class gerente(funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.__bonus = bonus

    @property
    def bonus(self):
        return self.__bonus

    def calcular_pagamento(self):
        pagamento = self.salario + self.bonus
        return pagamento

    def mostrar_dados(self):
        print(f"Nome: {self.nome}\nSalário: {self.salario} \nBônus: {self.bonus}")

class programador(funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.__bonus = bonus

    @property
    def bonus(self):
        return self.__bonus

    def calcular_pagamento(self):
        pagamento = self.salario + self.bonus
        return pagamento

    def mostrar_dados(self):
        print(f"Nome: {self.nome}\nSalário: {self.salario} \nBônus : {self.bonus}")

class empresa:
    def __init__(self, nome):
        self.__nome = nome
        self.__lista = []

    def lista(self):
        return self.__lista

    def adicionar_funcionario(self, funcionario):
        self.__lista.append(funcionario)
        print("Adicionado!")

    def listar_funcionarios(self):
        for c in self.__lista:
            print(f"nome: {c.nome}")


f1 = programador("luan", 1000, 250)
f1.mostrar_dados()

f2 = gerente("rafael", 2000, 500)
f2.mostrar_dados()

lista = [f1, f2]
for c in lista:
    print(f"{c.nome}: R$ {c.calcular_pagamento()}")

e1 = empresa("Honda")
e1.adicionar_funcionario(f1)
e1.adicionar_funcionario(f2)

e1.listar_funcionarios()