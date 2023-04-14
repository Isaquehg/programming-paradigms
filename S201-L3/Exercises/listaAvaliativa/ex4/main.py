from televisao import Televisao
from smartTv import SmartTV

tv1 = Televisao("LG", "Canal #1")
smartTv1 = SmartTV("Phillips", "Canal #3", True)

tv1.aumentarVolume()
tv1.diminuirVolume()
tv1.trocarCanal("Canal #5")

smartTv1.aumentarVolume()
smartTv1.diminuirVolume()
smartTv1.trocarCanal("Canal #7")
smartTv1.conectarInternet()