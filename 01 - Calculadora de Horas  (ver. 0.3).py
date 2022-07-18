#versões futuras:
#fazer uma função para voltar no menu
#fazer uma nova operação ou não...
#histórico
a=0
print("*** Calculadora de horas ver.0.3 (alpha)***")
while (a==0):
 opcao=int(input("Digite a opção:\n"
                 "1 - Converter Horas para Minutos\n"
                 "2 - Converter Horas para Segundos\n"
                 "3 - Converter Minutos para Horas\n"
                 "4 - Converter Minutos para Segundos\n"
                 "Digite 0 para fechar:\n"))
#0 - Fechar o Programa:
 if(opcao==0):
  print("\nObrigado por usar o Calculadora de Horas ver.0.3 (alpha)")
  a=a+1
#1 - Horas para Minutos:
 if (opcao==1):
   hora=int(input("\n--- Convertendo Hora para Minuto ---\n   Digite a hora: "))
   resultado=hora*60
  #Colocando a frase no singular:
   if (hora==1):
     print("\n*** Resultado ***\n{} hora são {} minutos\n".format(hora, resultado))
  #Colocando a frase no plural:
   else:
     print("\n{} horas são {} minutos\n".format(hora, resultado))
#2 - Horas para Segundos:
 if (opcao==2):
  hora=int(input("\n--- Convertendo Horas para Segundos ---\n   Digite a hora: "))
  resultado=hora*3600
  if (resultado == 1) or (hora==1):
   print("\n*** Resultado ***\n{} hora são {} segundos\n".format(hora, resultado))
  else:
   print("\n{} horas são {} segundos\n".format(hora, resultado))
#3 - Minutos para Horas:
 if (opcao==3):
  minutos=int(input("\n--- Convertendo Minutos para Horas ---\n  Digite o minuto: "))
  resultado=round(minutos/60,2)
  if (minutos==1):
   print("\n*** Resultado ***\n{} minuto são {} horas\n".format(minutos, resultado))
  elif (resultado==1):
   print("\n*** Resultado ***\n{} minutos é {} hora\n".format(minutos, resultado))
  else:
   print("\n*** Resultado ***\n{} minutos são {} horas\n".format(minutos, resultado))
#4 - Minutos para Segundos:
 if (opcao==4):
  minutos=int(input("\n--- Convertendo Minutos para Segundos ---\n   Digite o valor dos Minutos: "))
  resultado=minutos*60
  if (minutos==1):
   print("\n*** Resultado ***\n{} minuto são {} segundos\n".format(minutos, resultado))
  elif (resultado==1):
   print("\n*** Resultado ***\n{} minuto é {} segundo\n".format(minutos, resultado))
  else:
   print("\n*** Resultado ***\n{} minutos são {} segundos\n".format(minutos, resultado))
