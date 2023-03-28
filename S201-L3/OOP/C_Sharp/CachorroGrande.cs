using System

class CachorroGrande:Cachorro{
    public String Nome;
    public int Idade;
    private int Tamanho;

    public CachorroGrande(nome, idade, tamanho):Cachorro(nome, idade){
        Nome = nome;
        Idade = idade;
        Tamanho = tamanho;
    }

    public void showIdade(){
        Console.WriteLine($"Idade Big Dog = {Idade}");
    }
}