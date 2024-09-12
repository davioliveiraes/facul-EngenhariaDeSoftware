import heapq

class Atendimento:
   def __init__(self):
      self.fila_prioridade = []
      self.contador = 0 # para manter a ordem de chegada em casos de mesma prioridade
   
   def adicionar_solicitacao(self, descricao, prioridade):
      # Prioridade menor: Padrão; Prioridade maior: Urgente
      heapq.heappush(self.fila_prioridade, (prioridade, self.contador, descricao))
      self.contador += 1
   
   def atender_solicitacao(self):
      if self.fila_prioridade:
         prioridade, _, descricao = heapq.heappop(self.fila_prioridade)
         print(f"Solicitação de atendimento: {descricao} (Prioridade: {prioridade})")
      else:
         print("Nunhuma solicitação de atendimento.")

# Exemplo de uso
sistema = Atendimento()
sistema.adicionar_solicitacao("Solicitação Padrão: 1", 1) # prioridade padrão
sistema.adicionar_solicitacao("Solicitação Urgente: 1", 0) # prioridade urgente
sistema.adicionar_solicitacao("Solciitação Padrão: 2", 1) # prioridade padrão

sistema.atender_solicitacao() # Atender a Solicitação Urgente 1
sistema.atender_solicitacao() # Atender a Solicitação padrão 1
sistema.atender_solicitacao() # Atender a Solicitação padrão 2
