class elevador:
    def __init__(self, capacidade, quantidade):
        self.__andares = 10
        self.__capacidade = capacidade
        self.__quantidade = quantidade
        self.__andar_atual = 0

    def get_andares(self):
        return self.__andares

    def get_capacidade(self):
        return self.__capacidade

    def get_quantidade(self):
        return self.__quantidade

    def _mudar_quantidade(self, novo):
        self.__quantidade = novo

    def get_andar_atual(self):
        return self.__andar_atual

    def _mudar_andar(self, novo):
        self.__andar_atual = novo

    def entra(self):
        if self.get_quantidade() < self.get_capacidade():
            novo = self.get_quantidade() + 1
            self._mudar_quantidade(novo)
            print(f"entrou mais uma pessoa, agora são: {self.get_quantidade()} \ncapacidade total {self.get_capacidade()}")
        else:
            print("o elevador está cheio!!")

    def sai(self):
        if self.get_quantidade() > 0:
            novo = self.get_quantidade() - 1
            self._mudar_quantidade(novo)
            print(f"saiu uma pessoa do elevador, agora são: {self.get_quantidade()}  \ncapacidade total {self.get_capacidade()}")
        else:
            print("o elevador está vazio!")

    def sobe(self):
        if self.get_andar_atual() < self.get_andares():
            novo = self.get_andar_atual() + 1
            self._mudar_andar(novo)
            print(f"subindo! estamos no andar {self.get_andar_atual()} \nandares total: {self.get_andares()}")
        else:
            print("estamos na cobertura!")

    def desce(self):
        if self.get_andar_atual() > 1:
            novo = self.get_andar_atual() - 1
            self._mudar_andar(novo)
            print(f"descendo! estamos no andar {self.get_andar_atual()}")
        else:
            print("estamos no térreo")

el = elevador(10, 0)

while True:
    opcao = int(input("1- entrar pessoa \n2- sair pessoa \n3- subir elevador \n4- descer elevador \nescolha: "))

    if opcao == 1:
        el.entra()

    elif opcao == 2:
        el.sai()

    elif opcao == 3:
        el.sobe()

    elif opcao == 4:
        el.desce()

    elif opcao == 5:
        break