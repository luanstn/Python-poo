"""
class canaldoluan:
    def __init__(self, nome, descricao, inscritos):
       self.nome = nome
        self.descricao = descricao
        self.inscritos = inscritos

class canalempresarial(canaldoluan):
    def __init__(self, nome, descricao, inscritos):
        super().__init__(nome, descricao, inscritos)
        self.equipe = []

canal_luan = canaldoluan("luan", "canal mt bom", "1000")
canal_rafa = canaldoluan("rafa", "canal legal", "3000")
canal_empresarial = canalempresarial("luanz", "canal empresariado", "5000")


#o canal_luan não tem equipe
print(canal_luan.nome)

print(canal_empresarial.equipe)
#já o canal_empresarial tem equipe, pois foi adicionado dps, isso é herança

canal_empresarial.equipe.append("Camily")
canal_empresarial.equipe.append("rafz")
#eu consigo editar e modificar com muita facilidade no método, por isso vamos aprender o encapsulamento

print(canal_empresarial.equipe)

"""
"""
#                       ENCAPSULAMENTO


class canaldoluan:
    def __init__(self, nome, descricao, inscritos):
        self.nome = nome
        self.descricao = descricao
        self.inscritos = inscritos

class canalempresarial(canaldoluan):
    def __init__(self, nome, descricao, inscritos):
        super().__init__(nome, descricao, inscritos)
        self._equipe = []

    @property
    def equipe(self):
        return self._equipe

    def add_membro(self,membro):
        if membro not in self._equipe:
            self._equipe.append(membro)
        else:
            print("esse membro já está na equipe")

    def remover_membro(self,membro):
        if membro in self.equipe:
            self._equipe.remove(membro)
        else:
            print("esse membro não está na equipe")


canal_luan = canaldoluan("luan", "canal mt bom", "1000")
canal_rafa = canaldoluan("rafa", "canal legal", "3000")
canal_empresarial = canalempresarial("luanz", "canal empresariado", "5000")

print(f"membros atuais: {canal_empresarial.equipe}")
canal_empresarial.add_membro("pedro")

print(f"membros atuais: {canal_empresarial.equipe}")
canal_empresarial.add_membro("pedro")

canal_empresarial.remover_membro("pedro")
print(f"membros atuais: {canal_empresarial.equipe}")
"""

class animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def comer(self):
        print(f"{self.nome} está comendo")

    def dormir(self):
        print(f"{self.nome} está dormindo")

class cachorro(animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def latir(self):
        print(f"{self.nome} está latindo")

    def identificar(self):
        print(f"{self.nome} é da raça {self.raca}")


class gato(animal):
    def __init__(self, nome, idade, cor_pelo):
        super().__init__(nome, idade)
        self.cor_pelo = cor_pelo

    def miar(self):
        print(f"{self.nome} está miando")

    def cor(self):
        print(f"{self.nome} é da cor {self.cor_pelo}")


doguinho = cachorro("luke", 5, "pitbull")
gatinho = gato("garfield", 3, "laranja")

doguinho.comer()
doguinho.dormir()
doguinho.latir()
doguinho.identificar()
