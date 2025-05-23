# Classificação de Ordenação Simples
def simple_exchange_sort(lista):
   for i in range(len(lista)-1):
      for j in range(i+1, len(lista)):
         if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]
   return lista

lista = [40, 30, 20, 10, 5]
print(simple_exchange_sort(lista))

# Classificação simples de ordenação de forma decrescente
def simple_exchange_sort_decre(lista):
   for i in range(len(lista)-1):
      for j in range(i+1, len(lista)):
         if lista[i] < lista[j]:
            lista[i], lista[j] = lista[j], lista[i]
   return lista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(simple_exchange_sort_decre(lista))
