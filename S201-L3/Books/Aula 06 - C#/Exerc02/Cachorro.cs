using System;

class Cachorro{
  public string Nome {get;}
  public int Idade {get; set;}

  public void showNome(){
    Console.WriteLine($"O nome do cachorro é: {Nome}");
  }
  public virtual void showIdade(){
    Console.WriteLine($"A idade do cachorro é: {Idade}");
  }

  public Cachorro(string nome, int idade){
    Nome = nome;
    Idade = idade;
  }
}