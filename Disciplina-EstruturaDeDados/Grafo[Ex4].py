from collections import deque

def bfs(grafo, inicio):
   visitados = set() # Conjunto para armazenar os vértices visitados
   fila = deque([inicio]) # Fila para armazenar os vértices a serem explorados, começando pelo vértice inicial

   while fila:
      vertice_atual = fila.popleft() # Remove o elemento mais à esquerda da fila

      if vertice_atual not in visitados:
         visitados.add(vertice_atual) # Marca o vértice como visitado
         print(vertice_atual, end=' ') # Exibe o vértice visitado
      
         # Adiciona todos os vizinhos são visitados do vértice atual à fila
         for vizinha in grafo[vertice_atual]:
            if vizinha not in visitados:
               fila.append(vizinha)

grafo = {
   'A': ['B', 'C'],
   'B': ['A', 'D', 'E'],
   'C': ['A', 'F'],
   'D': ['B'],
   'E': ['B', 'F'],
   'F': ['C', 'E']
}

# Inicio a busca em largura a partir do vértice 'A'
print("Busca em largura (BFS) a partir do vértice 'A': ")
bfs(grafo, 'A')
