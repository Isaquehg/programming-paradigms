from televisao import Televisao

class SmartTV(Televisao):
    def __init__(self, modelo, canal, internet) -> None:
        super().__init__(modelo, canal)
        self.internet = internet

    def aumentarVolume(self):
        return super().aumentarVolume()
    
    def diminuirVolume(self):
        return super().diminuirVolume()
    
    def trocarCanal(self, canal: str):
        return super().trocaCanal(canal)

    def conectarInternet(self, conectado: bool):
        if(conectado):
            self.internet = True
        else:
            self.internet = False