using System

class CachorroGrande:Cachorro{
    public String Nome;
    public int Idade;

    public CachorroGrande(nome, idade):Cachorro(nome, idade){
        Nome = nome;
        Idade = idade;
    }

    public void showIdade(){
        Console.WriteLine($"Idade Small Dog = {Idade}");
    }
}