def busca_binario_condicional(lista, alvo, restricao):
   inicio, fim = 0, len(lista) - 1
   resultado = -1

   while inicio <= fim:
      meio = (inicio + fim) // 2
      if lista[meio] > alvo and lista[meio] % restricao == 0:
         resultado = lista[meio]
         fim = meio - 1
      elif lista[meio] <= alvo:
         inicio = meio + 1
      else:
         fim = meio - 1
   return resultado

lista_ordenada = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
alvo = 14
restricao = 3
resultado = busca_binario_condicional(lista_ordenada, alvo, restricao)

print(f"O menor número divisível por {restricao} e maior que {alvo} é: {resultado}")