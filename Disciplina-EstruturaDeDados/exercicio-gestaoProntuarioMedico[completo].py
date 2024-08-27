class Prontuario:
   def __init__(self, paciente, data, detalhes):
      self.paciente = paciente
      self.data = data
      self.detalhes = detalhes
      self.proximo = None

class ListaEncadeada:
   def __init__(self):
      self.head = None
   
   def adicionar_prontuario(self, paciente, data, detalhes):
      novo_pontuario = Prontuario(paciente, data, detalhes)
      if self.head is None:
         self.head = novo_pontuario
      else:
         atual = self.head
         while atual.proximo:
            atual = atual.proximo
         atual.proximo = novo_pontuario
   
   def busca_prontuario(self, paciente):
      atual = self.head
      while atual:
         if atual.paciente == paciente:
            return atual
         atual = atual.proximo
      return None
   
   def remover_prontuario(self, paciente):
      atual = self.head
      anterior = None
      while atual:
         if atual.paciente == paciente:
            if anterior:
               anterior.proximo = atual.proximo
            else:
               self.head = atual.proximo
            return True
         anterior = atual
         atual = atual.proximo
      return False
   
   def listar_prontuarios(self):
      atual = self.head
      while atual:
         print(f"Paciente: {atual.paciente}, Data: {atual.data}, Detalhes: {atual.detalhes}")
         atual = atual.proximo


prontuarios = ListaEncadeada()

prontuarios.adicionar_prontuario("Harvey Specter", "2024-05-22", "Consulta trimestral")
prontuarios.adicionar_prontuario("Mike Ross", "2024-07-25", "Consulta cardiolófica")
prontuarios.adicionar_prontuario("Luis Litt", "2024-08-20", "Exame de sangue")

print("Lista de Prontuários: ")
prontuarios.listar_prontuarios()

paciente_busca = str(input("Digite o paciente que desejar buscar: "))
prontuario_buscado = prontuarios.busca_prontuario(paciente_busca)
if prontuario_buscado:
   print(f"\nProntuário encontrado para {paciente_busca}; Data: {prontuario_buscado.data}; Detalhes: {prontuario_buscado.detalhes}")
else:
   print(f"\nProntuário de {paciente_busca} não encontrado.")

# Removendo um prontuário
paciente_remover = str(input("Digite o paciente que deseja remover: "))
prontuario_removido = prontuarios.remover_prontuario(paciente_remover)
if prontuario_removido:
   print(f"\nProntuário de {paciente_remover} removido com sucesso.")
else:
   print(f"\nProntuário de {paciente_remover} não foi removido com sucesso")

print("\nLista de Prontuarios final: ")
prontuarios.listar_prontuarios()
