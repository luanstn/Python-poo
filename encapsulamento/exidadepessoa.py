class pessoa:
    def __init__(self, nome, dia, mes, ano, altura):
        self.nome = nome
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
        self.altura = altura

    def get_dia(self):
        return self.__dia

    def get_mes(self):
        return self.__mes

    def get_nascimento(self):
        return self.__ano

    def set_idade(self, valor):
        if valor >= 1950 and valor <= 2026:
            self.__ano = valor
        else:
            print("valor inválido")

    def dados(self):
            print(f"nome: {self.nome} \nnascimento: {self.get_dia()}/{self.get_mes()}/{self.get_nascimento()} \naltura: {self.altura}")

    def calcula_idade(self):
        idade = 2026 - self.get_nascimento()
        print(idade)

p1 = pessoa("luan", 25, 6, 2003, 1.83)
p1.dados()
p1.calcula_idade()