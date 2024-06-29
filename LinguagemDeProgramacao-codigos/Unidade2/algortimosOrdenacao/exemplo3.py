# Selection Sort - Minsort - Ordenação por seleção, pegando o valor mínimo

def selection_sort_minsort(lista):
   for i in range(len(lista)):
      min_index = i
      for j in range(i+1, len(lista)):
         if lista[min_index] > lista[j]:
            min_index = j
      lista[i], lista[min_index] = lista[min_index], lista[i]
   return lista

lista = [50, 42, 35, 34, 33, 32]
print(selection_sort_minsort(lista))

# Selection Sort - Maxsort - Ordenação, pegando o valor máximo

def selection_sort_maxsort(lista):
   for i in range(len(lista)):
      max_index = 0
      for j in range(i+1):
         if lista[max_index] < lista[j]:
            max_index = j
      lista[i], lista[max_index] = lista[max_index], lista[i]
   return lista

lista = [60, 30, 50, 70, 40, 20]
print(selection_sort_maxsort(lista))
