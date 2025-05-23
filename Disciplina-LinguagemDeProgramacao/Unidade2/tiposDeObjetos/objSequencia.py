texto = "Aprendendo Python na disciplina de linguagem de programação"

print(f"Tamanho do texto = {len(texto)}")
print(f"Python in texto = {'Python' in texto}")
print(f"Quantidade de y no texto = {texto.count('y')}")
print(f"As 5 primeiras letras são: {texto[0:5]}")

print()

texto2 = "Aprendendo Python na disciplina de linguagem de programação"
print(f"texto = {texto2}")
print(f"Tamanho do texto = {len(texto2)}")

palavras = texto.split()
print(f"Palavras = {palavras}")
print(f"Quantidade de palavras = {len(palavras)}")

print()

linguagens = ["Python" , "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]
print(f"Antes da listcomp = {linguagens}")

linguagens = [item.lower() for item in linguagens]
print(f"Depois da listacomp = {linguagens}")

print()

print("Exemplo: ")
linguagens = "Python Java JavaScript C C# C++ Switf Go Kotlin".split()

nova_lista = map(lambda x: x.lower(), linguagens)
print(f"A nova lista é {nova_lista}")

nova_lista = list(nova_lista)
print(f"Agora sim, a nova lista é = {nova_lista}")

print()

numeros = list(range(0, 21))
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)

print()

vogais = ('a', 'e', 'i', 'o', 'u')
print(f"Tipo do objeto vogais = {type(vogais)}")

for p, x in enumerate(vogais):
   print(f"Posição: {p} - Seu valor: {x}")
