import sys
import heapq

class Grafo:
   def __init__(self, vertices):
      self.V = vertices
      self.grafo = [[0] * vertices for _ in range(vertices)]
   
   def imprimir_caminho(self, antecessores, j):
      if antecessores[j] == -1:
         print(j, end=' ')
         return
      self.imprimir_caminho(antecessores, antecessores[j])
      print(j, end=' ')
   
   def dijkstra(self, origem):
      distancia = [sys.maxsize] * self.V
      distancia[origem] = 0
      antecessores = [-1] * self.V
      visitados = [False] * self.V
      fila_prioridade = [(0, origem)]

      while fila_prioridade:
         dist_atual, u = heapq.heappop(fila_prioridade)
         if visitados[u]:
            continue
         visitados[u] = True

         for v in range(self.V):
            if self.grafo[u][v] > 0 and not visitados[v]:
               nova_dist = dist_atual + self.grafo[u][v]
               if nova_dist < distancia[v]:
                  distancia[v] = nova_dist
                  antecessores[v] = u
                  heapq.heappush(fila_prioridade, (nova_dist, v))

      print("Vértice\tDistância\tCaminho")
      for i in range(self.V):
         print(f"{i}\t\t{distancia[i]}\t\t", end=' ')
         self.imprimir_caminho(antecessores, i)
         print()

g = Grafo(9)
g.grafo = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]

g.dijkstra(0)