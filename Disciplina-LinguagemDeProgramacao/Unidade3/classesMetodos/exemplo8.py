class Pessoa:
   def __init__(self, cpf, nome, endereco):
      self.cpf = cpf
      self.nome = nome
      self.endereco = endereco
   
   def __str__(self):
      return f"Nome: {self.nome}, CPF: {self.cpf}, Endereço: {self.endereco}"
   
class Funcionario(Pessoa):
   def __init__(self, cpf, nome, endereco, matricula, salario):
      super().__init__(cpf, nome, endereco)
      self.matricula = matricula
      self.salario = salario
   
   def bater_ponto(self):
      print(f"{self.nome} bateu o ponto.")
   
   def fazer_login(self):
      print(f"{self.nome} fez login no sistema.")
   
   def __str__(self):
      return f"{super().__str__()}, Matrícula: {self.matricula}, Salário: {self.salario:,.2f}"

class Cliente(Pessoa):
   def __init__(self, cpf, nome, endereco, codigo, data_cadastro):
      super().__init__(cpf, nome, endereco)
      self.codigo = codigo
      self.data_cadastro = data_cadastro
   
   def fazer_compra(self):
      print(f"{self.nome} realizou uma compra.")
   
   def pagar_conta(self):
      print(f"{self.nome} pagou a conta.")
   
   def __str__(self):
      return f"{super().__str__()}, Código: {self.codigo}, Data de Cadastro: {self.data_cadastro}"

# Exemplos de uso
f1 = Funcionario("123.231.212-12", "David", "Rua X, 123", "D001", 4000.00)
print(f1)
f1.bater_ponto()
f1.fazer_login()

c1 = Cliente("982.123.522-12", "Davi", "Rua Y, 321", "002", "2025-01-10")
print(c1)
c1.fazer_compra()
c1.pagar_conta()