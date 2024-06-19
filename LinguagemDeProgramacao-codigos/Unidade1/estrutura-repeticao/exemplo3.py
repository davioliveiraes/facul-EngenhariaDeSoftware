# Com o comando for, podemos usar a função enumerate() para retorna á posição de cada item, dentro da sequência. Considerando
# o exemplo dado, no qual atribuímos a variável "nome" o valor de "Dawidh", "G" ocupa a posição () na sequência, "u" ocupa a posição 1,
# "i" a posição 2, e assim por diante. Veja que a variável "i" é usada para capturar a posição e a variável "c" cada caractere da palavra.

nome = "Dawidh"
for i, l in enumerate(nome):
   print(f"Posição: {i} - Letra: {l}")

