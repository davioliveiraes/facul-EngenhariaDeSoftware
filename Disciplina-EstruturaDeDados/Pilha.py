class Pilha:
   def __init__(self):
      self.items = []
   
   def push(self, item):
      self.items.append(item)
   
   def pop(self):
      if not self.is_empty():
         return self.items.pop()
      else:
         return "A pilha está vazia."

   def peek(self):
      if not self.is_empty():
         return self.items[-1]
      else:
         return "A pilha está vazia."
   
   def is_empty(self):
      return len(self.items) == 0
   
   def size(self):
      return len(self.items)
   
   def __str__(self):
      return str(self.items)

minha_pilha = Pilha()
print(minha_pilha)

minha_pilha.push(1)
minha_pilha.push(2)
minha_pilha.push(3)
print(minha_pilha)

print(minha_pilha.pop())
print(minha_pilha)

print(minha_pilha.peek())
print(minha_pilha.is_empty())

minha_pilha.pop()
minha_pilha.pop()
print(minha_pilha.is_empty())
print(minha_pilha.pop())
