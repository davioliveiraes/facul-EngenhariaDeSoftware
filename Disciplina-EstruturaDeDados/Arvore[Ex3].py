class Filhos:
   """
      Classe que gerencia os filhos de um vértice em uma árvore N-ária.
   """

   def __init__(self):
      # Cria uma lista Python vazia para armazenar os filhos
      self._vertices = list()
   
   def representacao_com_parenteses(self):
      """
         Retorna a representação da árvore com aninhamento por parênteses.
         :return: str
      """
      representacoes = []
      for vertice in self._vertices:
         representacoes.append(vertice.representacao_com_parenteses())
      return ''.join(representacoes)

   def representacao_com_recuo(self, numero_de_espacos=0):
      """
         Retorna a representação da árvore com recuo.
         :param numero_de_espacos: (int) Números de espaços para indentação
         :return: str
      """
      representacoes = []
      for vertices in self._vertices:
         representacoes.append(vertices.representacao_com_recuo(numero_de_espacos + 2))
      return ''.join(representacoes)

   def inserir(self, dado):
      """
         Insere um novo vértice com dado fornecido na lista de filhos.
         :param dado: dado do vértice
         :return: o vértice inserido
      """
      vertice_novo = Vertice(dado)
      self._vertices.append(vertice_novo)
      return vertice_novo

   def imprimir_percurso_pre_ordem(self):
      """
         Percorre os filhos da árvore em pré-ordem (vértice, filhos).
         :return: None
      """
      for vertice in self._vertices:
         vertice.imprimir_percurso_pre_ordem()
      
   def imprimir_percurso_pos_ordem(self):
      """
         Percorre os filhos da árvore em pós-ordem (filhos, vértice).
         :return: None
      """
      for vertice in self._vertices:
         vertice.imprimir_percurso_pos_ordem()
      
class Vertice:
   """
      Classe que representa um vértice em um árvore N-ária.
   """

   def __init__(self, dado):
      # Dado propriamento dito, conteúdo do vértice
      self.dado = dado
      # Classe que gerencia os filhos deste vértice
      self.filhos = None
   
   def __str__(self):
      return str(self.dado)

   def representacao_com_parenteses(self):
      """
         Retorna a representação da árvore com aninhamento por parênteses.
         :return: str
      """
      filhos = ''
      if self.filhos:
         filhos = self.filhos.representacao_com_parenteses()
      return f'({self.dado}{filhos})'.strip()
   
   def representacao_com_recuo(self, numero_de_espacos=0):
      """
         Retorna a representação da árvore com recuo.
         :param numero_de_espacos: (int) Número de espaços para indentação
      """
      filhos = ''
      if self.filhos:
         filhos = self.filhos.representacao_com_recuo(numero_de_espacos + 2)
      espacos = ' ' * numero_de_espacos
      return f'{espacos}{self.dado}\n{filhos}'
      
   def inserir_filho(self, dado):
      """
         Insere um novo filho ao vértice atual.
         :param dado: dado de novo filho
         :return: o vértice filho inserido
      """
      if self.filhos is None:
         self.filhos = Filhos()
      return self.filhos.inserir(dado)
      
   def imprimir_percurso_pre_ordem(self):
      """
         Percorre a árvore em pré-ordem (vertice, filhos) e imprimie o dado do vértice.
         :return: None
      """
      print(self)
      if self.filhos:
         self.filhos.imprimir_percurso_pre_ordem()
      
   def imprimir_percurso_pos_ordem(self):
      """
         Percorre a árvore em pós-ordem (filhos, vértice) e imprime o dado do vértice.
         :return: none
      """
      if self.filhos:
         self.filhos.imprimir_percurso_pos_ordem()
      print(self)

# Criando a estrutura da árvore com pacotes turísticos
raiz = Vertice("Pacotes Turísticos")

# Criando os filhos de 'Pacotes Turísticos'
tranquilidade = raiz.inserir_filho("Tranquilidade")
aventura = raiz.inserir_filho("Aventura")
luxo = raiz.inserir_filho("Luxo")

# Criando os filhos de 'Aventura'
rafting = aventura.inserir_filho("Rafting")
escalada = aventura.inserir_filho("Escalada")
tirolesa = aventura.inserir_filho("Tirolesa")

# Exibir a árvore de diferentes formas
print("\n Representação com recuo: ")
print(raiz.representacao_com_recuo())

print("\n Representação com parênteses: ")
print(raiz.representacao_com_parenteses())

# Imprimir percursos em diferentes ordens
print("\n Percurso em pré-ordem: ")
raiz.imprimir_percurso_pre_ordem()

print("\n Percurso em pós-ordem: ")
raiz.imprimir_percurso_pos_ordem()

print("\n Percurso em pré-ordem a partir de 'Aventura': ")
aventura.imprimir_percurso_pre_ordem()

print("\n Percurso em pós-ordem a partir de 'Aventura': ")
aventura.imprimir_percurso_pos_ordem()