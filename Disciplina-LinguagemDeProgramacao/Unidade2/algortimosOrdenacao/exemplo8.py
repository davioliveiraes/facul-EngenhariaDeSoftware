# Marge Sort - Ordenação Por intercalação
def marge_sort(lista, beg, end):
   if beg < end:
      mid = (beg+end) // 2
      marge_sort(lista, beg, mid)
      marge_sort(lista, mid+1, end)
      marge(lista, beg, mid, end)

def marge(lista, beg, mid, end):
   left = lista[beg:mid+1]
   right = lista[mid+1:end+1]
   i = 0
   j = 0
   k = beg
   while i < len(left) and j < len(right):
      if left[i] < right[j]:
         lista[k] = left[i]
         i += 1
      else:
         lista[k] = right[j]
         j += 1
      k += 1
   while i < len(left):
      lista[k] = left[i]
      i += 1
      k += 1
   while j < len(right):
      lista[k] = right[j]
      j += 1
      k += 1

lista = [40, 20, 50, 10, 5, 80, 15]
marge_sort(lista, 0, len(lista)-1)
print(lista)

# Ordenação de intercalação de forma decrescente
def marge_sort_decres(lista, beg, end):
   if beg < end:
      mid = (beg+end) // 2
      marge_sort_decres(lista, beg, mid)
      marge_sort_decres(lista, mid+1, end)
      marge_decres(lista, beg, mid, end)

def marge_decres(lista, beg, mid, end):
   left = lista[beg:mid+1]
   right = lista[mid+1:end+1]
   i = 0
   j = 0
   k = beg
   while i < len(left) and j < len(right):
      if left[i] > right[j]:
         lista[k] = left[i]
         i += 1
      else:
         lista[k] = right[j]
         j += 1
      k += 1
   while i < len(left):
      lista[k] = left[i]
      i += 1
      k += 1
   while j < len(right):
      lista[k] = right[j]
      j += 1
      k += 1

lista = [40, 20, 50, 10, 5, 80, 15]
marge_sort_decres(lista, 0, len(lista)-1)
print(lista)

