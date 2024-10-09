class Node:
   def __init__(self, point, left=None, right=None):
      self.point = point # Ponto armazenado (x, y)
      self.left = left # Subárvore à esquerda
      self.right = right # Subárvore à direita
   
class KDTree:
   def __init__(self, dimension=2):
      self.dimension = dimension # Número de dimensões (2D neste caso)
      self.root = None # Raiz da árvore
   
   def inserir(self, root, point, depth=0):
      """ Insere um ponto na kd-tree """
      if root is None:
         return Node(point)
      
      # Calcula o eixo de comparação (alternando entre x e y)
      eixo = depth % self.dimension

      if point[eixo] < root.point[eixo]:
         root.left = self.inserir(root.left, point, depth + 1)
      else:
         root.right = self.inserir(root.right, point, depth + 1)
      
      return root
   
   def construir(self, pontos):
      """ Constrói a kd-tree a partir de uma lista de pontos """
      for ponto in pontos:
         self.root = self.inserir(self.root, ponto)
   
   def buscar_vizinho_mais_proximo(self, root, ponto, depth=0, melhor=None):
      if root is None:
         return melhor
      
      if melhor is None or self.distancia_quadrada(root.point, ponto) < self.distancia_quadrada(melhor, ponto):
         melhor = root.point

      eixo = depth % self.dimension
      proxima_subarvore = root.left if ponto[eixo] < root.point[eixo] else root.right
      outra_subarvore = root.right if ponto[eixo] < root.point[eixo] else root.left

      melhor = self.buscar_vizinho_mais_proximo(proxima_subarvore, ponto, depth + 1, melhor)

      if (ponto[eixo] - root.point[eixo])**2 < self.distancia_quadrada(melhor, ponto):
         melhor = self.buscar_vizinho_mais_proximo(outra_subarvore, ponto, depth + 1, melhor)
      
      return melhor
   
   def distancia_quadrada(self, ponto1, ponto2):
      """Calcula a distância Euclidiana ao quadrado entre dois pontos """
      return sum((p1 - p2) ** 2 for p1, p2 in zip(ponto1, ponto2))
   
# Exemplo de uso
pontos = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]

kd_tree = KDTree()
kd_tree.construir(pontos)

# Buscar o vizinho mais próximo de ponto (9, 2)
ponto_consulta = (9, 2)
vizinho_mais_proximo = kd_tree.buscar_vizinho_mais_proximo(kd_tree.root, ponto_consulta)

print(f"Vizinho mais próximo do ponto {ponto_consulta}: {vizinho_mais_proximo}")
      