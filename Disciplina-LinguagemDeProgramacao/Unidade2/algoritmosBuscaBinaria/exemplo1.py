def executar_buscar_binaria(lista, valor):
   minimo = 0
   maximo = len(lista) - 1

   while minimo <= maximo:
      divmeio = (minimo + maximo) // 2
      if valor < lista[divmeio]:
         maximo = divmeio - 1
      elif valor > lista[divmeio]:
         minimo = divmeio + 1
      else:
         return True
   return False

busca_binaria = executar_buscar_binaria([2, 6, 7, 10, 15, 20], 10)
print(busca_binaria)
