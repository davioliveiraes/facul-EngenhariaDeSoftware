# Parte 1: Inicialização da tabela hash como um dicionário com listas vazias
hashtable = {}
m = 10 # Número de índices (ou 'buckets') na tabela hash

for i in range(m):
   hashtable[i] = [] # Cada índice da tabela inicia como uma lista vazia

# Parte 2: Definição da função hash
def hashfunct(v, mh):
   # v é o valor a ser armazenado e mh é o tamanho da tabela hash (m)
   return v % mh # Retorna o índice para armazenamento usando o método da divisão

# Parte 3: Função para inserir valores na tabela hash com tratamento de colisões
def inserir(hashtable, valor, m):
   indice = hashfunct(valor, m)
   hashtable[indice].append(valor) # Adiciona o valor à lista no índice apropriado

# Parte 4: Função para buscar valores na tabela hash
def buscar(hashtable, valor, m):
   indice = hashfunct(valor, m)
   if valor in hashtable[indice]:
      return f"Valor {valor} encontrado no índice {indice}"
   else:
      return f"Valor {valor} não encontrado na tabela hash"

# Inserção de valores na tabela hash
inserir(hashtable, 235, m)
inserir(hashtable, 578, m)
inserir(hashtable, 1024, m)
inserir(hashtable, 96, m)
inserir(hashtable, 32, m)
inserir(hashtable, 18, m) # Exemplo de colisão (18 e 96 têm o mesmo índice)

# Exibe o estado da tabela hash após as inserções 
print("Tabela hash após as inserções: ")
for indice, valores in hashtable.items():
   print(f"Índice {indice}: {valores}")

# Busca de valores na tabela hash
print(buscar(hashtable, 1024, m))
print(buscar(hashtable, 99, m)) # Valor não inserido