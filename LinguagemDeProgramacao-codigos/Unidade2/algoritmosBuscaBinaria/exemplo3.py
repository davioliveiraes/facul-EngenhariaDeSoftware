def busca_binario(lista, elemento):
   minimo = 0
   maximo = len(lista) - 1
   encontrado = False

   while minimo <= maximo and not encontrado:
      meio_lista = (minimo + maximo) // 2
      if lista[meio_lista] == elemento:
         encontrado = True
      elif elemento < lista[meio_lista]:
         maximo = meio_lista - 1
      else:
         minimo = meio_lista + 1
   return encontrado

teste_lista = [1, 2, 8, 10, 13, 15, 18, 20]
print(busca_binario(teste_lista, 5))
print(busca_binario(teste_lista, 15))
