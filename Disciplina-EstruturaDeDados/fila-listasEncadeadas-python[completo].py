class Node:
   def __init__(self, id):
      self.id = id
      self.next = None

class Queue:
   def __init__(self):
      self.head = None
      self.tail = None
   
   def is_empty(self):
      # Verificando se a fila está fazia
      return self.head is None
   
   def enqueue(self, id):
      # Adicionando um novo elemento ao final da fila
      new_code = Node(id)
      if self.tail:
         self.tail.next = new_code
      self.tail = new_code
      if not self.head:
         self.head = new_code
      print(f"Enfileirado: {id}")

   def dequeue(self):
      # Remove o elemento do início da fila e retorna seu id.
      # Retorna None se a fila estiver vazia.abs
      if self.is_empty():
         print("Lista está vazia. Não é possível desfileirar")
         return None
      removed_id = self.head.id
      self.head = self.head.next
      if not self.head:
         self.tail = None
      print(f"Defilado: {removed_id}")
      return removed_id
   
   def peek(self):
      # Retorna o id do lemento no início da fila sem removê-lo.
      # Retorna None se a fila estiver vazia.
      if self.is_empty():
         print(f"A lista está vazia. Não pode espiar.")
         return None
      return self.head.id
   
   def display(self):
      # Mostra todos os elementos da fila.abs
      if self.is_empty():
         print("A lista está vazia.")
         return
      current = self.head
      elements = []
      while current:
         elements.append(current.id)
         current = current.next
      print("Fila: ", " -> ".join(map(str, elements)))

# Exemplo de uso
process_queue = Queue()
process_queue.enqueue(1)
process_queue.enqueue(2)
process_queue.enqueue(3)
process_queue.display() # Mostra a fila atual
process_id = process_queue.dequeue() # Remove o primeiro elemento
process_queue.display() # Mostrando a fila após a remoção
peeked_id = process_queue.peek() # Visualiza o próximo a ser removido
print(f"Próxima da fila: {peeked_id}")