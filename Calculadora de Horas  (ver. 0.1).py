a=1
print("*** calculadora de horas ver.0.1 (alpha)***\n")
while a==1:
 opcao1=int(input("Digite a opção:\n1 - Converter horas para minutos\n2 - Converter horas para segundos\n"
    "3 - Converter minutos para horas\n4 - Converter minutos para segundos\n"))
 if(opcao1==1):
    hora=int(input("\nDigite o valor para hora: "))
    resultado=hora*60
    print("\n{} horas são {} minutos.\n".format(hora, resultado))
 elif(opcao1==2):
    hora=int(input("\nDigite o valor para hora: "))
    resultado=hora*3600
    print("\n{} horas são {} segundos\n".format(hora,resultado))
 elif(opcao1==3):
    minutos=int(input("\nConvertendo Minutos para Horas:\nDigite o valor dos minutos: "))
    resultado=minutos/60
    if(resultado<=1):
        print("\n*** Resultado ***\n{} minutos3 é {} hora\n".format(minutos, resultado))
    else:
        print("\n*** Resultado ***\n{} minutos são {} horas\n".format(minutos,resultado))
