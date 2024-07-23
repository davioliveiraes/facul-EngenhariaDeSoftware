# Ordenando strings(conjunto de letras)
def quicksort_strings(lista, beg, end):
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
      quicksort_strings(lista, beg, j)
   if i < end:
      quicksort_strings(lista, i, end)

list_strings = ['Microsoft', 'Apple', 'Xiomi', 'Samsung', 'LG', 'OpenAI', 'Nvidea']
print(f"Lista de strings original: {list_strings}")
print()
quicksort_strings(list_strings, 0, len(list_strings)-1)
print(f"LISTA DE STRINGS ORDENADA: {list_strings}")
