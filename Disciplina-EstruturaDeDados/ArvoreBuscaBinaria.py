class Node:
   """
      Classe que representa um nó da árvore binária de busca.
   """
   def __init__(self, key):
      self.left = None # Subárvore à esqurda
      self.right = None # Subárvore à direita
      self.val = key # Valor armazenado no nó
   
def inserir(node, key):
   """
      Função para inserir um novo nó com a chave 'key' na árvore
      :param node: Nó atual da árvore
      :param key: Valor a ser inserido na árvore
      :return: Nó raiz após a inserção
   """
   # Se a árvore estiver vazia, cria im novo nó e o retorna
   if node is None:
      return Node(key)
      
   # Caso contrário, desce pela árvore recursivamente
   if key < node.val:
      # Se o valor é menor que o valor do nó atual, vai para esquerda
      node.left = inserir(node.left, key)
   else:
      # Se o valor é maior, vai para a direita
      node.right = inserir(node.right, key)
      
   return node

def in_order_traversal(root):
   """
      Realiza o percurso em ordem (in-order) da árvore e imprime os valores.
      Esse método imprime a árvore de forma ordenada.
   """
   if root:
      in_order_traversal(root.left) # Visista a subárvore à esquerda
      print(root.val, end=' ') # Imprime o valor do nó atual
      in_order_traversal(root.right) # Visita a subárvore à direita

# Testando a inserção na árvore
raiz = Node(14) # Cria a raiz com o valor 14

# Sequência de inserção de nós
sequence = [4, 18, 0, 21, 17, 1, 8, 13]

# Inserindo os valores de nós
for key in sequence:
   inserir(raiz, key)

# Exibindo a árvore em ordem para verificar a estrutura
print(f"Árvore em ordem (in-order traversal): ")
in_order_traversal(raiz) # Deverá exibir os valores em ordem crescente