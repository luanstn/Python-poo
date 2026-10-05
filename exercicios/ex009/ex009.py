class tv:
    def __init__(self):
        self.ligada = False
        self.volume = 99
        self.canal = 1

    def sobe_canal(self):
        if self.ligada == True:
            if self.canal < 5:
                self.canal = self.canal+1
                print(f"estamos no canal {self.canal}")
            else:
                print("você está no último canal")
        else:
            print("A tv está desligada")


    def volta_canal(self):
        if self.ligada == True:
            if self.canal > 1:
                self.canal = self.canal-1
                print(f"estamos no canal {self.canal}")
            else:
                print("você já está no último canal")
        else:
            print("A tv está desligada")

    def liga(self):
        if self.ligada == False:
            self.ligada = True
            print("tv ligada")
        else:
            self.ligada = False
            print("Tv desligada")

    def aumenta(self):
        if self.volume < 100:
            if self.ligada == True:
                self.volume = self.volume + 1
                print(self.volume)
            else:
                print("a tv está desligada")
        else:
            print("está no volume máximo")


    def abaixa(self):
        if self.volume > 0:
            if self.ligada == True:
                self.volume = self.volume - 1
                print(self.volume)
            else:
                print("a tv está desligada")
        else:
            print("volume mínino")


c1 = tv()

while True:
    opcao = str(input())

    if opcao == "@":
        c1.liga()

    if opcao == "+":
        c1.aumenta()

    if opcao == "-":
        c1.abaixa()

    if opcao == "d":
        c1.sobe_canal()

    if opcao == "a":
        c1.volta_canal()