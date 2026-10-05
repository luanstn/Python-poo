class churrasco:
    def __init__(self,titulo, quantidade = 0):
        self.titulo = titulo
        self.quantidade = quantidade

    def analisar(self):
        calculo = self.quantidade * 0.40
        custottl = calculo * 82.40
        cadapessoa = custottl/ self.quantidade
        print(f"analisando o {self.titulo} com {self.quantidade} convidados")
        print(f"cada participante comerá 0.4Kg e cada Kg custa R$82.40\nrecomendo comprar {calculo:.3f}Kg de carne")
        print(f"o custo total será R${custottl:.2f}\ncada pessoa pagará R${cadapessoa:.2f} para participar")

c1 = churrasco("churrasco da família", 100)
c1.analisar()
