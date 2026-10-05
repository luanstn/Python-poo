
class sistemamultas:
    def __init__(self, nome, placa,velocidade):
        self.nome = nome
        self.velocidade = velocidade
        self.valor = 0
        self.placa = placa
        self.identificador = False

        self.multa()


    def multa(self):
        if self.velocidade > 60:
            excesso = self.velocidade - 60
            self.valor = excesso * 5
            self.identificador = True
        else:
            self.valor = 0
            self.identificador = False

    def pago(self):
        self.valor = 0
        self.identificador = False
        return "Multa paga"

    def atualizar_vel(self, valor):
        self.velocidade = valor
        self.multa()

    def __str__(self):
        if self.identificador == True:
            return (f"Você tem multa! \nNome: {self.nome} \nplaca: {self.placa} "
                    f"\nvalor da multa: R${self.valor} \nmotivo: {self.velocidade}km/h em uma via de 60km/h")
        else:
            return f"não tem multa \nNome: {self.nome} \nplaca: {self.placa}"

"""
carro1 = sistemamultas("Luan", "ksd212", 61)
print(carro1.multa())
print(carro1)
"""

carro2 = sistemamultas("Lucas", "df232d", 57)
print(carro2)
carro2.atualizar_vel(70)
print(carro2)

