class No:
   def __init__(self, valor=None):
      self.valor = valor
      self.proximo = None
   
class ListaEncadeada:
   def __init__(self):
      self.cabeca = None
   
   def inserir_no_inicio(self, valor):
      novo_no = No(valor)
      novo_no.proximo = self.cabeca
      self.cabeca = novo_no
   
   def inserir_no_fim(self, valor):
      novo_no = No(valor)
      if self.cabeca is None:
         self.cabeca = novo_no
         return
      ultimo = self.cabeca
      while ultimo.proximo:
         ultimo = ultimo.proximo
      ultimo.proximo = novo_no
   
   def remover(self, valor):
      atual = self.cabeca
      anterior = None
      while atual and atual.valor != valor:
         anterior = atual
         atual = atual.proximo
      if atual is None:
         return "Valor não encontrado na lista."
      if anterior is None:
         self.cabeca = atual.proximo
      else:
         anterior.proximo = atual.proximo

   def buscar(self, valor):
      atual = self.cabeca
      while atual and atual.valor != valor:
         atual = atual.proximo
      return atual
   
   def exibir(self):
      elementos = []
      atual = self.cabeca
      while atual:
         elementos.append(atual.valor)
         atual = atual.proximo
      print(" -> ".join(map(str, elementos)))

# Testando a implementação da Lista Encadeada
lista = ListaEncadeada()

# Inserindo no início
lista.inserir_no_inicio(3)
lista.inserir_no_inicio(2)
lista.inserir_no_inicio(1)

# Inserindo no final
lista.inserir_no_fim(4)
lista.inserir_no_fim(5)

# Removendo um valor
lista.remover(3)
lista.exibir()

# Buscando um valor
resultado_busca = lista.buscar(int(input("Digite um valor que deseja buscar: ")))
if resultado_busca:
   print(f"Valor {resultado_busca.valor}, encontrado na lista.")
else:
   print("Valor não encontrado na lista.")

# Testando buscar um valor inexistente
resultado_busca = lista.buscar(int(input("Digite um valor que deseja buscar: ")))
if resultado_busca:
   print(f"Valor: {resultado_busca.valor}, encontrado na lista")
else:
   print("Valor não foi encontrado.")
