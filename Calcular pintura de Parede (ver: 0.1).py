tw=0 #Trava o While
print("*"*12,"Calcular área da parede para pintura", "*"*12)
while tw>=0:
 largura=float(input("\nDigite a Largura da parede: "))
 altura=float(input("Digite a Altura da parede: "))
 area=largura*altura
 print("A área da sua parede é de: {}x{}m² e sua área é de: {}m²\n".format(largura,altura,area))
 rendimento=float(input("Digite o rendimento da sua lata de tinta: "))
 litro=area/rendimento #Exemplo a cada 2m de tinta, preciso de 1 litro
 print("Para você pintar essa parede, você precisa de {} litros de tintas\n".format(litro))
 decisao=str(input("Deseja continuar? Digite Sim ou Não: "))
 if decisao=="Sim" or "sim":
  tw=tw+1
 else:
   tw=-1
