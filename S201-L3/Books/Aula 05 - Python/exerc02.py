class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def imprimeNome(self):
    print(f'O nome é {self.nome}')

  def mostrarIdade(self):
    pass


class Professor(Pessoa):
  def mostrarIdade(self):
    print(f'Professor com {self.idade} anos')


class Aluno(Pessoa):
  def __init__(self,matricula,nome,idade):
    super().__init__(nome,idade)
    self.__matricula = matricula

  def latir(self, sound="Arf"):
    print(f"{self.nome} says {sound}")

  def mostrarIdade(self):
    print(f'Aluno com {self.idade} anos')