# Insertion Sort - Ordenação por inserção
def insertion_sort(lista):
   for i in range(1, len(lista)):
      j = i - 1
      while j >= 0 and lista[j] > lista[j+1]:
         lista[j], lista[j+1] = lista[j+1], lista[j]
         j -= 1
   return lista

lista = [11, 10, 6, 5, 2, 1]
print(insertion_sort(lista))

# Improved Insertion Sort - Ordenação de Inserção Melhorada
def improved_insert_sort(lista):
   for i in range(1, len(lista)):
      j = i
      while j > 0 and lista[j] < lista[j-1]:
         lista[j], lista[j-1] = lista[j-1], lista[j]
         j -= 1
   return lista

lista = [5, 2, 4, 6, 1, 3]
print(improved_insert_sort(lista))

# Ordenação por inserção de forma decrescente
def insertion_sort_decres(lista):
   for i in range(1, len(lista)):
      j = i
      while j > 0 and lista[j] > lista[j-1]:
         lista[j], lista[j-1] = lista[j-1], lista[j]
         j -= 1
   return lista

lista = [5, 2, 4, 6, 1, 3]
print(insertion_sort_decres(lista))

# Casos de testes usando a função
def insertion_sort_case(lista):
   for i in range(1, len(lista)):
      j = i - 1
      tmp = lista[i]
      while j >= 0 and lista[j] > tmp:
         lista[j+1] = lista[j]
         j = j-1
      lista[j+1] = tmp
   return lista

# Função de teste
def test_insertion_sort():
   test_cases = [
       ([5, 2, 4, 6, 1, 3], [1, 2, 3, 4, 5, 6]), # Lista não ordenada
        ([], []),                                 # Lista vazia
        ([1], [1]),                               # Lista com um elemento
        ([2, 1], [1, 2]),                         # Lista com dois elementos
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),       # Lista já ordenada
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])
   ]

   for i, (input_list, expected_output) in enumerate(test_cases):
      result = insertion_sort_case(input_list[:])
      assert result == expected_output, f"Teste de caso: {i+1} Falhou: esperava - {expected_output}, mas obteve: {result}"
   
   print("Todos os casos de teste passaram!")

test_insertion_sort()

