class player:
    def __init__(self):
        self.artista = "Luan"
        self.nome = "meteoro da paixão"
        self.tmptotal = 180
        self.tmpatual = 0
        self.pausa = False

    def tocar(self):
        if self.pausa == False:
            self.pausa = True
            if self.tmpatual < self.tmptotal:
                self.status()
            else:
                print("fim de música")
        else:
            print("já está tocando!")

    def pausar(self):
        if self.pausa == True:
            self.pausa = False
            print("música pausada")
            self.status()
        else:
            print("a música já está pausada")

    def avancar(self):
        if self.pausa == True:
            if self.tmpatual < self.tmptotal:
                self.tmpatual = self.tmpatual + 10
                self.status()
        else:
            print("a música está pausada")

    def voltar(self):
        if self.tmpatual - 10 >= 0:
            self.tmpatual = self.tmpatual - 10
            self.status()
        else:
            self.tmpatual = 0

    def status(self):
        print(f"Música: {self.nome}\n Artista : {self.artista}\n tempo: {self.tmpatual}/{self.tmptotal}")
        if self.pausa == True:
            print("tocando")
        else:
            print("pausado")

player1 = player()

while True:
    print("1 - tocar \n2 - pausar\n3 - avançar\n4 - voltar\n5 - status\n6 - Sair")
    opcao = int(input())

    if opcao == 1:
        player1.tocar()
    elif opcao == 2:
        player1.pausar()
    elif opcao == 3:
        player1.avancar()
    elif opcao == 4:
        player1.voltar()
    elif opcao == 5:
        player1.status()
    elif opcao == 6:
        print("saindo...")
        break




