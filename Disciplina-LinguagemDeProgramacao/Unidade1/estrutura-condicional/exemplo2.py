# Estrutura condicional composta
# Exemplo 1
a = 10
b = 5

if a < b:
    print("a é menor do que b")
    r = a + b
    print(r)
else:
    print("a é maior do que b")
    r = a - b
    print(r)

# Exemplo 2
nota1 = 10
nota2 = 20

if nota1 < nota2:
    print(f"A nota1:({nota1}) é menor que a nota2:({nota2})")
else:
    print(f"A nota1:({nota1}) não é menor que a nota2:({nota2})")

soma = nota1 + nota2
media = soma / 2
print(f"Soma das notas: {soma}; Média das notas: {media}")
