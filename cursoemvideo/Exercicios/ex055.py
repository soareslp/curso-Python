'''LER O PESO DE CINCO PESSOAS E FALAR QUAL MAIOR E QUAL O MENOR'''
pesoMaior = 0
pesoMenor = 0
for c in range(1, 6):
    peso = float(input('Digite {}º peso: '.format(c)))
    if c == 1:
        pesoMenor = peso
        pesoMaior = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        elif peso < pesoMenor:
            pesoMenor = peso
print("PESO MAIOR: {}\nPESO MENOR: {}".format(pesoMaior, pesoMenor))


