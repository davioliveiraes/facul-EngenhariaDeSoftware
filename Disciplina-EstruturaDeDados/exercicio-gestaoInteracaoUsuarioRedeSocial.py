class Grafo:
   def __init__(self):
      self.adjacencias = {}

   def adicionar_vertice(self, vertice):
      if vertice not in self.adjacencias:
         self.adjacencias[vertice] = []
   
   def adicionar_aresta(self, vertice_origem, vertice_destino):
      self.adicionar_vertice(vertice_origem)
      self.adicionar_vertice(vertice_destino)
      self.adjacencias[vertice] = []
   
   def adicionar_aresta(self, vertice_origem, vertice_destino):
      self.adicionar_vertice(vertice_origem)
      self.adicionar_vertice(vertice_destino)
      self.adjacencias[vertice_origem].append(vertice_destino)
   
   def grau_estrada(self, vertice):
      grau = 0
      for vizinho in self.adjacencias.values():
         if vertice in vizinho:
            grau += 1
      return grau
   
   def identificar_influenciadores(self):
      influenciadores = []
      for usuario in self.adjacencias:
         grau_estrada_usuario = self.grau_estrada(usuario)
         if all(grau_estrada_usuario > self.grau_estrada(vizinho) for vizinho in self.adjacencias[usuario]):
            influenciadores.append(usuario)
      
      if not influenciadores:
         print("Nenhum influencidor identificado.")
      return influenciadores

rede_social = Grafo()
rede_social.adicionar_aresta('Alice', 'Bob')
rede_social.adicionar_aresta('Alice', 'Carol')
rede_social.adicionar_aresta('Bob', 'Alice')
rede_social.adicionar_aresta('Bob', 'Dave')
rede_social.adicionar_aresta('Carol', 'Alice')
rede_social.adicionar_aresta('Carol', 'Dave')
rede_social.adicionar_aresta('Dave', 'Bob')
rede_social.adicionar_aresta('Dave', 'Carol')
rede_social.adicionar_aresta('Dave', 'Eve')
rede_social.adicionar_aresta('Eve', 'Dave')

influencidores = rede_social.identificar_influenciadores()

if influencidores:
   print(f"Influencidores identificados: {influencidores}")
else:
   print("Nenhum influenciador encontrado.")