class TreeNode:
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

class BinarySearchTree:
   def __init__(self):
      self.root = None
   
   def insert(self, data):
      if not self.root:
         self.root = TreeNode(data)
      else:
         self._insert_recursive(self.root, data)
   
   def _insert_recursive(self, node, data):
      if data < node.data:
         if not node.left:
            node.left = TreeNode(data)
         else:
            self._insert_recursive(node.left, data)
      else:
         if not node.right:
            node.right = TreeNode(data)
         else:
            self._insert_recursive(node.right, data)
   
   def search(self, target):
      return self._search_recursive(self.root, target)
   
   def _search_recursive(self, node, target):
      if not node:
         return False
      if node.data == target:
         return True
      elif target < node.data:
         return self._search_recursive(node.left, target)
      else:
         return self._search_recursive(node.right, target)
   
   def inorder_traversal(self, node=None):
      if node is None:
         node = self.root
      if node.left:
         self.inorder_traversal(node.left)
      print(node.data, end=" ")
      if node.right:
         self.inorder_traversal(node.right)

# Exemplo de uso:
bst = BinarySearchTree()
bst.insert(10)
bst.insert(20)
bst.insert(5)
bst.insert(15)

print("Árvore BST em ordem: ")
bst.inorder_traversal()
print()

print(f"Busca por 15: {bst.search(15)}") # Saída: True
print(f"Busca por 25: {bst.search(25)}") # Saída: False
   