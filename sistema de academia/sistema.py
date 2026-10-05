class aluno:
    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.__lista = []

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, valor):
        if valor <= 0:
            print("Erro: a idade tem que ser positiva")
            self.__idade = 0
        else:
            self.__idade = valor

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, valor):
        if valor <= 0:
            print("Erro: O peso tem que ser positivo")
            self.__peso = 0
        else:
            self.__peso = valor

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, valor):
        if valor <= 0:
            print("Erro: A altura tem que ser positiva")
            self.__altura = 0
        else:
            self.__altura = valor

    @property
    def lista(self):
        return self.__lista

    def adicionar_treino(self, valor):
        self.lista.append(valor)

    def remover_treino(self, valor):
        self.lista.remove(valor)

    def listar_treinos(self):
        for c in self.lista:
            print(f"Treino: {c.nome} | Duração: {c.duracao} | Calorias: {c.calorias}")


class treino:
    def __init__(self, nome, duracao, calorias):
        self.__nome = nome
        self.__duracao = duracao
        self.__calorias = calorias

    @property
    def nome(self):
        return self.__nome

    @property
    def duracao(self):
        return self.__duracao

    @property
    def calorias(self):
        return self.__calorias

    def __str__(self):
        return f"Treino: {self.nome} | Duração: {self.duracao} Min. | Calorias: {self.calorias}"

class academia:
    def __init__(self):
        self.__lista_alunos = []
        self.__lista_treinos = []

    @property
    def lista_alunos(self):
        return self.__lista_alunos

    @property
    def lista_treinos(self):
        return self.__lista_treinos

    def cadastrar_aluno(self, valor):
        if valor in self.lista_alunos:
            print("Esse aluno já foi matriculado")
        else:
            self.lista_alunos.append(valor)

    def cadastrar_treino(self, valor):
        self.lista_treinos.append(valor)

    def adicionar_treino(self, nome, valor):
        aluno = False
        for c in self.lista_alunos:
            if c.nome == nome:
                aluno = True
                break

        treino = False
        for v in self.lista_treinos:
            if v == valor:
                treino = True
                break

        if aluno == True and treino == True:
            for c in self.lista_alunos:
                if c.nome == nome:
                    c.adicionar_treino(valor)
                    print("treino adicionado com sucesso!")

        elif aluno == False:
            print("aluno não encontrado")

        else:
            print("treino não encontrado")

    def remover_treino(self, nome, valor):
        for c in self.lista_alunos:
            if c.nome == nome:
                if valor in c.lista:
                    c.remover_treino(valor)
                    print("treino removido com sucesso!")
                    return
                else:
                    print("esse treino ainda não foi adicionado")
                    return

        print("aluno não encontrado")

    def listar_alunos(self):
        print("------ ALUNOS MATRICULADOS ------")
        for c in self.lista_alunos:
            print(f"Nome: {c.nome} | Idade: {c.idade} | Peso: {c.peso} | Altura: {c.altura}")

    def listar_treinos(self):
        print(" ----- TREINOS DISPONÍVEIS -----")
        for c in self.lista_treinos:
            print(f"Treino: {c.nome} | Duração: {c.duracao} Min. | Calorias: {c.calorias}")

    def __len__(self):
        return len(self.lista_alunos)

a1 = aluno("Luan", 20, 73, 1.81)
a2 = aluno("Rafael", 15, 63, 1.78)
a3 = aluno("Raylson", 11, 56, 1.61)


t1 = treino("peito e tríceps", 60, 400)
t2 = treino("pernas", 45, 350)

ac = academia()
ac.cadastrar_aluno(a1)
ac.cadastrar_aluno(a2)
ac.cadastrar_aluno(a3)


ac.cadastrar_treino(t2)
ac.cadastrar_treino(t1)

ac.adicionar_treino("Luan", t2)
ac.adicionar_treino("Luan", t1)

ac.remover_treino("Luan", t1)

ac.listar_alunos()
