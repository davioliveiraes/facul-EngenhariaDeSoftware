vogais = 'aeiou'
resultado = vogais.index('a')
print(f"Posição vai ser: {resultado}")


vogais = 'aeiou'

try:
   letra_digitada = str(input("Digite uma letra: "))
   resultado = vogais.index(letra_digitada)
   print(f"A posição da letra vai ser: {resultado}")
except:
   print(f"Não foi possível encontrar a letra: {letra_digitada}")
