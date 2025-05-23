def busca_sequencial(lista, elemento):
   pos = 0
   encontrado = False
   para = False

   while pos < len(lista) and not encontrado and not para:
      if lista[pos] == elemento:
         encontrado = True
      else:
         if lista[pos] > elemento:
            para = True
         else:
            pos = pos + 1
   return encontrado

testelista = [1, 2, 8, 10, 13, 15, 18, 20]
print(busca_sequencial(testelista, 5))
print(busca_sequencial(testelista, 15))

# Exemplo usando o for

def busca_sequencial2(lista, valor):
   tamanho_lista = len(lista)
   print(f"A quantidade de elementos da lista: {tamanho_lista}")
   for i in range(len(lista)):
      if valor == lista[i]:
         return True
      return False

lista = [1, 2, 8, 10, 13, 15, 18, 20]
print(busca_sequencial2(lista, 1))
print(busca_sequencial2(lista, 5))
