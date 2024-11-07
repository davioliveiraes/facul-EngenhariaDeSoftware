class Produto:
   def __init__(self, id, nome, descricao, preco):
      self.id = id
      self.nome = nome
      self.descricao = descricao
      self.preco = preco
   
   def __str__(self):
      return f"ID: {self.id}, Nome: {self.nome}, Descrição: {self.descricao}, Preço: {self.preco}"

cache = {}

def adicionar_produto_ao_cache(produto):
   """
      Adiciona um produto ao cache.
   """
   cache[produto.id] = produto
   print(f"Produto '{produto.nome}' adicionado ao cache.")

def consultar_produto(id):
   """
      Consulta um produto no cache pelo ID. Se não estiver no cache, simula a busca no banco de dados.
   """
   if id in cache:
      print("Produto encontrado no cache.")
      return cache[id]
   else:
      print("Produto não encontrado no cache. Buscando no banco de dados...")
   
      produto = Produto(id, f"Produto_{id}", "Descrição fictícia", 100.00)
      adicionar_produto_ao_cache(produto)
      return produto
   
def remover_produto_do_cache(id):
   """
      Remove um produto do cache pelo ID, se ele estiver presente.
   """
   if id in cache:
      produto = cache.pop(id)
      print(f"Produto '{produto.nome}' removido do cache.")
   else:
      print(f"Produto com ID {id} não está no cache.")

produto1 = Produto(1, "Camiseta", "Camiseta de algodão", 29.99)
produto2 = Produto(2, "Calça", "Calça jeans", 59.99)

adicionar_produto_ao_cache(produto1)
adicionar_produto_ao_cache(produto2)

print("\nConsultando o produto com ID 1: ")
print(consultar_produto(1))

print("\nConsultando o produto com ID 3: ")
print(consultar_produto(3))

print("\n Removendo o produto com ID 1: ")
remover_produto_do_cache(1)

print("\nConsultando o produto com ID 1 após remoção: ")
print(consultar_produto(1))
