class aluno:
    def __init__(self, nome, matricula, curso):
        self.__nome = nome
        self.__matricula = matricula
        self.__curso = curso

    @property
    def nome(self):
        return self.__nome

    @property
    def matricula(self):
        return self.__matricula

    @property
    def curso(self):
        return self.__curso

    def __eq__(self, outro):
        return self.matricula == outro.matricula

a1 = aluno("luan", 123, "cc")
a2 = aluno("luan", 123, "ads")
a3 = aluno("rafael", 345, "ads")

print(a1 == a2)
