# Agora que você já entendeu como é comportamento da sintaxe utilize o emulador para testar o código. E se tivermos vários usuários python (userpy) para realizar a verificação da senha, como seria? Podemos utilizar a estrutura elif, para checar múltiplas condições e executar determinadas linhas de código. Observe o código para verificação de senha de 4 usuários cadastrados no sistema:

print("FAÇA SEU LOGIN: ")
endereco_email = input("Digite o endereço do seu email: ")
senha = input("Digite sua senha: ")

if endereco_email == "davioliveira@gmail.com" and senha == "senhadavi":
   print("BEM VINDO DAVI!")
elif endereco_email == "robertafreitas@gmail.com" and senha == "senharoberta":
   print("BEM VINDA ROBERTA!")
elif endereco_email == "victorhugo@gmail.com" and senha == "senhavictor":
   print("BEM VINDO VICTOR!")
elif endereco_email == "corinthiansoficial@gmail.com" and senha == "senhacorinthians":
   print("BEM VINDO CORINTHIANS OFICIAL!")
else:
   print("ERRO DE LOGIN, POR FAVOR VERIFIQUE EMAIL E SENHA, E TENTE NOVAMENTE.")

# As linhas 7, 9, 11 e 13 utilizamos a estrutura elif para verificar outras senhas de usuário. Na linha 15, 16, temos a estrutura
# else, que só será acionada se a entrada das linhas 4 e 5 for diferente dos logins e senhas permitidos.