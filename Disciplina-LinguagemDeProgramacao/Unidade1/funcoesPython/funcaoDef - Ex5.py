def imprimir_parametros(*args):
   qtde_parametros=len(args)
   print(f"Quantidade de parâmetros: {qtde_parametros}")

   for i, valor in enumerate(args):
      print(f"Posição: {i} - Valor: {valor}")
   
print("CHAMADA 1")
imprimir_parametros("Fortaleza", 10, 23.6, "Davi")

print("CHAMADA 2")
imprimir_parametros(10, "Fortaleza")

print()

def imprimir_parametros2(**kwargs):
   print(f"O tipo de objeto recebido: {type(kwargs)}")
   qtde_parametros = len(kwargs)
   print(f"Quantidade de parâmetros: {qtde_parametros}")

   for chave, valor in kwargs.items():
      print(f"Variável: {chave} - Valor: {valor}")

print("CHAMADA 1")
imprimir_parametros2(cidade="São     Paulo", idade=29, nome="Gevaldo")

print("CHAMADA 2")
imprimir_parametros2(cidade="Konoha", idade=20, nome="Sasuke")

print("CHAMADA 3")
imprimir_parametros2(desconot=10, valor=100)

somar = lambda x, y: x + y
resultado = somar(x=2, y=5)
print(resultado)
