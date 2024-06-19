# Função print()
nome = "Davi"
print(nome)

# Função input()
nome = input("Digite seu nome: ")
print(nome)

# Função int() - ex.1,2,3 e float() - ex. 1.2, 2.4
numero = input("Digite um número inteiro: ")
numero = int
print(numero)
numero = int(input("Digite um número inteiro: "))
print(numero)

numero2 = input("Digite um número decimal: ")
numero2 = float
print(numero2)
numero2 = float(input("Digite um número decimal: "))
print(numero2)

# Função type() - Mostra o tipo de dado recebido em uma variável
x = 22
nome = "Davi"
nota = 7.50
fez_inscricao = True

print(type(x))
print(type(nome))
print(type(nota))
print(type(fez_inscricao))

# Mais utilização da função type()
a = 2 
b = 0.5
c = 1
x = input("Digite o valor de x: ")

print(type(a))
print(type(b))
print(type(c))
print(type(x))

x = float(x)
y = a * x ** 2 + b * x + c
print(f"O resultado da equação y com valor {x} é igual {y}")

print(type(a))
print(type(b))
print(type(c))
print(type(x))
