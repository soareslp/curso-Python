#Pegar a distância de uma viagem em Km e cobrar R$0,50 por Km até 200Km e R$0,45 para viagens mais longas
dis = float(input('Digite a distância da viagem em quilômetros: '))
if dis <= 200:
    print("O preço da passagem para uma distância de {}Km será de R${:.2f}".format(dis, dis*0.50))
else:
    print("O preço da passagem para uma distância de {}Km será de R${:.2f}".format(dis, dis * 0.45));