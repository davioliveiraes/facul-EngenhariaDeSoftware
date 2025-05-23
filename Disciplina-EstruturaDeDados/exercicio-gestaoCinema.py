class CinemaReserva:
   def __init__(self, filas, assentos_por_fila):
      self.assentos = [[0 for _ in range(assentos_por_fila)] for _ in range(filas)]
   
   def mostrar_assentos(self):
      for fila in self.assentos:
         print(" ".join(map(str, fila)))
      print()
   
   def resevar_assento(self, fila, assento):
      if self.assentos[fila][assento] == 0:
         self.assentos[fila][assento] = 1
         print(f"Assento: {assento} - Na fila: {fila} - Reservado com sucesso.")
      else:
         print(f"Assento: {assento} - Na fila {fila} - Já está reservado.")
   
   def liberar_assento(self, fila, assento):
      if self.assentos[fila][assento] == 1:
         self.assentos[fila][assento] = 0
         print(f"Assento: {assento} - Na fila {fila} - liberado com sucesso.")
      else:
         print(f"Assento: {assento} - Na fila {fila} - Já está disponível.")
      
   def verificar_disponibilidade(self, fila, assento):
      return self.assentos[fila][assento] == 0
   
# Exemplo de uso
cinema = CinemaReserva(filas = 5, assentos_por_fila = 10)
cinema.mostrar_assentos()

cinema.resevar_assento(0, 1)
cinema.resevar_assento(2, 5)

cinema.mostrar_assentos()
cinema.liberar_assento(2, 5)

cinema.mostrar_assentos()

cinema.resevar_assento(0, 1)
cinema.liberar_assento(2, 5)

