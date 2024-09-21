class Node:
   """
      Classe que representa um nó em uma árvore de filmes por faixa etária
   """

   def __init__(self, value):
      self.value = value # Representação o nome da faixa etária ou o título do filme
      self.children = []
   
   def add_child(self, child_node):
      """
         Adiciona um nó filho a este nó.
      """
      self.children.append(child_node)
   
   def get_children(self):
      """
         Retorna a lista de filhos deste nó
      """
      return self.children

# Função para criar a estrutura de faixas etárias e filmes
def criar_estruturas_filmes():
    root = Node("Filmes por faixa etária: ")

    # Faixas etárias
    livre = Node("Livre")
    dez_anos = Node("10+")
    doze_anos = Node("12+")
    quatorze_anos = Node("14+")
    dezesseis_anos = Node("16+")
    dezoito_anos = Node("18+")

    # Adicionar as faixas etárias à raiz
    root.add_child(livre)
    root.add_child(dez_anos)
    root.add_child(doze_anos)
    root.add_child(dezesseis_anos)
    root.add_child(dezoito_anos)

    # Filmes para cada faixa etária
    livre.add_child(Node("O Rei Leão"))
    livre.add_child(Node("Frozen"))
    livre.add_child(Node("Toy Story"))

    dez_anos.add_child(Node("Harry Potter e a Pedra Filosofal"))
    dez_anos.add_child(Node("Procurando Nemo"))
    dez_anos.add_child(Node("Monstros S.A"))

    doze_anos.add_child(Node("Homem Aranha: De Volta ao Lar"))
    doze_anos.add_child(Node("Vingadores"))
    doze_anos.add_child(Node("Shrek"))

    quatorze_anos.add_child(Node("Pantera Negra"))
    quatorze_anos.add_child(Node("Velozes e Furiosos"))
    quatorze_anos.add_child(Node("Jurassic World"))

    dezesseis_anos.add_child(Node("Coringa"))
    dezesseis_anos.add_child(Node("Logan"))
    dezesseis_anos.add_child(Node("Mad Max: Estrada da Fúria"))

    dezoito_anos.add_child(Node("Clube da Luta"))
    dezoito_anos.add_child(Node("Pulp Fiction"))
    dezoito_anos.add_child(Node("O Poderoso Chefão"))

    return root

# Função para obter a idade mínimo de faixa etária
def obter_idade_minima(faixa_etaria):
   """
      Extrai a idade mínima da faixa etária a partir da string
   """
   if faixa_etaria == "Livre":
      return 0
   return int(faixa_etaria.split("+")[0])

# Função para recomendar filmes com base na idade do usuário
def recomendar_filmes(raiz, idade_usuario):
   """
      Retorna uma lista de filmes recomendados com base na idade do usuário.
      :param raiz: Nó raiz contendo as faixas etárias e filmes
      :param idade_usuario: Idade do usuário para filtrar as recomendações
      :return: Lista de títulos de filmes recomendados
   """
   recomendacoes = []

   # Percorre as faixas etárias
   for faixa in raiz.get_children():
      idade_minima = obter_idade_minima(faixa.value)

      # Condição se a idade do usuário for maior ou igual à idade mínima da faixa, adiciona os filmes
      if idade_usuario >= idade_minima:
         for filme in faixa.get_children():
            recomendacoes.append(filme.value)
   return recomendacoes

# Criando a estrutura de filmes por faixa etária
root = criar_estruturas_filmes()

# Testando as recomendações de filmes
print("Recomendações para idade 20: ")
print(recomendar_filmes(root, 20)) # Devolverá retorna filmes de todas as faixas

print("\nRecomendações para idade 13: ")
print(recomendar_filmes(root, 13)) # Devolverá retorna filmes até a faixa de 12+

print("\nRecomendações para idade 15: ")
print(recomendar_filmes(root, 15)) # Devolverá retorn filmes até a faixa de 14+

print("\nRecomendações para idade 9: ")
print(recomendar_filmes(root, 9)) # Devolverá retorna filmes da faixa 'Livre'
