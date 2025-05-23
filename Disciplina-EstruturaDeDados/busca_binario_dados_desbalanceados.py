def busca_primeiro_um(lista):
   inicio, fim = 0, len(lista) - 1
   resultado = - 1

   while inicio <= fim:
      meio = (inicio + fim) // 2
      if lista[meio] == 1:
         resultado = meio
         fim = meio - 1
      else:
         inicio = meio + 1
   return resultado

lista_desbalanceado = [0,0,0,0,1,1,1,1,1]
resultado = busca_primeiro_um(lista_desbalanceado)
print(f"O primeiro '1' está na posição: {resultado}")