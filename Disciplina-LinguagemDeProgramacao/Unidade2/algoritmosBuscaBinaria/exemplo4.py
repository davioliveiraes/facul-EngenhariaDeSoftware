def busca_binaria(lista, elemento, retornar_indice=False):
   minimo = 0
   maximo = len(lista) - 1
   iteracoes = 0

   while minimo <= maximo:
      iteracoes += 1
      meio_lista = (minimo + maximo) // 2
      if lista[meio_lista] == elemento:
         if retornar_indice:
            return (True, meio_lista, iteracoes)
         else:
            return (True, iteracoes)
      elif elemento < lista[meio_lista]:
         maximo = meio_lista - 1
      else:
         minimo = meio_lista + 1
   if retornar_indice:
      return (False, -1, iteracoes)
   else:
      return (False, iteracoes)

teste_lista = [1, 2, 8, 10, 13, 15, 18, 20]

# Teste da busca binária
print(busca_binaria(teste_lista, 5))
print(busca_binaria(teste_lista, 15))

# Teste da busca binária com retorno de índice
print(busca_binaria(teste_lista, 5, retornar_indice=True))
print(busca_binaria(teste_lista, 15, retornar_indice=True))
