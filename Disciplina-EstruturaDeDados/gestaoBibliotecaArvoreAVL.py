class NoAVL:
   def __init__(self, id_livro, titulo):
      self.id_livro = id_livro
      self.titulo = titulo
      self.altura = 1
      self.esquerda = None
      self.direita = None

class AVLTree:
   def altura(self, no):
      if not no:
         return 0
      return no.altura
   
   def fator_balanceamento(self, no):
      if not no:
         return 0
      return self.altura(no.esquerda) - self.altura(no.direita)
   
   def rotacao_direita(self,  y):
      x = y.esquerda
      T2 = x.direita

      # Realiza a rotação
      x.direita = y
      y.esquerda = T2

      # Atualiza as alturas
      y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))
      x.altura = 1 + max(self.altura(x.esquerda), self.altura(x.direita))

      # Retorna o novo nó raiz
      return x
   
   def rotacao_esquerda(self, x):
      y = x.direita
      T2 = y.esquerda

      # Realiza a rotação
      y.esquerda = x
      x.direita = T2

      # Atualiza as alturas
      x.altura = 1 + max(self.altura(x.esquerda), self.altura(x.direita))
      y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))

      return y
   
   def inserir(self, raiz, id_livro, titulo):
      # 1. Realiza a inserção normal em árvore binária de busca
      if not raiz:
         return NoAVL(id_livro, titulo)
      elif id_livro < raiz.id_livro:
         raiz.esquerda = self.inserir(raiz.esquerda, id_livro, titulo)
      else:
         raiz.direita = self.inserir(raiz.direita, id_livro, titulo)
      
      # 2. Atualiza a altura do nó atual
      raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))

      # 3. Calcula o fator de balenceamento para verificar a necessidade de balancear
      balanco = self.fator_balanceamento(raiz)

      # 4. Rotações para balancear a árvore
      # Caso Esquerda-Esquerda
      if balanco > 1 and id_livro < raiz.esquerda.id_livro:
         return self.rotacao_direita(raiz)
      
      # Caso Direita-Direita
      if balanco < -1 and id_livro > raiz.direita.id_livro:
         return self.rotacao_esquerda(raiz)
      
      # Caso Esquerda-Direita
      if balanco > 1 and id_livro > raiz.esquerda.id_livro:
         raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
         return self.rotacao_direita(raiz)
      
      # Caso Direita-Esquerda
      if balanco < -1 and id_livro < raiz.direita.id_livro:
         raiz.direita = self.rotacao_direita(raiz.direita)
         return self.rotacao_esquerda(raiz)
      
      return raiz
   
   def remover(self, raiz, id_livro):
      # 1. Realiza a remoção normal da árvore binária de busca
      if not raiz:
         return raiz
      elif id_livro < raiz.id_livro:
         raiz.esquerda = self.remover(raiz.esquerda, id_livro)
      elif id_livro > raiz.id_livro:
         raiz.direita = self.remover(raiz.direita, id_livro)
      else:
         # Nó com apenas um filho ou nenhum
         if raiz.esquerda is None:
            return raiz.direita
         elif raiz.direita is None:
            return raiz.esquerda
         
         # Nó com dois filhos: substitui pelo emnor valor na subárvore direita
         temp = self.get_no_com_menor_valor(raiz.direita)
         raiz.id_livro = temp.id_livro
         raiz.titulo = temp.titulo
         raiz.direita = self.remover(raiz.direita, temp.id_livro)
      
      # 2. Atualiza a altura do nó atual
      if raiz is None:
         return raiz
      raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))

      # 3. Calcula o fator de balanceamento
      balanco = self.fator_balanceamento(raiz)

      # 4. Rotações para balancear a árvore
      # Caso Esquerda-Esquerda
      if balanco > 1 and self.fator_balanceamento(raiz.esquerdo) >= 0:
         return self.rotacao_direita(raiz)
      
      # Caso Esquerda-Direita
      if balanco > 1 and self.fator_balanceamento(raiz.esquerda) < 0:
         raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
         return self.rotacao_direita(raiz)
      
      # Caso Direita-Direita
      if balanco < -1 and self.fator_balanceamento(raiz.direita) <= 0:
         return self.rotacao_esquerda(raiz)
      
      # Caso Direita-Esquerda
      if balanco < -1 and self.fator_balanceamento(raiz.direita) > 0:
         raiz.direita = self.rotacao_direita(raiz.direita)
         return self.rotacao_esquerda(raiz)

      return raiz
   
   def get_no_com_menor_valor(self, no):
      atual = no
      while atual.esquerda is not None:
         atual = atual.esquerda
      return atual
   
   def buscar(self, raiz, id_livro):
      if raiz is None or raiz.id_livro == id_livro:
         return raiz
      if id_livro < raiz.id_livro:
         return self.buscar(raiz.esquerda, id_livro)
      return self.buscar(raiz.direita, id_livro)
   
   def exibir_in_ordem(self, raiz):
      if raiz:
         self.exibir_in_ordem(raiz.esquerda)
         print(f"ID: {raiz.id_livro}, Título: {raiz.titulo}")
         self.exibir_in_ordem(raiz.direita)

avl = AVLTree()
raiz = None

# Inserindo livros
raiz = avl.inserir(raiz, 10, "Ultra Aprendizado")
raiz = avl.inserir(raiz, 20, "Sem Esforço")
raiz = avl.inserir(raiz, 30, "O Milagra do Amanhã")
raiz = avl.inserir(raiz, 40, "O homem mais rico da babilônia")
raiz = avl.inserir(raiz, 50, "Entendento Algoritmos")

# Exibindo a árvore em ordem
print("Livros na biblioteca: ")
avl.exibir_in_ordem(raiz)

# Buscando um livro
id_livro_busca = int(input("Digite o identificador do livro: "))
livro = avl.buscar(raiz, id_livro_busca)
if livro:
   print(f"\nLivro encontrado - ID: {livro.id_livro} Título: {livro.titulo}")
else:
   print(f"\nLivro com ID {id_livro_busca} não encontrado.")

# Removendo um livro
raiz = avl.remover(raiz, id_livro_busca)
print(f"\nApós a remoção do livro com {id_livro_busca}")
avl.exibir_in_ordem(raiz)
   