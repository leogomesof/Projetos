#fazer uma função para voltar no menu/ fazer uma nova operação ou não...
a=1
b=0
while(b>=0):
    print("*** calculadora de horas ver.0.2 (alpha)***\n")
    opcao=int(input("Digite a opção:\n1 - Converter horas para minutos\n2 - Converter horas para segundos\n"
    "3 - Converter minutos para horas\n4 - Converter minutos para segundos\nDigite 0 para fechar:\n"))
if(opcao==0):
    a=2
else:
    while a==1:
        if(opcao==1):
            hora=int(input("\n*** Convertendo Hora para Minuto***\n   Digite o valor para hora: "))
            resultado=hora*60
            if(resultado==1) or (hora==1):
             print("\n*** Resultado ***\n{} hora é {} minutos\n".format(hora, resultado))
            else:
             print("\n{} horas são {} minutos.\n".format(hora, resultado))
            b=b+1 
        elif(opcao==2) or (hora==1):
            hora=int(input("\nDigite o valor para hora: "))
            resultado=hora*3600
            if(resultado==1):
                print("\n*** Resultado ***\n{} minutos é {} hora\n".format(hora1, resultado))
            else:
                print("\n{} horas são {} segundos\n".format(hora,resultado))
        elif(opcao==3):
            minutos=int(input("\nConvertendo Minutos para Horas:\nDigite o valor dos minutos: "))
            resultado=round(minutos/60 , 2)
            if(resultado==1):
                print("\n*** Resultado ***\n{} minutos é {} hora\n".format(minutos, resultado))
            else:
                print("\n*** Resultado ***\n{} minutos são {} horas\n".format(minutos,resultado))
        elif(opcao==4):
            minutos=int(input("\nConvertendo Minutos para Segundo:\nDigite o valor dos Minutos: "))
            resultado=minutos*60
            if(resultado==1):
                print("\n*** Resultado ***\n{} minutos é {} segundo\n".format(minutos, resultado))
            else:
                print("\n*** Resultado ***\n{} minutos são {} segundos\n".format(minutos,resultado))
