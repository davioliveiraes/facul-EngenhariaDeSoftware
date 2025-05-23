def bubble_sort_optimized(lista):
   i = len(lista)-1
   while i >= 1:
      ch =  -1
      for j in range(0, i):
         if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
            ch = j
      i = ch
   return lista

def test_bubble_sort_optimized():
   test_cases = [
      ([5, 2, 4, 6, 1, 3], [1, 2, 3, 4, 5, 6]),
      ([], []),
      ([1], [1]),
      ([2, 1], [1, 2]),
      ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
      ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])
   ]

   for i, (input_list, expected_output) in enumerate(test_cases):
      result = bubble_sort_optimized(input_list[:])
      assert result == expected_output, f"Teste caso {i+1} falhou: esperado {expected_output} mas obteve {result}"

      print("Todos os testes de caso passaram.")

test_bubble_sort_optimized()
