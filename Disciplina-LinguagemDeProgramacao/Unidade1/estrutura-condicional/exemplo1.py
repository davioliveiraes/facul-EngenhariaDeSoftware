# Estrutura condicional Simples
# Exemplo 1:
a = 5
b = 10

if a < b:
    print("a é menor do que b")
    r = a + b
    print(r)

# Exemplo 2
nota1 = 7
nota2 = 9

if nota1 < nota2:
    print(f"A nota1: ({nota1}) é menor que a nota2: ({nota2})")
    soma = nota1 + nota2
    media = soma / 2
    print(f"Soma das notas é: {soma}; Média das notas: {media}")

n = None
if n != None:
    print("n é diferente de None!")

x = 5
if x == 5:
    print("x é igual a 5")

y = 20
if y > 10:
    print("O número y é maior que 10!")

s = "HelloWorld"
if s == "HelloWorld":
    print(f"A string s é igual: {s}")

z = 10
if z >= 10:
    print("O número z é maior ou igual a 10")