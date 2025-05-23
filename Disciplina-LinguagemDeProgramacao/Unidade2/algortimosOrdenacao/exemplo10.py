# Quick Sort - Ordenação Rápida
def quick_sort(lista, beg, end):
   i = beg
   j = end
   pivot = lista[(i+j) // 2]
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
         quick_sort(lista, beg, j)
      if i < end:
         quick_sort(lista, i, end)

lista = [40, 20, 50, 10, 5, 80, 15]
quick_sort(lista, 0, len(lista)-1)
print(lista)

# Ordem decrescente
def quick_sort_decres(lista, beg, end):
   i = beg
   j = end
   pivot = lista[(i+j) // 2]
   while i <= j:
      while lista[i] > pivot:
         i += 1
      while lista[j] < pivot:
         j -= 1
      if i <= j:
         lista[i], lista[j] = lista[j], lista[i]
         i += 1
         j -= 1
      if beg < j:
         quick_sort_decres(lista, beg, j)
      if i < end:
         quick_sort_decres(lista, i, end)

lista2 = [40, 20, 50, 10, 5, 80, 15]
quick_sort_decres(lista2, 0, len(lista)-1)
print(lista2)      
