# Imagine que você deseja acessar pela primeira vez algum sistema protegido por senha. Nesse exercício vamos implementar um simples verificador de senha do usuário e para isso utilizaremos as estruturas condicionais para permitir o login de um usuário. Vamos aplicar apenas as estruturas if-else.

print("FAÇA SEU LOGIN: ")
endereco_email = input("Digite o seu email: ")
senha = input("Digite sua senha: ")

if endereco_email == "davi@gmail.com" and senha == "senhateste":
   print("BEM VINDO DAVI!")
else:
   print("ERRO DE LOGIN, VERIFIQUE EMAIL E SENHA, E TENTE NOVAMENTE.")

# Nas linhas 4 e 5, input é a função que requisita os dados de login e senha do usuário. A estrutura condicional if-else, linhas 7 e 9, determinam se a condição será satisfeita e qual linha será executada. Na linha 7, é testado se o login e a senha do usuário são iguais a "userpy" and senha == "teste123“.