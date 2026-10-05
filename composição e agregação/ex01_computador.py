class processador:
    def __init__(self, modelo, nucleos):
        self.__modelo = modelo
        self.__nucleos = nucleos

    @property
    def modelo(self):
        return self.__modelo

    @property
    def nucleos(self):
        return self.__nucleos

    def mostrar_dados(self):
        print(f"modelo do processador: {self.modelo} \n nucleos: {self.nucleos}")

class memoria:
    def __init__(self, marca, gb):
        self.__marca = marca
        self.__gb = gb

    @property
    def marca(self):
        return self.__marca

    @property
    def gb(self):
        return self.__gb

    def mostrar_dados(self):
        print(f"marca: {self.marca} \n gb: {self.gb}")

class computador:
    def __init__(self, nome, processador, memoria):
        self.__nome = nome
        self.__processador = processador
        self.__memoria = memoria

    @property
    def processador(self):
        return self.__processador

    @property
    def memoria(self):
        return self.__memoria

    @property
    def nome(self):
        return self.__nome

    def mostrar_computador(self):
        print(self.nome)
        self.processador.mostrar_dados()
        self.memoria.mostrar_dados()

p1 = processador("nvidia", "4")
m1 = memoria("nvidia", "8")

c1 = computador("computador de luan", p1, m1)

c1.mostrar_computador()