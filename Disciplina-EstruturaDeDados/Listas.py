frutas = ["maça", "banana", "cereja", "laranja"]
print(frutas)

frutas.append("kiwi")
print(frutas)

frutas.insert(1, "manga")
print(frutas)

frutas.remove("cereja")
print(frutas)

del frutas[0]
print(frutas)

frutas.pop()
print(frutas)

frutas[1] = "abacate"
print(frutas)

if "abacate" in frutas:
   print("Sim, o abacate tem na lista.")

print(f"Lista final: {frutas}")
print(len(frutas))

vegetais = ["cenoura", "batata"]
hortifruti = frutas + vegetais
print(hortifruti)

copia_frutas = frutas.copy()
print(copia_frutas)

frutas.sort()
print(frutas)

frutas.reverse()
print(frutas)

print(frutas.count("laranja"))
print(frutas.index("laranja"))

frutas.clear()
print(frutas)

# Exemplo de List Comprehension
# Sem Comprehension
numeros = [1, 2, 3, 4, 5]
quadrado_pares = []
for numero in numeros:
   if numero % 2 == 0:
      quadrado_pares.append(numero ** 2)
print(f"Lista do ao quadrado dos números pares: {quadrado_pares}")

# Com Comprehension
numeros2 = [1, 2, 3, 4, 5]
quadrado_pares2 = [numero ** 2 for numero in numeros if numero % 2 == 0]
print(f"Lista do ao quadrado dos números pares: {quadrado_pares2}")
