import matplotlib.pyplot as plt
import networkx as nx

edges = [
   ('Loja 1', 'Cliente 1'),
   ('Cliente 1', 'Cliente 2'),
   ('Cliente 3', 'Loja 3')
]

G = nx.Graph()
G.add_edges_from(edges)

pos = nx.spring_layout(G)
plt.figure(figsize=(10, 6))

nx.draw(
   G, pos,
   edge_color='gray',
   width=2,
   linewidths=1.5,
   node_size=600,
   node_color='lightblue',
   alpha=0.9
)

labels = {node: node for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels, font_size=12, font_color="black")

edge_labels = {
   ('Loja 1', 'Cliente 1'): 'Transações: 2',
   ('Cliente 1', 'Cliente 2'): 'Transações: 5',
   ('Cliente 3', 'Loja 3'): 'Transações: 7'
}

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10)

plt.axis('off')
plt.show()
