class No:
   def __init__(self, valor):
      self.valor = valor
      self.esquerda = None
      self.direita = None

class ArvoreBinaria:
   def __init__(self):
      self.raiz = None
   
   def inserir(self, valor):
      if self.raiz is None:
         self.raiz = No(valor)
      else:
         self._inserir(self.raiz, valor)
      
   def _inserir(self, no, valor):
      if valor < no.valor:
         if no.esquerda is None:
            no.esquerda = No(valor)
         else:
            self._inserir(no.esquerda, valor)
      else:
         if no.direita is None:
            no.direita = No(valor)
         else:
            self._inserir(no.direita, valor)
   
   def buscar(self, valor):
      return self._buscar(self.raiz, valor)
   
   def _buscar(self, no, valor):
      if no is None or no.valor == valor:
         return no
      if valor < no.valor:
         return self._buscar(no.esquerda, valor)
      return self._buscar(no.direita, valor)
   
   def pre_ordem(self, no):
      if no:
         print(no.valor, end=' ')
         self.em_ordem(no.esquerda)
         self.em_ordem(no.direita)

   def em_ordem(self, no):
      if no:
         self.em_ordem(no.esquerda)
         print(no.valor, end=' ')
         self.em_ordem(no.direita)
   
   def pos_ordem(self, no):
      if no:
         self.pos_ordem(no.esquerda)
         self.pos_ordem(no.direita)
         print(no.valor, end=' ')
   
# Testando a implementação da Árvore Binária
arvore = ArvoreBinaria()
arvore.inserir(10)
arvore.inserir(5)
arvore.inserir(15)
arvore.inserir(2)
arvore.inserir(7)
arvore.inserir(12)
arvore.inserir(17)

# Percursos da árvore
print("Pré-ordem: ")
arvore.pre_ordem(arvore.raiz)

print("\nEm ordem: ")
arvore.em_ordem(arvore.raiz)

print("\nPós-ordem: ")
arvore.pos_ordem(arvore.raiz)

# Buscando um valor na árvore
print()
no_encontrado = arvore.buscar(int(input("Digite um número que deseja saber se tá inserido: ")))
if no_encontrado:
   print(f"\nValor: {no_encontrado.valor}, encontrado na árvore.")
else:
   print(f"\nValor não encontrado na árvore.")