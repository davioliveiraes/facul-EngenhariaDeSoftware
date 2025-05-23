# Ordenando números
from random import randint

def quicksort_number(lista, beg, end):
   i = beg
   j = end
   pivot = lista[(i+j)//2]
   while i <= j:
      while lista[i] < pivot:
         i += 1
      while lista[j] > pivot:
         j -= 1
      if i <= j:
         lista[i], lista[j] = lista[j], lista[i]
         i += 1
         j -= 1
   if beg < j:
      quicksort_number(lista, beg, j)
   if i < end:
      quicksort_number(lista, i, end)

random_list = [randint(1, 100) for _ in range(20)]
print(f"Lista original: {random_list}")
print()
quicksort_number(random_list, 0, len(random_list)-1)
print(f"LISTA ORDENADA: {random_list}")

