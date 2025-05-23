class Node:
   def __init__(self, id):
      self.id = id
      self.next = None

class Queue:
   def __init__(self):
      self.head = None
      self.tail = None
   
   def enqueue(self, id):
      new_node = Node(id)
      if self.tail:
         self.tail.next = new_node
      self.tail = new_node
      if not self.head:
         self.head = new_node
      
   def dequeue(self):
      if not self.head:
         return None
      removed_id = self.head.id
      self.head = self.head.next
      if not self.head:
         self.tail = None
      return removed_id

# Exemplo de uso
process_queue = Queue()
process_queue.enqueue(1)
process_queue.enqueue(2)
process_id = process_queue.dequeue()