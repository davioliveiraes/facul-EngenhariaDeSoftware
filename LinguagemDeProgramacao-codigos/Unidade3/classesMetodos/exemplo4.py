class Televisao:
   def __init__(self):
      self.volume = 10
   
   def aumentar_volume(self):
      self.volume += 1
   
   def diminuir_volume(self):
      self.volume -= 1

tv = Televisao()
print(f"Volume ao ligar a tv = {tv.volume}")
tv.aumentar_volume()
print(f"Volume atual: {tv.volume}")
tv.diminuir_volume()
print(f"Volume atual: {tv.volume}")