using System;

public class Aluno : Pessoa{
  private string Turma;

  public Aluno(string nome, int idade, string turma) : base(nome,idade){
    Turma = turma;
  }

  public override void showInfo(){
    Console.WriteLine($"Aluno {getNome()} tem {getIdade()} anos.");
  }
}