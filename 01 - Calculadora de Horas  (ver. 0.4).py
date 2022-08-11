#versões futuras:
#fazer uma função para voltar no menu de cálculos (Temperatura e outros cálculos)
#fazer uma nova operação ou não...
#histórico

#versão 0.4 notas da atualização: 
#Correção de variáveis inteiras para pontos flutuantes

global a

def hr_mnt():
 hora=float(input("\n--- Convertendo Hora para Minuto ---\n   Digite as horas: "))
 resultado=hora*60
 #Colocando a frase no singular:
 if (hora==1):
  print("\n*** Resultado ***\n{} hora são {} minutos\n".format(hora, resultado))
  #Colocando a frase no plural:
 else:
   print("\n{} horas são {} minutos\n".format(hora, resultado))

def hr_sgd():
 hora=float(input("\n--- Convertendo Horas para Segundos ---\n   Digite a hora: "))
 resultado=hora*3600
 if (resultado == 1) or (hora==1):
   print("\n*** Resultado ***\n{} hora são {} segundos\n".format(hora, resultado))
 else:
    print("\n{} horas são {} segundos\n".format(hora, resultado))

def mnt_hr():
 minutos=int(input("\n--- Convertendo Minutos para Horas ---\n  Digite o minuto: "))
 resultado=round(minutos/60,2)
 if (minutos==1):
  print("\n*** Resultado ***\n{} minuto são {} horas\n".format(minutos, resultado))
 elif (resultado==1):
  print("\n*** Resultado ***\n{} minutos é {} hora\n".format(minutos, resultado))
 else:
  print("\n*** Resultado ***\n{} minutos são {} horas\n".format(minutos, resultado))

def mnt_sgd():
 minutos=int(input("\n--- Convertendo Minutos para Segundos ---\n   Digite o valor dos Minutos: "))
 resultado=minutos*60
 if (minutos==1):
  print("\n*** Resultado ***\n{} minuto são {} segundos\n".format(minutos, resultado))
 elif (resultado==1):
  print("\n*** Resultado ***\n{} minuto é {} segundo\n".format(minutos, resultado))
 else:
  print("\n*** Resultado ***\n{} minutos são {} segundos\n".format(minutos, resultado))

def thnks():
 print("\nObrigado por usar o Calculadora de Horas ver.0.4 (beta)")
 global a
 a=a+1

print("*** Calculadora de horas ver.0.4 (beta)***")
while (a==0):
 opcao=int(input("Digite a opção e pressione ENTER:\n"
                 "1 - Converter Horas para Minutos\n"
                 "2 - Converter Horas para Segundos\n"
                 "3 - Converter Minutos para Horas\n"
                 "4 - Converter Minutos para Segundos\n"
                 "Digite 0 para fechar:\n"))
 if(opcao==0): #0 - Fechar o Programa:
  thnks()
 elif (opcao==1): #1 - Horas para Minutos:
  hr_mnt()
 elif (opcao==2): #2 - Horas para Segundos:
  hr_sgd()
 elif (opcao==3): #3 - Minutos para Horas:
  mnt_hr()
 elif (opcao==4): #4 - Minutos para Segundos:
  mnt_sgd()
