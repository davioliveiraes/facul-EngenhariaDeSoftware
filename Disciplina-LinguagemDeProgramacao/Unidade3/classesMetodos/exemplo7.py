class Pessoa:
   def __init__(self, nome, idade):
      self.nome = nome
      self.idade = idade
   
   def andar(self):
      print(f"{self.nome} está andando.")
   
   def ligar(self):
      print(f"{self.nome} está em ligação.")
   
class Funcionario(Pessoa):
   def __init__(self, nome, idade, ocupacao, salario):
      super().__init__(nome, idade)
      self.ocupacao = ocupacao
      self.salario = salario
   
   def trabalho(self):
      print(f"{self.nome}, que é {self.ocupacao}, está trabalhando.")
   
   def ligacao(self):
      self.ligar()
      print(f"{self.nome} está em ligação no trabalho.")

# Exemplo de uso
funcionario_1 = Funcionario("Davi", 25, "Engenheiro de Software", 40000)
funcionario_1.trabalho()
funcionario_1.ligacao()