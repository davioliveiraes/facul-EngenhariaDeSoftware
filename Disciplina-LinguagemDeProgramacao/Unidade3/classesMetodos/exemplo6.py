class ContaCorrente():
   def __init__(self):
      self._saldo = 0.0
   
   def depositar(self, valor):
      if valor > 0:
         self._saldo += valor
      else:
         print("O valor do depósito deve ser positivo.")
   
   def consultar_saldo(self):
      return self._saldo

conta = ContaCorrente()
conta.depositar(200.0)
print(f"Saldo atual: R${conta.consultar_saldo():,.2f}")

conta.depositar(50.0)
print(f"Saldo atual: R${conta.consultar_saldo():,.2f}")
