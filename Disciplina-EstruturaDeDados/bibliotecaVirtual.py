class BibliotecaVirtual:
   def __init__(self):
      self.livros = {}
   
   def adicionar_livro(self, titulo, autor, ano):
      if titulo in self.livros:
         print(f"Livro já existente na biblioteca.")
      else:
         self.livros[titulo] = {'Autor': autor, "Ano": ano}
         print("Livro adicionado.")
   
   def remover_livro(self, titulo):
      if titulo in self.livros:
         del self.livros[titulo]
         print("Livro já removido com sucesso.")
      else:
         print("Livro já removido.")

   def pesquisar_livro(self, titulo):
      return self.livros.get(titulo, "Livro não encontrado")
   
   def listar_livros(self):
      for titulo, infos in self.livros.items():
         print(f"Titulo: {titulo} - Autor: {infos['Autor']} - (Ano: {infos['Ano']})")

# Exemplo de uso

biblioteca = BibliotecaVirtual()
biblioteca.adicionar_livro("Pai rico Pai pobre", "Robert T.Kiyosaki", 2000)
biblioteca.adicionar_livro("Os segredos da mente milionária", "T.Harv Eker", 2020)
print(biblioteca.pesquisar_livro("Pai rico Pai pobre"))
biblioteca.listar_livros()
biblioteca.remover_livro("Os segredos da mente milionária")
biblioteca.listar_livros()
