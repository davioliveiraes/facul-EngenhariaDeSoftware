class Fila:
   def __init__(self):
      self.items = []
   
   def enqueue(self, item):
      self.items.append(item)
   
   def dequeue(self):
      if not self.is_empty():
         return self.items.pop(0)
      else:
         return "A fila está vazia."
   
   def peek(self):
      if not self.is_empty():
         return self.items[0]
      else:
         return "A fila está vazia."

   def is_empty(self):
      return len(self.items) == 0
   
   def size(self):
      return len(self.items)
   
   def __str__(self):
      return str(self.items)
   
minha_fila = Fila()
print(minha_fila)

minha_fila.enqueue(1)
minha_fila.enqueue(2)
minha_fila.enqueue(3)
print(minha_fila)

print(minha_fila.dequeue()) 
print(minha_fila)

print(minha_fila.dequeue())
print(minha_fila)

print(minha_fila.peek())
print(minha_fila.is_empty())

minha_fila.dequeue()
minha_fila.dequeue()
print(minha_fila.is_empty())
print(minha_fila.dequeue())