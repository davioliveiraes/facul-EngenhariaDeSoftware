class Anotacoes:
   def __init__(self, pagina, paragrafo, texto):
      self.pagina = pagina
      self.paragrafo = paragrafo
      self.texto = texto
      self.chave = (pagina, paragrafo) # a chave é uma tupla (página, parágrafo) para ordenação

   def __repr_(self):
      return f'Anotações (Página: {self.pagina}, Parágrafo: {self.paragrafo}, Texto: "{self.texto}")'
   
class NodoB:
   def __init__(self, t):
      self.chaves = [] # Lista de anotações (ordenada por chave)
      self.filhos = [] # Lista de nodos filhos
      self.t = t # Grau mínimo da árvore B
      self.folha = True # Verdadeiro se for uma folha
   
   def __repr__(self):
      return f'NodoB(chaves: {self.chaves}, folha: {self.folha})'
   
   def dividir(self, pai, filho):
      """
         Divide o nodo atual e ajusta a árvore
      """
      novo_nodo = NodoB(self.t)
      novo_nodo.folho = self.folha

      # Movemos metade das chaves para o novo nodo
      meio = self.t - 1
      pai.chaves.insert(indice, self.chaves[meio])
      novo_nodo.chaves = self.chaves[meio + 1]
      self.chaves = self.chaves[:meio]

      # Se não for folha, também dividimos os filhos
      if not self.folha:
         novo_nodo.filhos = self.filhos[meio + 1:]
         self.filhos = self.filhos[:meio + 1]
      pai.filhos.insert(indice + 1, novo_nodo)
   
   def inserir_nao_cheio(self, anotacao):
      """
         Insere uma anotação em um nodo que não está cheio
      """
      if self.folha:
         # Inserir a anotação na posição correta
         self.chaves.append(anotacao)
         self.chaves.sort(key=lambda x: x.chave)
      else:
         # Encontrar o filho apropriado para inserir a anotação
         i = len(self.chaves) - 1
         while i >= 0 and anotacao.chave < self.chaves[i].chave:
            i -= 1
         i += 1
      
      # Se o filho está cheio, precisamos dividi-lo
      if len(self.filho[i].chaves) == 2 * self.t - 1:
         self.filhos[i].dividir(self, i)

         if anotacao.chave > self.chaves[i].chave:
            i += 1
      
      # Inserir no filho adequado
      self.filhos[i].inserir_nao_cheio(anotacao)

class ArvoreB:
   def __init__(self, t):
      self.raiz = NodoB(t)
      self.t = t

   def inserir(self, anotacao):
      """
         Insere uma nota anotação na árvore B
      """
      raiz = self.raiz
      if len(raiz.chaves) == 2 * self.t - 1:
         # A raiz está cheio, precisamos dividi-la
         novo_raiz = NodoB(self.t)
         novo_raiz.folha = False
         novo_raiz.filhos.append(self.raiz)
         novo_raiz.dividir(self.raiz, 0)

         # Agora temos uma nova raiz, com dois filhos, reinserir
         self.raiz = novo_raiz
      
      self.raiz.inserir_nao_cheio(anotacao)

   def consultar(self, pagina, paragrafo):
      """
         Busca uma anotação pela página e parágrafo
      """
      return self._buscar(self.raiz, (pagina, paragrafo))

   def _buscar(self, nodo, chave):
      """
         Função recursiva para buscar uma chave em um nodo
      """
      i = 0
      while i < len(nodo.chaves) and chave > nodo.chaves[i].chave:
         i += 1
         
      if i < len(nodo.chaves) and chave == nodo.chaves[i].chave:
         return nodo.chaves[i]
         
      if nodo.folha:
         return None # Se for folha e não encontramos, a anotação não existe
         
      return self._buscar(nodo.filho[i], chave)
   
   def remover(self, pagina, paragrafo):
      """
         Remove uma anotação pela página e parágrafo
      """
      # A implementação completa da remoção em árvores B é complexa e envolve vários caso,
      #  Como fusão de nodo e redistribuição de chaves, o que requer uma implementação mais detalhada.
      pass # ToDo
   
   def listar_anotacoes(self):
      """
         Lista todas as anotações em ordem crescente de chaves
      """
      anotacoes = []
      self._listar(self.raiz, anotacoes)
      return anotacoes
   
   def _listar(self, nodo, anotacoes):
      """
         Função recursiva para listar as anotações em ordem
      """
      i = 0
      while i < len(nodo.chaves):
         if not nodo.folhas:
            self._listar(nodo.filhos[i], anotacoes)
         anotacoes.append(nodo.chaves[i])
         i += 1

      if not nodo.folha:
         self._listar(nodo.filhos[i], anotacoes)
         