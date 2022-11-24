frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print(frase)
print("""Vamos flamengo
Vamos ser campeão, vamos flamengo
Minha maior nação vamos flamengo
VAMOS FLAMENGO!!!""")

print('Curso' in frase)
print(frase.find("Curso"))
print(frase.find("Vídeo"))
print(frase.find("video"))
dividido = frase.split()