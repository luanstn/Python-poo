class medico:
    def __init__(self, nome, especialidade):
        self.__nome = nome
        self.__especialidade = especialidade

    @property
    def nome(self):
        return self.__nome

    @property
    def especialidade(self):
        return self.__especialidade

    def mostrar_dados(self):
        print(f"nome: {self.nome} \nespecialidade: {self.especialidade}")

class paciente:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    def mostrar_dados(self):
        print(f"nome: {self.nome} \nidade: {self.idade}")

class consulta:
    def __init__(self, medico, paciente, dia, mes, ano):
        self.__medico = medico
        self.__paciente = paciente
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def medico(self):
        return self.__medico

    @property
    def paciente(self):
        return self.__paciente

    @property
    def dia(self):
        return self.__dia

    @property
    def mes(self):
        return self.__mes

    @property
    def ano(self):
        return self.__ano

    def realizar_consulta(self):
        print("consulta realizada!")
        print(f"médico: {self.medico.nome} \npaciente: {self.paciente.nome} \ndata: {self.dia}/{self.mes}/{self.ano}")

m1 = medico("Luan", "neurocirurgião")
p1 = paciente("camily", 19)
c1 = consulta(m1, p1, 25, 6, 2026 )

c1.realizar_consulta()