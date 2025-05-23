import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

usuarios = ["Marta", "Cristiano Ronaldo", "Neymar", "Cristiana", "Debinha", "Messi"]
G.add_nodes_from(usuarios)

arestas = [
   ("Marta", "Cristiano Ronaldo"),
   ("Cristiano Ronaldo", "Neymar"),
   ("Neymar", "Cristiana"),
   ("Cristiana", "Debinha"),
   ("Debinha", "Marta"),
   ("Marta", "Neymar"),
   ("Messi", "Marta"),
   ("Messi", "Cristiana"),
]

G.add_edges_from(arestas)

print(f"Números de nós: {G.number_of_nodes()}")
print(f"Números de arestas: {G.number_of_edges()}")
print(f"Centralidade de Aglomeração (Clustering): {nx.clustering(G.to_undirected())}")
print(f"Coeficiente de Aglomeração (Clustering): {nx.clustering(G.to_undirected())}")

caminho = nx.shortest_path(G, source="Messi", target="Messi")
print(f"Caminho mais curto entre Messi e Neymar: {caminho}")

plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=5000, node_color="lightblue", font_size=10, font_weight="bold")
plt.title("Rede Social Simulada.")
plt.show()