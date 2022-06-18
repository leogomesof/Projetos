#fazer uma função para voltar no menu/ fazer uma nova operação ou não...
a=0
while (a==0):
 print("*** calculadora de horas ver.0.2 (alpha)***")
 opcao=int(input("\nDigite a opção:\n1 - Converter Horas para Minutos\n2 - Converter Horas para Segundos"
                 "\nDigite 0 para fechar: "))
 #0 - Fechar o Programa
 if(opcao==0):
  a=a+1
 #1 - Horas Para Minuto
 if (opcao==1):
   hora = int(input("\n*** Convertendo Hora para Minuto***\n   Digite o valor para hora: "))
   resultado = hora * 60
   if (resultado == 1) or (hora == 1):
     print("\n*** Resultado ***\n{} hora é {} minutos\n".format(hora, resultado))
   else:
     print("\n{} horas são {} minutos.\n".format(hora, resultado))
