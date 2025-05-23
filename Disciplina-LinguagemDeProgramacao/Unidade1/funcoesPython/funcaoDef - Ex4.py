def converter_maiusculo(texto, flag_maiusculo):
   if flag_maiusculo:
      return texto.upper()
   else:
      return texto.lower()

texto = converter_maiusculo(flag_maiusculo=True, texto="Davi")
print(texto)

def converter_minusculo(texto, flag_minusculo=True):
# O parâmetro flag_minuculo possuo True como valor default
   if flag_minusculo:
      return texto.lower()
   else:
      return texto.upper()

texto1 = converter_minusculo(flag_minusculo=True, texto="JavaScript é um linguagem de programação muito boa!")
texto2 = converter_minusculo(texto="Python é um excelente linguagem de programação!")

print(f"Texto 1: {texto1}")
print(f"Texto 2: {texto2}")
