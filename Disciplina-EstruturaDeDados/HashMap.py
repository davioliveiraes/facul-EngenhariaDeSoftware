class No:
   def __init__(self, chave, valor):
      self.chave = chave
      self.valor = valor
      self.proximo = None
   
class HashMap:
   def __init__(self, tamanho=10):
      self.tamanho = tamanho
      self.tabela = [None] * tamanho
   
   def _hash(self, chave):
      # função de hash simples
      return hash(chave) % self.tamanho
   
   def inserir(self, chave, valor):
      indice = self._hash(chave)
      if self.tabela[indice] is None:
         self.tabela[indice] = No(chave, valor)
      else:
         atual = self.tabela[indice]
         while True:
            if atual.chave == chave:
               atual.valor = valor
               return
            if atual.proximo is None:
               break
            atual = atual.proximo
         atual.proximo = No(chave, valor)
   
   def obter(self, chave):
      indice = self._hash(chave)
      atual = self.tabela[indice]
      while atual:
         if atual.chave == chave:
            return atual.valor
         atual = atual.proximo
      return None
   
   def remover(self, chave):
      indice = self._hash(chave)
      atual = self.tabela[indice]
      anterior = None
      while atual:
         if atual.chave == chave:
            if anterior:
               anterior.proximo = atual.proximo
            else:
               self.tabela[indice] = atual.proximo
            return True
         anterior = atual
         atual = atual.proximo
      return False
   
   def exibir(self):
      for i, no in enumerate(self.tabela):
         print(f"Índice {i}: ", end=" ")
         atual = no
         while atual:
            print(f"({atual.chave}: {atual.valor})", end=" ")
            atual = atual.proximo
         print("None")
   
hashmap = HashMap()

hashmap.inserir("chave1", "valor1")
hashmap.inserir("chave2", "valor2")
hashmap.inserir("chave3", "valor3")
hashmap.inserir("chave4", "valor4")

hashmap.exibir()

print(f"Valor da chave1: {hashmap.obter("chave1")}")
print(f"Valor da chave3: {hashmap.obter("chave3")}")

hashmap.remover("chave2")
hashmap.exibir()

print(f"Valor da chave2: {hashmap.obter("chave2")}")