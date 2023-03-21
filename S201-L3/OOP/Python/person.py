class Person():
    def __init__(self, nome, idade):
        self.__nome = nome
        self.idade = idade

    def print_nome(self):
        print(f"O nome é {self.__nome}")
    
    def getIdade(self):
        print(self.idade)

person1 = Person("Larry", 25)
person2 = Person("Darry", 42)
print(f"Nome1 = {person1.nome}. Idade1: {person1.idade}")
print(f"Nome2 = {person2.nome}. Idade2: {person2.idade}")