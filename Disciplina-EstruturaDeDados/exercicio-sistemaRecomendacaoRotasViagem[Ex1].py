import itertools

def calcular_distancia_total(cidades, grafo):
   distancia_total = 0
   for i in range(len(cidades) - 1):
      distancia_total += grafo[cidades[i]][cidades[i + 1]]
   distancia_total += grafo[cidades[-1]][cidades[0]]
   return distancia_total

def tsp_held_karp(grafo):
   n = len(grafo)
   memo = {}
   for k in range (1, n):
      memo[(1 << k, k)] = (grafo[0][k], 0)
   
   for subset_size in range(2, n):
      for subset in itertools.combinations(range(1, n), subset_size):
         bits = 0
         for bit in subset:
            bits |= 1 << bit
         for k in subset:
            prev_bits = bits & ~(1 << k)
            res = []
            for m in subset:
               if m == k:
                  continue
               res.append((memo[(prev_bits, m)][0] + grafo[m][k], m))
            memo[(bits, k)] = min(res)
   bits = (1 << n) - 2
   res = []
   for k in range(1, n):
      res.append((memo[(bits, k)][0] + grafo[k][0], k))
   opt, parent = min(res)

   caminho = []
   for i in range(n - 1):
      caminho.append(parent)
      bits &= ~(1 << parent)
      if (bits, parent) in memo:
         _, parent = memo[(bits, parent)]
      else:
            print(f"Chave {bits, parent} não encontrada no memo.")
   
   caminho.append(0)
   caminho.reverse()

   return caminho, opt

grafo = [
   [0, 29, 20, 31],
   [29, 0, 15, 17],
   [20, 15, 8, 28],
   [21, 17, 28, 0]
]

caminho, distancia_minima = tsp_held_karp(grafo)
print(f"Caminho mais curto: {caminho}")
print(f"Distância mínima: {distancia_minima}")

def tsp_vizinho_proximo(grafo, cidade_inicial=0):
   n = len(grafo)
   visitadas = [False] * n
   caminho = [cidade_inicial]
   visitadas[cidade_inicial] = True
   total_distancia = 0

   cidade_atual = cidade_inicial

   for _ in range(n - 1):
      prox_cidade = None
      menor_distancia = float('inf')

      for cidade in range(n):
         if not visitadas[cidade] and grafo[cidade_atual][cidade] < menor_distancia:
            menor_distancia = grafo[cidade_atual][cidade]
            prox_cidade = cidade
      
      caminho.append(prox_cidade)
      visitadas[prox_cidade] = True
      total_distancia += menor_distancia
      cidade_atual = prox_cidade
   
   total_distancia += grafo[cidade_atual][cidade_inicial]
   caminho.append(cidade_inicial)

   return caminho, total_distancia

caminho, distancia_total = tsp_vizinho_proximo(grafo)
print(f"\nCaminho mais curto (Heurística do Vizinho mais Próximo): {caminho}")
print(f"Distância total: {distancia_total}")
