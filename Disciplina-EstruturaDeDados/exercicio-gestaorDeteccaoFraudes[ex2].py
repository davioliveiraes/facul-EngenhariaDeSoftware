import networkx as nx

grafo = nx.Graph()

pessoas = ["Harvey", "Mike", "Louis", "Rachel", "Donna", "Jessica", "Katrina", "Alex"]

grafo.add_nodes_from(pessoas)

grafo.add_edge("Harvey", "Mike", relation="parent")
grafo.add_edge("Mike", "Louis", relation="sibling")
grafo.add_edge("Louis", "Rachel", relation="spouse")
grafo.add_edge("Rachel", "Donna", relation="cousin")
grafo.add_edge("Dona", "Jessica", relation="friend")
grafo.add_edge("Katrina", "Donna", relation="colleague")
grafo.add_edge("Harvey", "Louis", relation="neighbor")
grafo.add_edge("Donna", "Mike", relation="uncle")
grafo.add_edge("Alex", "Louis", relation="business")
grafo.add_edge("Katrina", "Alex", relation="sibling")

def detectar_conexoes_suspeitas(grafo):
   suspeitas = []
   for pessoa in grafo.nodes:
      conexoes = list(grafo.neighbors(pessoa))
      if len(conexoes) > 3:
         suspeitas.append(pessoa)
   return suspeitas

suspeitas = detectar_conexoes_suspeitas(grafo)
print(f"Pessoas com conexões suspeitas: {suspeitas}")

caminho = nx.shortest_path(grafo, source="Harvey", target="Donna")
print(f"Caminho entre Harvey e Donna: {caminho}")