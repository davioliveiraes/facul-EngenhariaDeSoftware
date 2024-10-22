import itertools

class Grafo:
   def __init__(self, orientado=False):
      self._lista_de_adjacencias = dict()
      self.orientado = orientado
   
   @property
   def vertices(self):
      return set(self._lista_de_adjacencias.keys())
   
   def arestas(self):
      arestas_do_grafo = []
      for v_origem in self.vertices:
         arestas_do_grafo += self.v_arestas(v_origem)
      return arestas_do_grafo
   
   def v_arestas(self, v_origem):
      return [(v_origem, v_destino, custo) for v_destino, custo in self._lista_de_adjacencias[v_origem]]
   
   def inserir_aresta(self, u, v, custo):
      self._lista_de_adjacencias.setdefault(u, [])
      self._lista_de_adjacencias.setdefault(v, [])
      self._lista_de_adjacencias[u].append((v, custo))
      if not self.orientado:
         self._lista_de_adjacencias[v].append((u, custo))
   
   def inserir_arestas(self, arestas):
      for aresta in arestas:
         self.inserir_aresta(*aresta)
   
   def imprimir(self):
      total = 0
      for u, v, custo in self.arestas():
         print(f"{u} -- {v} => {custo:.2f}")
         total += custo
      if not self.orientado:
         total /= 2
      print(f"Custo total: {total:.2f}")

def kruskal(grafo):
   arestas_mst = set()
   conjuntos = {v: {v} for v in grafo.vertices}
   arestas_ordenadas = sorted(grafo.arestas(), key=lambda aresta: aresta[-1])

   for u, v, custo in arestas_ordenadas:
      if conjuntos[u].isdisjoint(conjuntos[v]):
         arestas_mst.add((u, v, custo))
         uniao = conjuntos[u] | conjuntos[v]
         for vertice in uniao:
            conjuntos[vertice] = uniao
   
   mst = Grafo()
   mst.inserir_arestas(arestas_mst)
   return mst

def solicitar_locais():
   qtd = int(input("Digite a quantidade de locais: "))
   locais = []
   for i in range(qtd):
      local = input(f"Digite o nome do local {i+1}: ")
      locais.append(local)
   return locais

def solicitar_distancias(locais):
   distancias = []
   for u, v in itertools.combinations(locais, 2):
      distancia = float(input(f"Digite a distância entre {u} e {v}: "))
      distancias.append((u, v, distancia))
   return distancias

print("Exemplo com locais e distâncias predefinidos: ")
arestas_predefinidas = [
   ('Parquinho', 'Lago', 2.2),
   ('Quadras', 'Lago', 5.5),
   ('Parquinho', 'Quadras', 8.6),
   ('Lanchonete', 'Lago', 6.0),
]

g1 = Grafo()
g1.inserir_arestas(arestas_predefinidas)
mst = kruskal(g1)
mst.imprimir()

print("\nAgora você pode inserir seus próprios locais e distâncias: ")
locais = solicitar_locais()
arestas_usuario = solicitar_distancias(locais)
g2 = Grafo()
g2.inserir_arestas(arestas_usuario)
mst_usuario = kruskal(g2)
mst_usuario.imprimir()
