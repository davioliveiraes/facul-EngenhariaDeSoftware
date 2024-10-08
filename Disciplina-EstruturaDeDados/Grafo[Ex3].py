class Grafo:
   def __init__(self):
      self.grafo = {} # Dicionário para armazenar os vértices e suas adjacências
   
   def adicionar_vertice(self, vertice):
      if vertice not in self.grafo:
         self.grafo[vertice] = [] # Adiciona o vértice com uma lista de adjacências vazia
   
   def adicionar_aresta(self, vertice_origem, vertice_destino):
      if vertice_origem in self.grafo:
         self.grafo[vertice_origem].append(vertice_destino)
      else:
         print(f"ERRO: O vértice {vertice_origem} não existe no grafo.")
   
   def dfs(self, vertice, visitados=None):
      if vertice not in self.grafo:
         print(f"ERRO: O vértice {vertice} não está no grafo.")
         return

      if visitados is None:
         visitados = set() # Conjunto para armazenar vértices visitados
      
      visitados.add(vertice)
      print(vertice, end=' ') # Exibe o vértice visitado

      for vizinho in self.grafo[vertice]:
         if vizinho not in visitados:
            self.dfs(vizinho, visitados) # Chamada recursiva para visitar os vizinhos

# Exemplo de uso do grafo
g = Grafo()

# Adiciona vértices
g.adicionar_vertice('A')
g.adicionar_vertice('B')
g.adicionar_vertice('C')
g.adicionar_vertice('D')
g.adicionar_vertice('E')

# Adiciona arestas
g.adicionar_aresta('A', 'B')
g.adicionar_aresta('A', 'C')
g.adicionar_aresta('B', 'D')
g.adicionar_aresta('C', 'E')

# Executa a busca em profundidade (DFS)
print("Busca em profundidade a partir do vértice 'A': ")
g.dfs('A')
