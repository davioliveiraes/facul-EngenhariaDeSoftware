grafo = {
   'D': {'A': 2, 'B': 4},
   'A': {'D': 2, 'C': 1, 'B': 3},
   'B': {'A': 3, 'D': 4, 'E': 2},
   'C': {'A': 1, 'F': 4},
   'E': {'B': 2, 'F': 3},
   'F': {'C': 4, 'E': 3}
}

def dijkstra(grafo, inicio):
   menor_distancia = {}
   antecessor = {}
   nao_visitados = grafo.copy()
   infinito = float('inf')
   caminho = []

   for vertice in nao_visitados:
      menor_distancia[vertice] = infinito
   menor_distancia[inicio] = 0

   while nao_visitados:
      vertice_minimo = None

      for vertice in nao_visitados:
         if vertice_minimo is None:
            vertice_minimo = vertice
         elif menor_distancia[vertice] < menor_distancia[vertice_minimo]:
            vertice_minimo = vertice
      
      for vertice_adjacente, peso in grafo[vertice_minimo].items():
         if peso + menor_distancia[vertice_minimo] < menor_distancia[vertice_adjacente]:
            menor_distancia[vertice_adjacente] = peso + menor_distancia[vertice_minimo]
            antecessor[vertice_adjacente] = vertice_minimo
      
      nao_visitados.pop(vertice_minimo)
   
   vertice_atual = min(menor_distancia, key=menor_distancia.get)
   while vertice_atual is not None:
      caminho.insert(0, vertice_atual)
      vertice_atual = antecessor.get(vertice_atual, None)
   return menor_distancia, caminho

distancias, caminho = dijkstra(grafo, 'D')
print(f"Melhores distâncias a partir de 'D': {distancias}")
print(f"Caminho mais curto: {caminho}")