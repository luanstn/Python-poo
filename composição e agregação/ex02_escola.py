class professor:
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

class curso:
    def __init__(self, nome, carga_horaria):
        self.__nome = nome
        self.__carga_horaria = carga_horaria

    @property
    def nome(self):
        return self.__nome

    @property
    def carga(self):
        return self.__carga_horaria

    def mostrar_dados(self):
        print(f"nome: {self.nome} \ncarga horária: {self.carga}")

class escola:
    def __init__(self, professor, curso):
        self.__professor = professor
        self.__curso = curso

    @property
    def professor(self):
        return self.__professor

    @property
    def curso(self):
        return self.__curso

    def atribuir_professor(self):
        print(f"professor {self.professor.nome} foi atribuido ao curso {self.curso.nome}")

p1 = professor("Luan", "python")
c1 = curso("python", 6)

e1 = escola(p1, c1)

e1.atribuir_professor()