def busca_binaria_matriz(matriz,  alvo):
   if not matriz or not matriz[0]:
      return (-1, -1)
   
   linhas, colunas = len(matriz), len(matriz[0])
   inicio, fim = 0, linhas * colunas - 1

   while inicio <= fim:
      meio = (inicio + fim) // 2
      linha, coluna = divmod(meio, colunas)
      valor = matriz[linha][coluna]

      if valor == alvo:
         return (linha, coluna)
      elif valor < alvo:
         inicio = meio + 1
      else:
         fim = meio - 1
   return (-1, -1)

matriz_ordenada = [
   [1, 3, 5, 7],
   [10, 11, 16, 20],
   [23, 30, 34, 50]
]

alvo = 16
resultado = busca_binaria_matriz(matriz_ordenada, alvo)
print(f"Valor {alvo} encontrado na posição: {resultado}")

alvo_inexistente = 25
resultado = busca_binaria_matriz(matriz_ordenada, alvo_inexistente)
print(f"Valor {alvo_inexistente} encontrado na posição: {resultado}")