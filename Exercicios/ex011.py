a = float(input("Digite a altura da parede: "));
l = float(input("Digite a largura da parede: "));
s=a*l
print("A dimensão dessa parede é {}x{}."
      "\nPara printar essa parede de {}m²."
      "\nSerão necessários {}l de tinta."
      .format(a,l,s, (s/2)));