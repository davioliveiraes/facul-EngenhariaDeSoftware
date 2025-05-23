def busca_sequencial(lista, valor):
   """
      Realiza uma busca sequencial em uma lsita para encontrar o valor desejado.

      Parâmetros:
      lista (list): A lista de elementos onde a busca será realizada.
      valor: O valor a ser buscado na lista.

      Retorna:
      int: O índice do valor se encontrado; -1 se não encontrado.
   """

   for i in range(len(lista)):
      if lista[i] == valor:
         return i # Retorna o índice onde o valor foi encontrado
   return -1 # Retorna -1 se o valor não estiver na lista

# Exemplo de uso
lista_exemplo = [10, 23, 45, 70, 11, 15]
valor_a_buscar = 70

resultado = busca_sequencial(lista_exemplo, valor_a_buscar)

if resultado != -1:
   print(f"Valor: {valor_a_buscar} encontrado no índice {resultado}.")
else:
   print(f"Valor: {valor_a_buscar} não encontrado na lista.")

# Teste com valor existente
print(busca_sequencial([1, 3, 5, 7, 9],5)) # Deve retornar 2 (índice do valor 5)

# Teste com valor inexistente
print(busca_sequencial([1, 3, 5, 7, 9], 4)) # Deve retorna -1 (valor não está na lista)

# Teste com valor no início da lista
print(busca_sequencial([10, 20, 30, 40, 50], 10)) # Deve retornar 0

# Teste com valor n o final da lista
print(busca_sequencial([10, 20, 30, 40, 50], 50)) # Deve retornar 4