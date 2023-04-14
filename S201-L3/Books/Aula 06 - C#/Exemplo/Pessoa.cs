using System;

public class Pessoa {
  private string Nome;
  private int Idade;

  public Pessoa(string nome, int idade){
    Nome = nome;
    Idade = idade;
  }

  public virtual void showInfo(){
    Console.WriteLine($"{Nome} tem {Idade} anos.");
  }

  public string getNome(){
    return Nome;
  }
  public int getIdade(){
    return Idade;
  }
}