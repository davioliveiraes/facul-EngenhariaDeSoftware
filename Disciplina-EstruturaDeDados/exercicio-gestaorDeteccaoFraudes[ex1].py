import networkx as nx

# Criando um grafo dirigido (para relações que tem direção) ou não dirigido

grafo = nx.Graph()

# Adicionando os nós(pessoas) e arestas (relações)
grafo.add_node("Francisca")
grafo.add_node("Jonatas")
grafo.add_node("Davi")
grafo.add_node("Roberta")

# adicionando conexões (arestas) entre as pessoas
grafo.add_edge("Francisca", "Jonatas", relation="parent")
grafo.add_edge("Jonatas", "Davi", relation="sibling")
grafo.add_edge("Davi", "Roberta", relation="spouse")
grafo.add_edge("Francisco", "Roberta", relation="cousin")

# Função para detectar conexões suspeitas
def detectar_conexoes_suspeitas(grafo):
   suspeitas = []
   for pessoa in grafo.nodes:
      # Exemplo simples: verificar se um nó tem mais de 3 conexões diretas
      conexoes = list(grafo.neighbors(pessoa))
      if len(conexoes) > 3:
         suspeitas.append(pessoa)
   return suspeitas

# Executando a função par encontrar conexões suspeitas
suspeitas = detectar_conexoes_suspeitas(grafo)
print(f"Pessoas com conexões suspeitas: {suspeitas}")

# Exemplo de busca por caminho entre dois indivíduos
caminho = nx.shortest_path(grafo, source="Francisca", target="Roberta")
print(f"Caminho entre Francisca e Roberta: {caminho}")

