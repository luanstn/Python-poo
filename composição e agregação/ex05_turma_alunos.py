#AGREGAÇÃO#

class aluno:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome

    @property
    def matricula(self):
        return self.__matricula

    def mostrar_dados(self):
        print(f"Nome: {self.nome} \nMatricula: {self.matricula}")

class turma:
    def __init__(self):
        self.__lista = []

    @property
    def lista(self):
        return self.__lista

    def adicionar_aluno(self, aluno):
        self.lista.append(aluno)

    def listar(self):
        for c in self.lista:
            print(f"Nome: {c.nome} matricula: {c.matricula}")

a1 = aluno("luan santana", 1)
a2 = aluno("Rafael Rayol", 2)

t1 = turma()

t1.adicionar_aluno(a1)
t1.adicionar_aluno(a2)

t1.listar()