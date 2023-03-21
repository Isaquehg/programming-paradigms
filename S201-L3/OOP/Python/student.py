from person import Person

class Student(Person):
    def __init__(self, nome, idade, mat):
        super().__init__(nome, idade)
        self.nome = nome
        self.idade = idade
        self.__mat = mat

    def getMat(self):
        print(f"matricula aluno: {self.__mat}")

    def print_nome(self):
        return super().print_nome()
    
    def getIdade(self):
        print(f"idade aluno: {super().getIdade()}")