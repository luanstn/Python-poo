class produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def etiqueta(self):
        print("Produto")
        print(f"{self.nome}")
        print(f"R${self.valor}")

p1 = produto("Iphone 15", "2,5000")
p1.etiqueta()