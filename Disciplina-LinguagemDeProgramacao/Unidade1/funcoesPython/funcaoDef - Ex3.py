def calcular_desconto(valor, desconto = 0):
   valor_com_desconto = valor - (valor * desconto)
   return valor_com_desconto

valor1 = calcular_desconto(100) # Sem desconto
valor2 = calcular_desconto(100, 0.25) # Com desconto de 25%
print(f"Primeiro valor: R${valor1}")
print(f"Segundo valor: R${valor2}")

def calcular_desconto2():
   valor2 = float(input("Digite o valor a ser pago: R$"))
   desconto2 = int(input("Digite o desconto em percentual(%): "))
   valor_a_ser_pago = valor2 - (valor2 * (desconto2/100))
   return valor_a_ser_pago

print(f"O valor à ser pago vai ser de: R${calcular_desconto2():,.2f}")

def calcular_desconto3(preco_original, percentual_desconto):
   desconto = preco_original * (percentual_desconto/100)
   preco_com_desconto = preco_original - desconto
   