using System;

class Program {
  public static void Main (string[] args) {
        // Declarando variavel
        float[] numeros = new float[3];
        float media;

        // Leitura de 3 Números
        for(int i=0; i<3; i++){
            numeros[i] = int.Parse(Console.ReadLine());
        }

        // Calculo
        media = calculoMedia(numeros);

        // Output (Indice aumenta conforme a qtde de variaveis)
        Console.WriteLine($"Media = {media}");

        Cachorro cachorro1 = new Cachorro("Larry", 2);
        CachorroGrande cachorro2 = new CachorroGrande("Darry", 5);
        CachorroPequeno = cachorro3 = new CachorroPequeno("Merry", 1);

        cachorro2.showIdade();
        cachorro3.showIdade();
    }

    public static float calculoMedia(float[] arr){
        float media;

        media = (arr[0]+arr[1]+arr[2])/3;
        
        return media;
    }
}