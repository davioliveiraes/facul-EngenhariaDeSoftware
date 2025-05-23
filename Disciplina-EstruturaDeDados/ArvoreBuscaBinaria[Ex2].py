class Node:
   """
      Classe que representa um nó da árvore binária de busca
   """
   def __init__(self, key):
      self.left = None
      self.right = None
      self.key = key
   
class ArvoreBB:
   """
      Classe que representa uma árvore binária de busca.
   """
   def __init__(self):
      self.root = None
   
   def inserir(self, key):
      """
         Insere um nó com a chave especificada na árvore.
      """
      if self.root is None:
         self.root = Node(key)
      else:
         self._inserir_recursivo(self.root, key)
   
   def _inserir_recursivo(self, current_node, key):
      """
         Função auxiliar para inserção recursiva.
      """
      if key < current_node.key:
         if current_node.left is None:
            current_node.left = Node(key)
         else:
            self._inserir_recursivo(current_node.left, key)
      else:
         if current_node.right is None:
            current_node.right = Node(key)
         else:
            self._inserir_recursivo(current_node.right, key)
   
   def remover(self, key):
      """
         Remove um nó com a chave especificado da árvore
      """
      self.root = self._remover_recursivo(self.root, key)
   
   def _remover_recursivo(self, current_node, key):
      """
      Função auxiliar para remoção recursiva.
      """
      if current_node is None:
         return current_node
      
      if key < current_node.key:
         current_node.left = self._remover_recursivo(current_node.left, key)
      elif key > current_node.key:
         current_node.right = self._remover_recursivo(current_node.right, key)
      else:
         if current_node.left is None:
            return current_node.right
         elif current_node.right is None:
            return current_node.left
      
         # Substitui o valor de nó pela chave mínima do lado direito
         current_node.key = self._buscar_valor_min(current_node.right)
         # Remove o nó substituto
         current_node.right = self._remover_recursivo(current_node.right, current_node.key)
   
      return current_node

   def _buscar_valor_min(self, node):
      """
         Encontra o menor valor a partir de um nó
      """
      while node.left is not None:
         node = node.left
      return node.key

   def buscar(self, key):
      """
         Busca um nó na árvore pela chave
      """
      return self._buscar_recursivo(self.root, key)

   def _buscar_recursivo(self, current_node, key):
      """
         Função auxiliar para busca resursiva.
      """
      if current_node is None or current_node.key == key:
         return current_node
      if key < current_node.key:
         return self._buscar_recursivo(current_node.left, key)
      return self._buscar_recursivo(current_node.right, key)

   def in_order_traversal(self, node):
      """
         Exibe os nós da árvore em ordem crescente (in-order).
      """
      if node:
         self.in_order_traversal(node.left)
         print(node.key, end=" ")
         self.in_order_traversal(node.right)

# Exemplo de uso
bst = ArvoreBB()

# Inserindo nós
bst.inserir(3) # Adiciona tarefa com prioridade 3
bst.inserir(1) # Adiciona tarefa com prioridade 1
bst.inserir(4) # Adiciona tarefa com prioridade 4

# Exibe a árvore em ordem para verificar a inserção
print("Árvore após inserção (in-order): ")
bst.in_order_traversal(bst.root)
print("\n")

# Verifica se a tarefa com prioridade 1 existe
print(f"Tarefa com prioridade 1 existe? {bst.buscar(1) is not None}")

# Remove a tarefa com prioridade 3
bst.remover(3)

# Exibe a árvore com prioridade 3
bst.remover(3)

# Exibe a árvore em ordem para verificar a remoção
print("\nÁrvore após remover a tarefa com prioridade 3 (in-order): ")
bst.in_order_traversal(bst.root)
print("\n")

# Verifica se a tarefa com prioridade 3 ainda existe
print(f"Tarefa com prioridade 3 existe? {bst.buscar(3) is not None}")