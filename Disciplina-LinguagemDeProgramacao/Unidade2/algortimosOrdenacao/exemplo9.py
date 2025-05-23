def merge_sort(lista, beg=0, end=None):
   if end is None:
      end = len(lista)-1
   if beg < end:
      meio = (beg + end) // 2
      merge_sort(lista, beg, meio)
      merge_sort(lista, meio+1, end)
      merge(lista, beg, meio, end)

def merge(lista, beg, meio, end):
   n1 = meio - beg + 1
   n2 = end - meio
   left = [lista[beg+1] for i in range(n1)]
   right = [lista[meio + 1 + j] for j in range(n2)]
   i = 0
   j = 0
   k = beg
   while i < n1 and j < n2:
      if left[i] <= right[j]:
         lista[k] = left[i]
         i += 1
      else:
         lista[k] = right[i]
         j+=1
      k += 1
   while i < n1:
      lista[k] = left[i]
      i += 1
      k += 1
   while j < n2:
      lista[k] = right[j]
      j += 1
      k += 1

# De forma decrescente

def merge_sort_decres(lista, beg=0, end=None):
   if end is None:
      end = len(lista) - 1
      if beg < end:
         meio = (beg + end) // 2
         merge_sort_decres(lista, beg, meio)
         merge_sort_decres(lista, meio+1, end)
         merge_decres(lista, beg, meio, end)

def merge_decres(lista, beg, meio, end):
   n1 = meio - beg + 1
   n2 = end - meio
   left = [lista[beg+1] for i in range(n1)]
   right = [lista[meio+1+j]for j in range(n2)]
   i = 0
   j = 0
   k = beg
   while i < n1 and j < n2:
      if left[i] >= right[j]:
         i+=1
      else:
         lista[k] = right[j]
         j+=1
      k+=1
   while i < n1:
      lista[k] = left[i]
      i+=1
      k+=1
   while j < n2:
      lista[k] = right[k]
      j += 1
      k += 1
    
lista = [38, 27, 43, 3, 9, 82, 10]
print(f"LISTA ORIGINAL: {lista}")
merge_sort(lista)
print(f"LISTA ORDENADA(CRESCENTE): {lista}")
merge_sort_decres(lista)
print(f"LISTA OREDENADA(DECRESCENTE): {lista}")