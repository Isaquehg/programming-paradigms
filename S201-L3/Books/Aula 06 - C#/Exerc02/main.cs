using System;

class Program {
  public static void Main (string[] args) {
    Cachorro dog1 = new CachorroGrande("Dog", 10, 8);
    Cachorro dog2 = new CachorroPequeno("Dog", 10);
    Cachorro dog3 = new Cachorro("Dog", 10);

    dog1.showIdade();
    dog2.showIdade();
    dog3.showIdade();
  }
}