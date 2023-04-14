using System;

class Program {
  public static void Main (string[] args) {
    // Declarando variavel
    float[] numeros = new float[3];
    float media;

    // Leitura
    for(int i=0; i<3; i++){
      Console.Write("N{0}: ", i+1);
      numeros[i] = int.Parse(Console.ReadLine());
    }

    // Calculo
    media = calculoMedia(numeros);

    // Saida
    Console.WriteLine("Aluno tem {0} de media", media);
  }

  public static float calculoMedia(float[] arr){
    float media;

    media=(arr[0]+arr[1]+arr[2])/3;
    
    return media;
  }
}