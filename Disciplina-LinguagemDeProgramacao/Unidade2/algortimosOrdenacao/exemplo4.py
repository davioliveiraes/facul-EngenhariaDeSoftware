# teste pagando o valor máximo(maxsort)
def selection_sort(lista):
   for i in range(len(lista)-1, 0, -1):
      max_index = 0
      for j in range(1, i+1):
         if lista[max_index] < lista[j]:
            max_index = j
      lista[i], lista[max_index] = lista[max_index], lista[i]
   return lista

def test_selection_sort():
   test_cases = [
      ([5, 2, 4, 6, 1, 3], [1, 2, 3, 4, 5, 6]),
      ([], []),
      ([1], [1]),
      ([2, 1], [1, 2]),
      ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
      ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]) 
   ]

   for i, (input_list, exepected_output) in enumerate(test_cases):
      result = selection_sort(input_list[:])
      assert result == exepected_output, f"O caso de teste {i+i} falhou: esperado {exepected_output}, mas obeteve o resultado: {result}"

      print("Todos os teste de casos passaram!")

test_selection_sort()