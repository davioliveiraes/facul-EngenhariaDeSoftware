def improved_bubble_sort(lista):
   i = len(lista)-1
   while i >= 1:
      ch = -1
      for j in range(i):
         if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
            ch = j
      i = ch
   return lista

lista = [6, 3, 5, 7, 2, 4]
print(improved_bubble_sort(lista))

# Ordenado de forma decrescente
def bubble_sort_decres(lista):
   for i in range(len(lista)-1, 0, -1):
      for j in range(i):
         if lista[j] < lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
   return lista

lista = [6, 3, 5, 7, 2, 4]
print(bubble_sort_decres(lista))
