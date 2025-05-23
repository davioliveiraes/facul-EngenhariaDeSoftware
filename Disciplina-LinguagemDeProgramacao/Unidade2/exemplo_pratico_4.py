def buscar_binario(lista, elemento):
   minimo = 0
   maximo = len(lista)-1

   while minimo <= maximo:
      meio_lista = (minimo+maximo) // 2
      if lista[meio_lista] == elemento:
         return meio_lista
      elif elemento < lista[meio_lista]:
         maximo = meio_lista - 1
      else:
         minimo = meio_lista + 1
   return -1

numeros = [i * 5 for i in range(1, 21)]
elementos_para_buscar = [10, 25, 50, 100, 105]
resultados = {}

for elemento in elementos_para_buscar:
   indice = buscar_binario(numeros, elemento)
   if indice != -1:
      resultados[elemento] = f"Elemento: {elemento} foi encontrado no indice: {indice}"
   else:
      resultados[elemento] = f"Elemento: {elemento} não encontrado na lista."

for elemento, mensagem in resultados.items():
   print(mensagem)
