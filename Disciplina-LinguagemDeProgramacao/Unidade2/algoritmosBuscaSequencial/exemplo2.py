import random
def executar_busca_linear(lista, valor):
   for elemento in lista:
      if valor == elemento:
         return True
   return False

lista = random.sample(range(100), 20)
print(f"Lista ordenada: {sorted(lista)}")

resultado = executar_busca_linear(lista, 10)
print(f"O valor 10 foi encontrado: {resultado}")
