class Covid():
   def posicao(self):
      print("--------------------------")
   
   def nome(self):
      print("--------------------------")
   
   def casos(self):
      print("--------------------------")
   
   def mortes(self):
      print("--------------------------")
   
class Brasil(Covid):
   def posicao(self):
      print("3° LUGAR")
   
   def nome(self):
      print("- > BRASIL - AMÉRICA DO SUL")
   
   def casos(self):
      print("29.000.00 CASOS POR COVID-19")
   
   def mortes(self):
      print("658.000 MORTES CONFIRMADOS POR COVID-19 E CERCA DE 28.300.000 CURADOS")

class main():
   br = Brasil()
   print("Brasil: ")
   br.posicao()
   br.nome()
   br.casos()
   br.mortes()

if __name__ == "__main__":
   main()