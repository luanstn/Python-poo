class paciente:
    def __init__(self, nome, idade, cpf):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def cpf(self):
        return self.__cpf

    def consultar_dados(self):
        print(f"nome: {self.nome} \nidade: {self.__idade} \ncpf: {self.cpf}")

    def alterar_idade(self, valor):
        self.__idade = valor

class medico:
    def __init__(self, nome, especialidade):
        self.__nome = nome
        self.__especialidade = especialidade
        self.__lista = []

    @property
    def nome(self):
        return self.__nome

    @property
    def especialidade(self):
        return self.__especialidade

    @property
    def lista(self):
        return self.__lista

    def adicionar_paciente(self, valor):
        self.__lista.append(valor)
        print("paciente adicionado")

    def remover_pacientes(self, valor):
        self.__lista.remove(valor)

    def listar_pacientes(self):
        for c in self.__lista:
            print(f"nome: {c.nome} \nidade: {c.idade} \ncpf: {c.cpf}")

class consulta:
    def __init__(self, paciente, medico):
        self.__paciente = paciente
        self.__medico = medico
        self.__status = "agendada"

    @property
    def paciente(self):
        return self.__paciente

    @property
    def medico(self):
        return self.__medico

    @property
    def status(self):
        return self.__status

    def realizar(self):
        if self.__status == "agendada":
            self.__status = "realizada"
            print("consulta realizada!")
        else:
            print("não pode ser realizada")

    def cancelar(self):
        if self.__status == "agendada":
            self.__status = "cancelada"
            print("consulta cancelada!")
        elif self.__status == "realizada":
            print("essa consulta já foi realizada")
        else:
            print("a consulta já foi cancelada")

    def finalizar(self):
        if self.__status == "agendada":
            print("não é possível finalizar uma consulta ainda agendada")
        elif self.__status == "cancelada":
            print("a consulta foi cancelada, não pode finalizar")
        else:
            self.__status = "finalizada"
            print("consulta finalizada!")

p1 = paciente("luan", 22, 2334328373)
p2 = paciente("camily", 19, 93848920)
m1 = medico("rafael", "medico geral")

m1.adicionar_paciente(p1)
m1.adicionar_paciente(p2)

c1 = consulta(p1, m1)
c1.realizar()
c1.cancelar()
c1.finalizar()
