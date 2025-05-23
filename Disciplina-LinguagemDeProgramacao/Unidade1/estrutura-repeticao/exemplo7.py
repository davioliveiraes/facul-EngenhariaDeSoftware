# Exercicio procura letras e posição
# Criando uma solução que procura pelas vogais 'a' e 'o', informando que encontramos e qual posição do texto ela está.

texto = "A inserção de comentários no código do programa é uma prática normal. Em função disso, toda linguagem de programação tem alguma maneira de permitir que comentários sejam inseridos nos programas. O objetivo é adicionar descrições em partes do código, seja par a documentálo ou para adicionar uma descrição do algoritmo implementado (BANIN, p. 45, 2018)."

for i, c in enumerate(texto):
   if c == 'a' or c == 'o':
      print(f"Achamos a vogal: {c} - na posição: {i}°")
   else:
      continue
