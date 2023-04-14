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
        return super().trocarCanal(canal)

    def conectarInternet(self):
        if self.internet:
            print("Conectado à internet com sucesso!")