class TabelaHashEstudantes:
   def __init__(self, tamanho=10):
      self.tamanho = tamanho
      self.tabela =[[] for _ in range(tamanho)]
   
   def _hash_func(self, nome):
      return sum(ord(char) for char in nome) % self.tamanho
   
   def inserir(self, nome, rota):
      indice = self._hash_func(nome)
      for entrada in self.tabela[indice]:
         if entrada[0] == nome:
            entrada[1] = rota
            return
      self.tabela[indice].append([nome, rota])
   
   def buscar(self, nome):
      indice = self._hash_func(nome)
      for entrada in self.tabela[indice]:
         if entrada[0] == nome:
            return entrada[1]
      return "Estudante não encontrado."

   def remover(self, nome):
      indice = self._hash_func(nome)
      for i, entrada in enumerate(self.tabela[indice]):
         if entrada[0] == nome:
            del self.tabela[indice][i]
            return f"{nome} removido"
      return "Estudante não encontrado."
   
   def exibir_todas_rotas(self):
      for i, lista in enumerate(self.tabela):
         if lista:
            print(f"Índice {i}: {lista}")

rotas_estudantes = TabelaHashEstudantes(tamanho=10)

rotas_estudantes.inserir("Alice", "Rota 1")
rotas_estudantes.inserir("Bob", "Rota 2")
rotas_estudantes.inserir("Carlos", "Rota 3")
rotas_estudantes.inserir("Diana", "Rota 4")

rotas_estudantes.exibir_todas_rotas()

print(f"\nBusca: {rotas_estudantes.buscar("Alice")}")

rotas_estudantes.inserir("Alice", "Rota 5")
print("\nApós atualização da rota de Alice: ")
rotas_estudantes.exibir_todas_rotas()

print(f"\nRemovendo Bob: {rotas_estudantes.remover("Bob")}")
print(f"\nApós remoção de Bob: ")
rotas_estudantes.exibir_todas_rotas()
