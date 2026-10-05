
class produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.__quantidade = quantidade

    def get_quantidade(self):
        return self.__quantidade

    def _mudar_quantidade(self, novo_valor):
        self.__quantidade = novo_valor

    def adicionar_estoque(self, qtd):
        quantidade_atual = self.get_quantidade()
        if qtd > 0:
            novo = quantidade_atual + qtd
            self._mudar_quantidade(novo)
        else:
            print("adicione o valor correto")

    def remover_produto(self,qtd):
        quantidade_atual = self.get_quantidade()
        if qtd > 0:
            if qtd <= quantidade_atual:
                novo = quantidade_atual - qtd
                self._mudar_quantidade(novo)
            else:
                print("estoque insuficiente")
        else:
            print("insira um número certo")


p1 = produto("arroz", 100)

p1.remover_produto(101)

print(p1.get_quantidade())




