class Pessoa(object):
   def __init__(self, nome, numeroid):
      self.nome = nome
      self.numeroid = numeroid
   def display(self):
      print(self.nome)
      print(self.numeroid)
   
class Funcionario(Pessoa):
   def __init__(self, nome, numeroid, salario, cargo):
      self.salario = salario
      self.cargo = cargo

      Pessoa.__init__(self, nome, numeroid)
   
func = Funcionario("Aluno Davi", 30111999, 2000, "Engenheiro de Software")
func.display()

