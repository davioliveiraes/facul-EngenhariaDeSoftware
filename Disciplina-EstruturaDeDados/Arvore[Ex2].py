class Vertice:
   """
      Classe que representa um vértice de uma Árvore Binária
   """

   def __init__(self, dado=None):
      self.dado = dado
      self.esquerda = None
      self.direita = None
   
   def __str__(self):
      return str(self.dado)
   
   def representacao_com_parenteses(self):
      """
         Retorna a representação da árvore com aninhamento com por parênteses
      """
      esque = self.esquerda.representacao_com_parenteses() if self.esquerda else ''
      dire = self.direita.representacao_com_parenteses() if self.direita else ''
      return f'({self.dado} {esque} {dire})'.strip()

   def representacao_com_recuo(self, numero_de_espacos=0):
      """
         Retorna a representação da árvore com recuo
         :return: (str)
      """
      espacos = ' ' * numero_de_espacos
      esque = self.esquerda.representacao_com_recuo(numero_de_espacos + 4) if self.esquerda else ''
      dire = self.direita.representacao_com_recuo(numero_de_espacos + 4) if self.direita else ''
      return f'{espacos}{self}\n{esque}{dire}'
   
   def imprimir_percurso_em_ordem(self):
      """
         Percorre a árvore em ordem simétrica (esquerda, vértice, direita) e imprime o dado do vértice
      """
      if self.esquerda:
         self.esquerda.imprimir_percurso_em_ordem()
      print(self)
      if self.direita:
         self.direita.imprimir_percurso_em_ordem()

   def imprimir_percurso_pre_ordem(self):
      """
         Percorre a árvore em pré-ordem(vértice, esquerda, direita) e imprime o dado do vértice
      """
      print(self)
      if self.esquerda:
         self.esquerda.imprimir_percurso_pre_ordem()
      if self.direita:
         self.direita.imprimir_percurso_pre_ordem()

   def imprimir_percurso_pos_ordem(self):
      """
         Percorre a árvore em pós-ordem (esquerda, direita, vértice)
         e imprime o dado do vértice.
      """
      if self.esquerda:
         self.esquerda.imprimir_percurso_pos_ordem()
      if self.direita:
         self.direita.imprimir_percurso_pos_ordem()
      print(self)

# Criando os vértices da árvore (com dados vazios)
passeio = Vertice('Passeio')

diurno = Vertice('Diurno')
frio = Vertice('Frio')
planetario = Vertice('Planetário')
museu = Vertice('Museu')
calor = Vertice('Calor')
parque = Vertice('Parque')
praia = Vertice('Praia')

noturno = Vertice('Noturno')
restaurante = Vertice('Restaurante')
cinema_noturno = Vertice('Cinema Noturno')

# Vinculando os filhos de 'Passeio'
passeio.esquerda = diurno
passeio.direita = noturno

# Vinculando os filhos de 'Diurno'
diurno.esquerda = frio
diurno.direita = calor

# Vinculando os filhos de 'Frio'
frio.esquerda = planetario
frio.direita = museu

# Vinculando os filhos de 'Calor'
calor.esquerda = parque
calor.direita = praia

# Vinculando os filhos de 'Noturno'abs
noturno.esquerda = restaurante
noturno.direita = cinema_noturno

# Imprime a representação da árvore com parênteses
print("\nRepresentação com parênteses: ")
print(passeio.representacao_com_parenteses())

# Imprime a representação da árvore com recuo
print("\nRepresentação com recuo: ")
print(passeio.representacao_com_recuo())

# Imprime os dados dos vértices em diferentes percursos
print("\nPercurso em ordem: ")
passeio.imprimir_percurso_em_ordem()

print("\nPercurso em pré-ordem: ")
passeio.imprimir_percurso_pre_ordem()

print("\nPercurso em pós-ordem: ")
passeio.imprimir_percurso_pos_ordem()

   