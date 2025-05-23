import networkx as nx
import matplotlib.pyplot as plt

class GrafoVisualizacao:

   def __init__(self):
      self.arestas = []
   
   def adicionar_aresta(self, vertice1, vertice2):
      self.arestas.append((vertice1, vertice2))
   
   def desenhar(self, node_color='lightblue', edge_color='gray', node_size=1000, font_size=10):
      G = nx.Graph()
      G.add_edges_from(self.arestas)

      plt.figure(figsize=(8, 6))
      nx.draw_networkx(
         G,
         node_color=node_color,
         edge_color=edge_color,
         node_size=node_size,
         font_size=font_size,
         with_labels=True,
         font_color='black'
      )
      plt.title("Visualização do Grafo")
      plt.show()

grafo = GrafoVisualizacao()

grafo.adicionar_aresta("Davi", "Conta Poupança")
grafo.adicionar_aresta("Davi", "Roberta")
grafo.adicionar_aresta("Roberta", "Conta Poupança")
grafo.adicionar_aresta("Davi", "Conta Corrente")
grafo.adicionar_aresta("Victor", "Conta Corrente")

grafo.desenhar(node_color="lightgreen", edge_color="blue", node_size=1200, font_size=12)