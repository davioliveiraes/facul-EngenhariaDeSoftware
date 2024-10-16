class Grafo:
   def __init__(self, orientado=True):
      self.orientado = orientado
      self.adjacencias = {}
   
   def inserir_arestas(self, arestas):
      """
         Insere um conjunto de arestas no grafo
      """
      for u, v in arestas:
         self.adicionar_aresta(u, v)
   
   def adicionar_aresta(self, u, v):
      """
         Adiciona uma aresta (u, v) ao grafo
      """
      if u not in self.adjacencias:
         self.adjacencias[u] = []
      self.adjacencias[u].append(v)

      if not self.orientado:
         if v not in self.adjacencias:
            self.adjacencias[v] = []
         self.adjacencias[v].append(u)
      
   def remover_aresta(self, u, v):
      """
         Remove uma aresta (u, v) do grafo
      """
      if u in self.adjacencias and v in self.adjacencias[u]:
         self.adjacencias[u].remove(v)
      if not self.orientado and v in self.adjacencias and u in self.adjacencias[v]:
         self.adjacencias[v].remove(u)
   
   def imprimir(self):
      """
         Imprime a representação do grafo
      """
      for vertice, vizinhos in self.adjacencias.items():
         print(f"{vertice} -> {', '.join(vizinhos)}")

def busca_em_largura(grafo, inicio):
   """
      Realiza busca em largura a partir de um vértice de início.
   """
   visitados = set()
   fila = [inicio]

   while fila:
      vertice = fila.pop(0)
      if vertice not in visitados:
         visitados.add(vertice)
         if vertice in grafo.adjacencias:
            for vizinho in grafo.adjacencias[vertice]:
               if vizinho not in visitados:
                  fila.append(vizinho)
   return visitados

# Função para verificar os caminhos alternativos 
def verificar_caminhos_alternativos(arestas, orientado=True):
   """
      Verifica para cada aresta se há um caminho alternativo caso ela seja removida do grafo
   """
   def criar_grafo_com_arestas(arestas, orientado):
      grafo = Grafo(orientado)
      grafo.inserir_arestas(arestas)
      return grafo
   
   for u, v in arestas:
      print(f"\nRemovendo aresta ({u}, {v})")

      # Criar o grafor e remover a aresta atual
      grafo = criar_grafo_com_arestas(arestas, orientado)
      grafo.remover_aresta(u, v)

      # Busca em largura a partir do vértice u
      visitados = busca_em_largura(grafo, u)
      
      # Verifica se ainda há um caminho alternativo
      if v in visitados:
         print(f"Sim, há caminho alternativo entre {u} e {v}.")
      else:
         print(f"Não há caminho alternativo entre {u} e {v}.")

# Exemplo de arestas para testar
arestas1 = [
   ('J', 'K'), ('J', 'N'), ('N', 'P'), ('P', 'C'), ('C', 'Q'),
   ('C', 'J'), ('Q', 'M'), ('M', 'L'), ('L', 'C'), ('K', 'L')
]

arestas2 = [
   ('E', 'D'), ('E', 'F'), ('E', 'A'), ('D', 'A'), ('D', 'I'),
   ('A', 'H'), ('I', 'A'), ('I', 'H'), ('H', 'G'), ('G', 'A'),
   ('G', 'B'), ('B', 'F'), ('F', 'A')
]

# Verificar caminhos alternativos nos dois conjuntos de arestas
print("Testando arestas orientadas: ")
verificar_caminhos_alternativos(arestas1, orientado=True)

print("\nTestando arestas não orientadas: ")
verificar_caminhos_alternativos(arestas2, orientado=False)
