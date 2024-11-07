produtos = [
   {"id": 1, "nome": "Camiseta", "preco": 29.99},
   {"id": 2, "nome": "Calça", "preco": 59.99},
   {"id": 3, "nome": "Tênis", "preco": 89.99},
   {"id": 4, "nome": "Casaco", "preco": 119.90},
]

def merge_sort(lista, chave):
   if len(lista) > 1:
      meio = len(lista) // 2
      esquerda = lista[:meio]
      direita = lista[meio:]

      merge_sort(esquerda, chave)
      merge_sort(direita, chave)

      i = j = k = 0
      while i < len(esquerda) and j < len(direita):
         if esquerda[i][chave] < direita[j][chave]:
            lista[k] = esquerda[i]
            i += 1
         else:
            lista[k] = direita[j]
            j += 1
         k += 1
      
      while j < len(direita):
         lista[k] = direita[j]
         j += 1
         k += 1

merge_sort(produtos, "preco")
print("Produtos ordenados por preço: ")
for produto in produtos:
   print(produto)

print()

def busca_binario(lista, chave, valor):
   esquerda, direita = 0, len(lista) - 1
   while esquerda <= direita:
      meio = (esquerda + direita) // 2
      if lista[meio][chave] == valor:
         return meio
      elif lista[meio][chave] < valor:
         esquerda = meio + 1
      else:
         direita = meio - 1
   return - 1

indice = busca_binario(produtos, "preco", 59.99)
if indice != -1:
   print(f"Produto encontrado: {produtos[indice]}")
else:
   print("Produto não encontrado")

print()

def busca_binario_intervalo(lista, chave, inicio, fim):
   resultados = []
   for produto in lista:
      if inicio <= produto[chave] <= fim:
         resultados.append(produto)
   return resultados

intervalo_produtos = busca_binario_intervalo(produtos, "preco", 30, 90)
print("Produtos no intervalo de preço entre 30 e 90: ")
for produto in intervalo_produtos:
   print(produto)
