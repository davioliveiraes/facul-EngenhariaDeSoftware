# Parte 1: Inicialização e difinição da função hash
hashtable = {} # Inicialização a tabela hash como um dicionário vazio
m = 10 # Define o número de índices na tabela hash

# Função hash usando o método da divisção
def hashfunct(v, mh):
   return v % mh # Retorna o índice para armazenamento

# Inicializa a tabela hash com listas vazias para tratamento de colisões
for i in range(m):
   hashtable[i] = [] # Cada índice inicia como uma lista vazia

# Parte 2: Função da inserção com tratamento de colisões (encadeamento separado)
def insereTC(valor):
   indice = hashfunct(valor, m)
   hashtable[indice].append(valor)

# Parte 3: Inserção de valores na tabela hash
insereTC(235)
insereTC(578)
insereTC(1024)
insereTC(96)
insereTC(32)
insereTC(18) # Este valor causa colisão com o valor 96, por exemplo

# Parte 4: Exibe o estado atual da tabela hash após as inserções
print("Tabela hash após inserções: ")
for indice, valores in hashtable.items():
   print(f"Índice {indice}: {valores}")

# Função para buscar um valor na tabela hash
def buscar(hashtable, valor):
   indice = hashfunct(valor, m)
   if valor in hashtable[indice]:
      return f"Valor {valor} encontrado no índice {indice}."
   else:
      return f"Valor {valor} não encontrado na tabela hash."

# Testes de busca de valores na tabela hash
print(buscar(hashtable, 1024)) # Valor inserido
print(buscar(hashtable, 99)) # Valor não inserido