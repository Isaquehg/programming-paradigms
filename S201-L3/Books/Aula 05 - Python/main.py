''' Exemplo
class Cachorro:
  # Construtor
  tipo = "Puddle"
  def __init__(self, idade):
    self.idade = idade

  def latir(self,latido):
    print(f"{self.tipo} fez: {latido}")

# Classe 'filha'
class Yorkshire(Cachorro):
  def __init__(self, idade, nome):
    super().__init__(idade)
    self.__nome = nome
    
  def latir(self):
    print(f"{self.__nome} não late")

# Instanciando
a = Yorkshire(13, "Dog")
a.latir()
'''

# EXERCICIO
import exerc01 as a
import exerc02 as b

pessoa1 = a.Pessoa("Gabriel", 19)
pessoa2 = b.Pessoa("Nome", 99)

print(f"{pessoa1.nome}: {pessoa1.idade} anos")
print(f"{pessoa2.nome}: {pessoa2.idade} anos")

aluno = b.Aluno(154, "Daniel", 29)
prof = b.Professor("Gabriel", 19)
pessoa = b.Pessoa("Eu", 999)

aluno.mostrarIdade()
aluno.latir("auuuuuuuu")