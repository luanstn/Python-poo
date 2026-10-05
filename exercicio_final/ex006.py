class tarefa:
    def __init__(self, id, titulo):
        self.__id = id
        self.__titulo = titulo
        self.__status = "a fazer"

    @property
    def id(self):
        return self.__id

    @property
    def titulo(self):
        return self.__titulo

    @property
    def status(self):
        return self.__status

    def mudar_status(self):
        if self.status == "a fazer":
            self.__status = "em progresso"
        elif self.status == "em progresso":
            self.__status = "concluído"

    def ver_status(self):
        print(self.__status)

class quadroKanban:
    def __init__(self):
        self.__lista = []

    @property
    def lista(self):
        return self.__lista

    def adicionar_tarefa(self, valor):
        self.lista.append(valor)

    def mover_tarefa(self, valor):
        if valor in self.lista:
            valor.mudar_status()
        else:
            print("não tem essa tarefa.")

    def exibir_quadro(self):
        fazer = []
        progresso = []
        concluido = []
        for c in self.lista:
            if c.status == "a fazer":
                fazer.append(c)
            elif c.status == "em progresso":
                progresso.append(c)
            else:
                concluido.append(c)
        for c in fazer:
            print(f"id: {c.id} \ntítulo: {c.titulo} \nstatus: {c.status}")
        for c in progresso:
            print(f"id: {c.id} \ntítulo: {c.titulo} \nstatus: {c.status}")
        for c in concluido:
            print(f"id: {c.id} \ntítulo: {c.titulo} \nstatus: {c.status}")

t1 = tarefa(1, "faxinar a casa")
t2 = tarefa(2, "andar com cachorro")
t3 = tarefa(3, "lavar carro")
t4 = tarefa(4, "estudar")

q1 = quadroKanban()
q1.adicionar_tarefa(t1)
q1.adicionar_tarefa(t2)
q1.adicionar_tarefa(t3)
q1.adicionar_tarefa(t4)
