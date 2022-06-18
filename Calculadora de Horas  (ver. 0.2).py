#fazer uma função para voltar no menu/ fazer uma nova operação ou não...
a=0
print("*** calculadora de horas ver.0.2 (alpha)***")
while (a==0):
 opcao=int(input("Digite a opção:\n1 - Converter Horas para Minutos\n2 - Converter Horas para Segundos"
                 "\nDigite 0 para fechar: "))
 #0 - Fechar o Programa
 if(opcao==0):
  a=a+1
 #1 - Horas para Minutos
 if (opcao==1):
   hora=int(input("\n*** Convertendo Hora para Minuto ***\n   Digite o valor para hora: "))
   resultado=hora*60
   #Colocando a frase no singular
   if (hora==1):
     print("\n*** Resultado ***\n{} hora são {} minutos\n".format(hora, resultado))
   #Colocando a frase no plural
   else:
     print("\n{} horas são {} minutos.\n".format(hora, resultado))
 #2 - Horas para Segundos
 if (opcao==2):
  hora=int(input("\nDigite o valor para hora: "))
  resultado=hora*3600
  if (resultado == 1):
   print("\n*** Resultado ***\n{} minutos é {} hora\n".format(hora, resultado))
  else:
   print("\n{} horas são {} segundos\n".format(hora, resultado))
