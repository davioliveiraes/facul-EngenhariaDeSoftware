from datetime import datetime, timedelta

class Biblioteca:
   def __init__(self):
      self.livros = {}
      self.emprestimos = {}
   
   def adicionar_livro(self, titulo, autor, copias):
      self.livros[titulo] =  {"autor": autor, "copias": copias}
      print(f"Livro: {titulo} adicionando com sucesso.")
   
   def emprestimo_livro(self, usuario, titulo):
      if titulo in self.livros and self.livros[titulo]["copias"] > 0:
         data_emprestimo = datetime.now()
         data_devolucao = data_emprestimo + timedelta(days=15)

         self.emprestimos[usuario] = {
            "titulo": titulo,
            "data_emprestimo": data_emprestimo,
            "data_devolucao": data_devolucao
         }

         self.livros[titulo]["copias"] -= 1
         print(f"Livro: {titulo}; Empréstimo: {usuario}. Deve ser devolvida até {data_devolucao.strftime('%d/%m/%Y')}.")
      else:
         print(f"Livro: {titulo} não disponível para empréstimo.")
   
   def devolver_livro(self, usuario):
      if usuario in self.emprestimos:
         titulo = self.emprestimos[usuario]["titulo"]
         data_devolucao = self.emprestimos[usuario]["data_devolucao"]
         data_hoje = datetime.now()

         if data_hoje > data_devolucao:
            dias_atraso = (data_hoje - data_devolucao).days
            multa = dias_atraso * 2
            print(f"Livro: {titulo} devolvido com {dias_atraso}. Multa: R${multa}.")
         else:
            print(f"Livro {titulo} devolvido dentro do prazo.")
         
         self.livros[titulo]["copias"] += 1
         del self.emprestimos[usuario]
      else:
         print(f"Usuário: {usuario} não tem livros emprestados.")
   
   def atualizar_datas(self, usuario, nova_data_devolucao):
      if usuario in self.emprestimos:
         nova_data = datetime.strptime(nova_data_devolucao, "%d/%m/%Y")
         self.emprestimos[usuario]["data_devolucao"] = nova_data
         print(f"Data de devolução do livro atualizado para {nova_data.strftime('%d/%m/%Y')}.")
      else:
         print(f"Usuário '{usuario}' não tem livros emprestados")

# Exemplo de uso:
biblioteca = Biblioteca()

biblioteca.adicionar_livro("Código Limpo", "Robert C. Martin", 4)
biblioteca.adicionar_livro("Diário Estoico", "Ryan Holiday", 2)
biblioteca.adicionar_livro("Entendendo Algoritmos", "Aditya Y. Bhargava", 5)
print()
biblioteca.emprestimo_livro("Davi", "Código Limpo")
biblioteca.emprestimo_livro("Roberta", "Entendendo Algoritmos")
biblioteca.emprestimo_livro("Victor", "Diário Estoico")
print()
biblioteca.devolver_livro("Roberta")
print()
biblioteca.atualizar_datas("Davi", "01/09/2024")
print()
biblioteca.devolver_livro("Davi")

