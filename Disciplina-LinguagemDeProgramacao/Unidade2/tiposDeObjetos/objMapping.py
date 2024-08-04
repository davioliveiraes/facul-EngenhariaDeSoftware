dici_1 = {}
dici_1['nome'] = 'Davi'
dici_1['idade'] = 24
print(dici_1)

print()

dici_2 = {'nome': 'Davi', 'idade': 24}
print(dici_2)

print()

dici_3 = dict([('nome', "Davi"), ('idade', 24)])
print(dici_3)

print()

dici_4 = dict(zip(['nome', 'idade'], ["Davi", 24]))
print(dici_4)

print()

print(dici_1 == dici_2 == dici_3 == dici_4)
