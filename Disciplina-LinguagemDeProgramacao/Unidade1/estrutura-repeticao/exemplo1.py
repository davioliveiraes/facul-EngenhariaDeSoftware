# O comando while deve ser utilizado para construir e controlar a estrutura decisão, sempre que o número de
# repetição não seja conhecida.

numero = 1
while numero != 0:
   numero = int(input("Digite um número inteiro: "))
   if numero % 2 == 0:
      print("Ele é um número par.")
   else:
      print("Ele é um número impar.")

# Todo o bloco com identeçã o de uma tabulação (4 espeços) faz parte da estrutura de repetição.
# Lembre: todo os blocos de comandos em Python são controlados pela indetação.