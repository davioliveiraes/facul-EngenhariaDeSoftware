# A função range() pode ser usada de três formas distintas:
#A construção de uma sequência numérica poder ser feita com o comando range(). Ao consultar a documentação oficial, encontramos range() na lista de funções built-in em Python. Exemplos: 

seq1 = list(range(10))
print(seq1)
#Gerando uma sequência de 0 á 9.
#Output -  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

seq2 = list(range(1,11))
print(seq2)
#Gerando uma sequência de 0 á 10
#Output - [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

seq3 = list(range(0,30,5))
print(seq3)
#Gerando uma sequência de 0 a 30 com step = 5
#Output - [0, 5, 10, 15, 20, 25]

seq4 = list(range(0, -10, -1))
print(seq4)
#Gerando uma sequência númerica negativa.
#Output - [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

seq5 = list(range(0))
print(seq5)
#Gerando uma lista vazia
#Output - [] 