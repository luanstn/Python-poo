class funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    @property
    def nome(self):
        return self.__nome

    @property
    def salario(self):
        return self.__salario

    def trabalhar(self):
        print(f"{self.__nome} está trabalhando")

    def mostrar_dados(self):
        print(f"nome: {self.__nome} \nsalario: {self.__salario}")

class programador(funcionario):
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.__linguagem = linguagem

    @property
    def linguagem(self):
        return self.__linguagem

    def trabalhar(self):
        print(f"{self.nome} está programando em {self.__linguagem}")

class designer(funcionario):
    def __init__(self, nome, salario, ferramenta):
        super().__init__(nome, salario)
        self.__ferramenta = ferramenta

    @property
    def ferramenta(self):
        return self.__ferramenta

    def trabalhar(self):
        super().trabalhar()
        print(f"{self.nome} está usando {self.__ferramenta}")


p1 = programador("luan", 3000, "python")
d1 = designer("rafael", 3100, "canva")

lista = [p1, d1]

for c in lista:
    c.trabalhar()


