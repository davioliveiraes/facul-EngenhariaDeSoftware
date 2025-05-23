class GrafoLabirinto:
   def __init__(self):
      self.salas = {}
   
   def adicionar_sala(self, sala):
      # Verifica se a sala está no grafo, se não, adiciona
      if sala not in self.salas:
         self.salas[sala] = []
      
   def adicionar_passagem(self, sala1, sala2):
      if sala1 in self.salas and sala2 in self.salas:
         self.salas[sala1].append(sala2)
         self.salas[sala2].append(sala1)
   
   def exibir_salas_adjacentes(self, sala_atual):
      if sala_atual in self.salas:
         adjacentes = self.salas[sala_atual]
         print(f"Salas adjacentes à {sala_atual}: {', '.join(adjacentes)}")
         return adjacentes
      else:
         print(f"Sala {sala_atual} não encontrada.")
      return []
   
labirinto = GrafoLabirinto()
salas = ['v1', 'v2', 'v3', 'v4', 'v4', 'v5', 'v1A', 'v1E', 'v2A']
for sala in salas:
   labirinto.adicionar_sala(sala)

labirinto.adicionar_passagem('v1', 'v2')
labirinto.adicionar_passagem('v2', 'v3')
labirinto.adicionar_passagem('v3', 'v4')
labirinto.adicionar_passagem('v4', 'v5')
labirinto.adicionar_passagem('v5', 'v1')
labirinto.adicionar_passagem('v4', 'v1A')
labirinto.adicionar_passagem('v2A', 'v1E')

posicao_jogador = 'v1'
while True:
   adjacentes = labirinto.exibir_salas_adjacentes(posicao_jogador)

   escolha = input(f"Escolha uma sala para onde se mover (atual: {posicao_jogador}) ou 'sair' para encerrar: ").strip()

   if escolha == 'sair':
      print("FIM DE JOGO")
      break
   elif escolha in adjacentes:
      posicao_jogador = escolha
   else:
      print("ESCOLHA INVÁLIDA. TENTE NOVAMENTE.")