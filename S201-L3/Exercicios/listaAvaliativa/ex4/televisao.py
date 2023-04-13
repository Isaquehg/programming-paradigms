class Televisao():
    def __init__(self, modelo, canal) -> None:
        self.modelo = modelo
        self._volume = 0
        self._canal = canal

    def aumentarVolume(self):
        self._volume += 1
        print(f"Volume aumentado para {self._volume}")

    def diminuirVolume(self):
        self._volume -= 1
        print(f"Volume reduzido para {self._volume}")

    def trocarCanal(self, canal: str):
        self.canal = canal
        print(f"Canal alterado para {self.canal}")