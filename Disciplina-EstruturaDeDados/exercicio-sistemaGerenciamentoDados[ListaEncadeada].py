class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
   
class LinkedList:
   def __init__(self):
      self.head = None
      self.tail = None # Ponteiro para o último nó
   
   def insert_end(self, data):
      new_node = Node(data)
      if not self.head:
         # Se a lista estiver vazia, o novo nó é o head e o tail
         self.head = new_node
         self.tail = new_node
      else:
         # Atualiza o último nó e o ponteiro tail
         self.tail.next = new_node
         self.tail = new_node
   
   def search(self, target):
      current = self.head
      while current:
         if current.data == target:
            return True
         current = current.next
      return False
   
   def display(self):
      current = self.head
      while current:
         print(current.data, end=" -> ")
         current = current.next
      print("None")

# Exemplo de uso
lista = LinkedList()
lista.insert_end(10)
lista.insert_end(20)
lista.insert_end(30)

print("Lista: ")
lista.display()

print(f"Busca por 20: {lista.search(20)}") # Saída: True
print(f"Busca por 40: {lista.search(40)}") # Saída: False
