# Estrutura encadeado, devemos usar o comando 'elif', que é uma abreviação de else if

codigo_compra = 3344

if codigo_compra == 3322:
    print("A compra só de pode ser efetuada à vista.")
elif codigo_compra == 2233:
    print(f"A compra pode ser efetuada à prazo, só que apenas no boleto.")
elif codigo_compra == 3344:
    print(f"A compra pode ser efetuada à prazo, tanto no boleto como também no cartão de crédito.")
else:
    print("Código de compra não cadastrado.")

