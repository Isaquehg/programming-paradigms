from person import Person

class Teacher(Person):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.nome = nome
        self.idade = idade

    def print_nome(self):
        return super().print_nome()

    def getIdade(self):
        print(f"idade professor: {super().getIdade()}")