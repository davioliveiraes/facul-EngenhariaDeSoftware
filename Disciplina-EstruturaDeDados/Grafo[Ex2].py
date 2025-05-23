class Grafo:
   def __init__(self):
      self.vertices = {} # Dicionário para armazenar os vértices e suas adjacências
   
   def adicionar_vertice(self, vertice):
      if vertice not in self.vertices:
         self.vertices[vertice] = [] # Inicializa a lista de adjacências vazia para o vértice
      else:
         print(f"Vértice: '{vertice}' já existe.")
   
   def adicionar_aresta(self, origem, destino, bidirecional=False):
      if origem not in self.vertices:
         print(f"Vértice de origem '{origem} não existe.'")
         return
      if destino not in self.vertices:
         print(f"Vértice de destino '{destino}' não existe.")
      
      # Evitar duplicação de aresta
      if destino not in self.vertices[origem]:
         self.vertices[origem].append(destino) # Adiciona destino à lista de adjacências de origem
      else:
         print(f"Aresta '{origem} -> {destino}' já existe.")
      
      # Se for bidirecional, adicionar a aresta inversa
      if bidirecional:
         if origem not in self.vertices[destino]:
            self.vertices[destino].append(origem)
         else:
            print(f"Aresta '{destino} -> {origem}' já existe.")
      
   def mostrar_vertices(self):
      print("\nVértices do Grafo: ")
      for vertice in self.vertices:
         print(f"  {vertice}")
   
   def mostrar_arestas(self):
      print("\nArestas do Grafo: ")
      for origem in self.vertices:
         for destino in self.vertices[origem]:
            print(f"  {origem} -> {destino}")

# Exemplo de uso
# Cria um objeto grafo
grafo = Grafo()

# Adicina vértices ao grafo
grafo.adicionar_vertice('A')
grafo.adicionar_vertice('B')
grafo.adicionar_vertice('C')
grafo.adicionar_vertice('D')

# Adicionar arestas ao grafo (unidirecional e bidirecional)
grafo.adicionar_aresta('A', 'B')
grafo.adicionar_aresta('A', 'C')
grafo.adicionar_aresta('B', 'C')
grafo.adicionar_aresta('C', 'D', bidirecional=True)

# Mostrar os vértices e as arestas do grafo
grafo.mostrar_vertices()
grafo.mostrar_arestas()