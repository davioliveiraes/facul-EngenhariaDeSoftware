class Grafo:
   def __init__(self, vertices):
      self.V = vertices
      self.arestas = []
   
   def adicionar_aresta(self, u, v, peso):
      if u < 0 or v < 0 or u >= self.V or v >= self.V:
         print(f"Aresta inválida: ({u}, {v}) fora dos limites dos vértices.")
         return
      self.arestas.append([u, v, peso])
   
   def encontrar(self, pai, i):
      if pai[i] == i:
         return i
      return self.encontrar(pai, pai[i])
   
   def unir(self, pai, rank, x, y):
      raiz_x = self.encontrar(pai, x)
      raiz_y = self.encontrar(pai, y)

      if rank[raiz_x] < rank[raiz_y]:
         pai[raiz_x] = raiz_y
      elif rank[raiz_x] > rank[raiz_y]:
         pai[raiz_y] = raiz_x
      else:
         pai[raiz_y] = raiz_x
         rank[raiz_x] += 1

   def kruskal(self):
      resultado = []
      i, e = 0, 0
      self.arestas = sorted(self.arestas, key=lambda item: item[2])
      pai = []
      rank = []

      for no in range(self.V):
         pai.append(no)
         rank.append(0)
      
      while e < self.V - 1:
         u, v, peso = self.arestas[i]
         i = i + 1
         x = self.encontrar(pai, u)
         y = self.encontrar(pai, v)

         if x != y:
            e = e + 1
            resultado.append([u, v, peso])
            self.unir(pai, rank, x, y)
         
      print("Árvore Geradora Mínima (MST): ")
      for u, v, peso in resultado:
         print(f"Aresta ({u}, {v}) com peso: {peso}")

g = Grafo(4)
g.adicionar_aresta(0, 1, 10)
g.adicionar_aresta(0, 2, 6)
g.adicionar_aresta(0, 3, 5)
g.adicionar_aresta(1, 3, 15)
g.adicionar_aresta(2, 3, 4)

g.kruskal()
         