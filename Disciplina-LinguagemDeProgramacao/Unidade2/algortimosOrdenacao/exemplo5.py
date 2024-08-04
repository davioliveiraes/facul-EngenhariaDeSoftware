def bubble_sort(lista):
   for i in range(len(lista)-1, 0, -1):
      for j in range(i):
         if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
   return lista

lista = [50, 40, 30, 20, 10, 1]
print(bubble_sort(lista))
