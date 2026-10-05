class pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def altura(self):
        return self.__altura

    @idade.setter
    def idade(self, valor):
        if valor < 0:
            print("a idade não pode ser negativa!")
            return

        self.__idade = valor
    def aumentar_idade(self):
        self.__idade = self.idade + 1

    def mostrar(self):
        print(f"nome: {self.nome} \nidade: {self.idade} \naltura: {self.altura}")

    def __str__(self):
        return f"nome: {self.nome} \nidade: {self.idade} \naltura: {self.altura}"
p1 = pessoa("luan", 21, 177)
p1.mostrar()
print(p1)


