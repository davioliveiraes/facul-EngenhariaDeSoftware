livros = {
   'ID1': {'titulo': 'Código Limpo', 'autor': 'Robert C. Martin', 'ano': 2009},
   'ID2': {'titulo': 'Diário Estoico', 'autor': 'Ryan Holiday', 'ano': 2016},
   'ID3': {'titulo': 'Entendendo Algoritmos', 'autor': 'Aditya Y. Bhargava', 'ano': '2015'}
}

class Emprestimo:
   def __init__(self, livro, data_emprestimo, data_devolucao):
      self.livro = livro
      self.data_emprestimo = data_emprestimo
      self.data_devolucao = data_devolucao
   
   def __str__(self):
      return f"Empréstimo: {self.livro} - data do emprestimo: {self.data_emprestimo} - data de devolução: {self.data_devolucao}"
   def __repr__(self):
      return f"Empréstimo: {self.livro},{self.data_emprestimo}, {self.data_devolucao}"

emprestimo_1 = Emprestimo(livros['ID2'], '2024-08-20', '2024-09-05')
emprestimo_2 = Emprestimo(livros['ID3'], '2024-08-19', '2024-09-18')
print(emprestimo_1)
print()
print(emprestimo_2)