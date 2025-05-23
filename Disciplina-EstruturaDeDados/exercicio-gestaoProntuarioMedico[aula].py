class Prontuario:
   def __init__(self, paciente, diagnostico, tratamento, proximo=None):
      self.paciente = paciente
      self.diagnostico = diagnostico
      self.tratamento = tratamento
      self.proximo = proximo

class ListaEncadeadaProntuarios:
   def __init__(self):
      self.head = None
   
   def adicionar_prontuario(self, paciente, diagnostico, tratamento):
      novo_prontuario = Prontuario(paciente, diagnostico, tratamento, self.head)

      self.head = novo_prontuario

   def busca_prontuario(self, nome_paciente):
      atual = self.head
      while atual:
         if atual.paciente == nome_paciente:
            return atual
         atual = atual.proximo
      return None
   
   def listagem(self):
      lista = []
      atual = self.head
      while atual:
         lista.append({
            "paciente": atual.paciente,
            "diagnostico": atual.diagnostico,
            "tratamento": atual.tratamento
         })
         atual = atual.proximo
      return lista

   # Uso da lista encadeada para gerenciar prontuários
sistema_prontuarios = ListaEncadeadaProntuarios()
   
sistema_prontuarios.adicionar_prontuario("Harvey Specter", "Diabetes Tipo 2", "Metformina")

sistema_prontuarios.adicionar_prontuario("Luis Litt", "Hipertensão", "Losartana")

listagem_prontuarios = sistema_prontuarios.listagem()
print(listagem_prontuarios)

paciente_buscado = "Harvey Specter"
prontuario = sistema_prontuarios.busca_prontuario(paciente_buscado)
if prontuario:
   print(f"\nProntuário encontrado para {paciente_buscado}.")
else:
   print(f"\nProntuário {paciente_buscado} não encontrado.")


