import random

class Grafo:
   def __init__(self):
      self.grafo = {}
   
   def adicionar_vertice(self, v):
      if v not in self.grafo:
         self.grafo[v] = []
   
   def adicionar_aresta(self, u, v):
      self.grafo[u].append(v)
      self.grafo[v].append(u)
   
   def vizinhos(self, v):
      return self.grafo[v]

class Formiga:
   def __init__(self, nome, posicao_inicial):
      self.nome = nome
      self.posicao_atual = posicao_inicial
   
   def mover_para(self, nova_posicao):
      self.posicao_atual = nova_posicao
      print(f"{self.nome} se moveu para {nova_posicao}")

class JogoDeFormigas:
   def __init__(self, grafo, formigas, comida):
      self.grafo = grafo
      self.formigas = formigas
      self.comida = comida
   
   def turno(self):
      for formiga in self.formigas:
         if formiga.posicao_atual == self.comida:
            print(f"{formiga.nome} encontrou a comida!")
            return True

         vizinhos = self.grafo.vizinhos(formiga.posicao_atual)
         if vizinhos:
            nova_posicao = random.choice(vizinhos)
            formiga.mover_para(nova_posicao)
      
      return False
   
   def jogar(self):
      encontrou_comida = False
      turnos = 0

      while not encontrou_comida:
         print(f"\n--- Turno {turnos + 1} ---")
         encontrou_comida = self.turno()
         turnos += 1
      
      print(f"\nO jogo terminou em {turnos} turnos.")

grafo = Grafo()
colonia = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
for c in colonia:
   grafo.adicionar_vertice(c)

grafo.adicionar_aresta('A', 'B')
grafo.adicionar_aresta('A', 'C')
grafo.adicionar_aresta('B', 'D')
grafo.adicionar_aresta('C', 'D')
grafo.adicionar_aresta('C', 'E')
grafo.adicionar_aresta('D', 'F')
grafo.adicionar_aresta('E', 'F')
grafo.adicionar_aresta('F', 'G')
grafo.adicionar_aresta('F', 'H')

formiga1 = Formiga("Formiga 1", 'A')
formiga2 = Formiga("Formiga 2", 'E')

comida = 'H'
jogo = JogoDeFormigas(grafo, [formiga1, formiga2], comida)
jogo.jogar()