class Grafo:
   def __init__(self):
      self.grafo = {}
   
   def adicionar_vertice(self, vertice):
      if vertice not in self.grafo:
         self.grafo[vertice] = []
   
   def adicionar_aresta(self, vertice1, vertice2):
      if vertice1 in self.grafo and vertice2 in self.grafo:
         self.grafo[vertice1].append(vertice2)
         self.grafo[vertice2].append(vertice1)
      
   def mostrar_grafo(self):
      for vertice in self.grafo:
         print(f"{vertice} -> {self.grafo[vertice]}")
   
   def buscar_em_profundidade(self, inicio, visitados=None):
      if visitados is None:
         visitados = set()
      visitados.add(inicio)
      print(inicio, end=" ")
      for vizinho in self.grafo[inicio]:
         if vizinho not in visitados:
            self.buscar_em_profundidade(vizinho, visitados)
   
   def buscar_em_largura(self, inicio):
      visitados = set()
      fila = [inicio]
      visitados.add(inicio)
      while fila:
         vertice = fila.pop(0)
         print(vertice, end=" ")
         for vizinho in self.grafo[vertice]:
            if vizinho not in visitados:
               fila.append(vizinho)
               visitados.add(vizinho)

g = Grafo()
g.adicionar_vertice("A")
g.adicionar_vertice("B")
g.adicionar_vertice("C")
g.adicionar_vertice("D")
g.adicionar_vertice("E")

g.adicionar_aresta("A", "B")
g.adicionar_aresta("A", "C")
g.adicionar_aresta("B", "D")
g.adicionar_aresta("C", "D")
g.adicionar_aresta("D", "E")

g.mostrar_grafo()

print("\nBusca em Profundidade: ")
g.buscar_em_profundidade(input("Digite profundidade buscada: "))

print("\n\nBusca em Largura: ")
g.buscar_em_profundidade(input("Digite largura buscada: "))
