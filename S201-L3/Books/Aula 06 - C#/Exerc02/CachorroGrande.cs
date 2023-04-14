using System;

class CachorroGrande : Cachorro{
  private int Tamanho;

  public override void showIdade(){
    Console.WriteLine($"{Nome} com tamanho {Tamanho} tem {Idade} anos.");
  }
  
  public CachorroGrande(string nome, int idade, int tamanho) : base(nome,idade){
    Tamanho = tamanho;
  }
}