import array as arr

m = 15

hashtable = arr.array('i', [0] * m)

def hashfunct(v, mh):
   return v % mh

def insereTC(valor):
   hashtable[hashfunct(valor, m)] += 1

def retornaV(valor):
   return hashtable[hashfunct(valor, m)]

def menu():
   while True:
      print("\n--- MENU DE OPERAÇÕES ---")
      print("1. Inserir produto")
      print("2. Consultar quantidade de produtos de uma classe")
      print("3. Exibir tabela hash")
      print("4. Sair")

      opcao = input("Escolha uma opção: ")
      if opcao == "1":
         x = int(input("Digite o número da etiqueta do produto para inserir: "))
         insereTC(x)
         print(f"Produto com etiqueta {x} inserido na classe {hashfunct(x, m)}.")

      elif opcao == "2":
         x = int(input("Digite o número da etiqueta para consultar: "))
         quantidade = retornaV(x)
         print(f"Quantidade de produtos na classe {hashfunct(x, m)}: {quantidade}")
      
      elif opcao == "3":
         print("\nEstado atual da tabela hash: ")
         for indice , quantidade in enumerate(hashtable):
            print(f"Classe {indice}: {quantidade} produtos(s)")
      
      elif opcao == "4":
         print("Saindo do programa.")
         break
      
      else:
         print("Opção inválida. Tente novamente.")

menu()