class semaforo:
    def __init__(self):
        self.__cor = "vermelho"

    @property
    def cor(self):
        return self.__cor

    def mudar(self):
        if self.__cor == "vermelho":
            self.__cor = "amarelo"
        elif self.__cor =="amarelo":
            self.__cor = "verde"
        elif self.__cor == "verde":
            self.__cor = "vermelho"

    def mostrar(self):
        print(f"cor atual: {self.__cor}")

s1 = semaforo()

s1.mostrar()
s1.mudar()
s1.mostrar()
s1.mudar()
s1.mostrar()