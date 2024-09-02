class ItemLista:
   def __init__(self, data=0, nextItem=None):
      self.data = data
      self.next = nextItem
   
   def __repr__(self):
      return '%s => %s' % (self.data, self.next)

class ListaEncadeada:
   def __init__(self):
      self.head = None
   
   def __repr__(self):
      return "%s" % (self.head)
   
   def insere(lista, data):
      # Armazenando um objeto para adicionar um novo item na lista
      item = ItemLista(data)
      # o head é apontado como próximo item
      item.next = lista.head
      # o item atual se torna o head
      lista.head = item
   
   def remove(lista, valor):
      # Verificar se o item a ser removido é o head
      if lista.head and lista.head.data == valor:
         lista.head == lista.head.next
      else:
         # Detectar a posição do elemento
         before = None
         navegar = lista.head
         # Navegar na lista para encontrar o elemento
         while navegar and navegar.data != valor:
            before = navegar
            navegar = navegar.next
         
         # print(navegar.data)
         # Remove o item se ele for encontrado

   def buscar(lista, valor):
      navegar = lista.head
      while navegar and navegar.data != valor:
         navegar = navegar.next
      return navegar

lista = ListaEncadeada()
lista.insere(1)
lista.insere(2)
lista.insere(3)

print(f"Lista após inserções: {lista}")

lista.remove(2)
print(f"Lista após remover o valor 2: {lista}")

item_encontrado = lista.buscar(3)
if item_encontrado:
   print(f"Item encontrado: {item_encontrado}")
else:
   print("Item não encontrado")

