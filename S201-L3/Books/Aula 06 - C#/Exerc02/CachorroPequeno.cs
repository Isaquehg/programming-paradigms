using System;

class CachorroPequeno : Cachorro
{
    public override void showIdade()
    {
        Console.WriteLine($"{Nome} pequeno com {Idade} anos.");
    }

    public CachorroPequeno(string nome, int idade) : base(nome, idade) { }
}