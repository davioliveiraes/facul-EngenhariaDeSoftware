lista = [10, 4, 1, 15, -3]
lista_ordenada1 = sorted(lista)
lista_ordenada2 = lista.sort()

print(f"Lista: {lista}")
print(f"Lista Ordenada 1: {lista_ordenada1}")
print(f"Lista Ordenada 2: {lista_ordenada2}")
print(f"Lista: {lista}")

print()

lista2 = [7, 4]
if lista2[0] > lista2[1]:
   aux = lista2[1]
   lista2[1] = lista2[0]
   lista2[0] = aux

print(f"Lista ordenada: {lista2}")

print()

lista3 = [5, -1]
if lista3[0] > lista3[1]:
   lista3[0], lista3[1] = lista3[1], lista3[0]

print(f"Lista ordenada: {lista3}")


