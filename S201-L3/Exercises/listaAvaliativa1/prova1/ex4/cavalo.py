from animalCorrida import AnimalCorrida


class Cavalo(AnimalCorrida):
    def __init__(self, nome, cor, velocidade) -> None:
        super().__init__(nome, cor, velocidade)
        self.__posicao = 0

    def mover(self):
        if(self.__posicao < 200):
            self.__posicao += self.velocidade * 4
            print(f"Cavalo {self.nome} na posição {self.__posicao}")
        else:
            print(f"O cavalo {self.nome} terminou a corrida!")
