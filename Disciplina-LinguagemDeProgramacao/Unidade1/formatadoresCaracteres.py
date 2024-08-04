nome = input("Digite seu nome: ")

#Modo 1: Utilizando a linguagem em C
print("Olá %s, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world." %(nome))
print()
#Modo 2: Função .format
print("Olá {}, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world.".format(nome))
print()
#Modo 3: Strings Formatadas
print(f"Olá {nome}, bem vindo a disciplina de pragramação. Parabéns pelo seu primeiro hello world")
