class VerticeAVL:

   # Contrutor: inicializa um vértice com uma chave pai, e subárvores esquerda e direta vazias
   def __init__(self, chave, pai=None):
      self.chave = chave # Valor do nó
      self.pai = pai # Referência ao pai
      self.esquerdo = None # Suárvore esquerda
      self.direito = None # Suárvore direita
      self._altura = 0 # Altura do nó, inicialmente 0

   @property
   def altura(self):
      return self.altura
   
   @altura.setter
   def altura(self, valor):
      self._altura = valor
   
   @property
   def altura(self, valor):
      self._altura = valor
   
   @property
   def fator_de_balanceamento(self):
      altura_esquerda = self.esquerdo.altura if self.esquerdo else - 1
      altura_direita = self.direito.altura if self.direita else - 1
      return altura_direita - direita_esquerda
   
   def __str__(self):
      return str(self.chave)
   
   def __repr__(self):
      return str(self.chave)
   
   # Método para imprimir a subárvore a partir deste vértice, com recuo visual para indicar a hierarquia
   def imprimir_subarvore(self, recuo=0, sentido=""):
      if self.direito:
         self.direito.imprimir_subarvore(recuo + 10, "/")
      print("{}{}-----> [{}] (h={}, fb={})".format(" " * recuo, sentido, self.chave, self.altura, self.fator_de_balanceamento))
      if self.esquerdo:
         self.esquerdo.imprimir_subarvore(recuo + 10, "\\")
   
   # Método para inserir uma nova chave na árvore, respeitando as propriedades de árvore AVL.
   def inserir(self, chave_nova):
      print("{} (atual={})".format(chave_nova, self.chave))
      if chave_nova == self.chave:
         return self # Se a chave já existe, não faz nada.
      
      raiz_da_subarvore = self

      # Insere na subárvore esquerda ou direita, conforme a comparação das chaves.
      if chave_nova < self.chave:
         if self.esquerdo:
            raiz_da_subarvore = self.esquerdo.inserir(chave_nova)
         else:
            self.esquerdo = VerticeAVL(chave_nova, self)
      elif chave_nova > self.chave:
         if self.direito:
            raiz_da_subarvore = self.direito.inserir(chave_nova)
         else:
            self.direito = VerticeAVL(chave_nova, self)
      
      # Atualiza a altura e balencia a árvore após a inserção
      raiz_da_subarvore.atualizar_altura()
      raiz_da_subarvore = raiz_da_subarvore.balancear()

      return raiz_da_subarvore.pai or raiz_da_subarvore # Retorna a nova raiz da subárvore.and

   # Método para atualizar a altura do vértice
   def atualizar_altura(self):
      altura_esquerda = self.esquerdo.altura if self.esquerdo else -1
      altura_direita = self.direito.altura if self.direito else -1
      self.altura = max(altura_esquerda, altura_direita) + 1

   # Método para balancear a árvore AVL
   def balancear(self):
      fb = self.fator_de_balanceamento
      # Se o fator de balanceamento for maior que 1, há desbalanceamento para esquerda
      if fb < -1:
         if self.direito.fator_de_balanceamento < 0:
            # Rotação esquerda-direita
            self.direito = self.direito.rotacao_direito()
         return self.rotacao_esquerda()
      # Se o fator de balanceamento for menor que -1, há desbalanceamento para a esquerda
      if fb < -1:
         if self.esquerdo.fator_de_balanceamento > 0:
            # Rotação esquerda-direita
            self.esquerdo = self.esquerdo.rotacao_esquerda()
         return self.rotacao_direita()
      return self # Já está balanceado

   # Rotação à esquerda em torno deste vértice
   def rotacao_esquerda(self):
      nova_raiz = self.direito
      self.direito = nova_raiz.esquerdo
      if nova_raiz.esquerdo:
         nova_raiz.esquerdo.pai = self
      nova_raiz.esquerdo = self

      nova_raiz.pai = self.pai
      self.pai = nova_raiz

      self.atualizar_altura()
      nova_raiz.atualizar_altura()
      return nova_raiz
   
   # Rotação à direita em torno deste vértice
   def rotacao_direita(self):
      nova_raiz = self.esquerdo
      self.esquerdo = nova_raiz.direito
      if nova_raiz.direito:
         nova_raiz.direito.pai = self
      nova_raiz.direito = self

      nova_raiz.pai = self.pai
      self.pai = nova_raiz

      self.atualizar_altura()
      nova_raiz.atualizar_altura()
      return nova_raiz
      