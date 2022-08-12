#Patch notes 12/08:
#Utilitários versão 0.1: Criação da função mp para escolher qual cálculo realizar
#Utilitários versão 0.2: Criação da aba Conversor de temperaturas

#Conversão de Horas versão 0.5: Correção de variáveis inteiras para pontos flutuantes e remoção de vários if's por bloco de funções

#Conversor de Temperaturas versão 0.1: Adicionado a conversão de Celsius para Fahrenheit

#Conversão de Unidades de Medida: em desenvolvimento

#versões futuras:
#1 - fazer uma função para voltar no menu: ok (cdh0.5 e u0.1)
#2 - fazer uma nova operação ou não: ok (cdh0.5)
#3 - histórico de cálculos

global menu_tm_conv
global menu_tmp_conv
global menu_unt_conv
global mp

def mp():
 tst=int(input("*** Utilitários v0.2 ***\n1 - Conversão de Horas\n2 - Conversão de Temperaturas\n3 - Conversão de Unidades de Medida\n"))
 if tst==1:
  menu_tm_conv()
 elif tst==2:
  menu_tmp_conv()
 elif tst==3:
  menu_unt_conv()

def thnks_tmp():
 print("\n*** Obrigado por usar o Conversor de Temperaturas v0.1 ***")
 mp()   

def menu_tmp_conv():
 print("\n*** Conversor de Temperaturas v0.1*** Em desenvolvimento")
 op_tmp=int(input("*** Digite a opção e pressione ENTER ***\n1 - Converter Celsius para Fahrenheit\nDigite 0 para voltar ao menu:\n"))
 if op_tmp==0:
  thnks_tmp()
  mp()
 elif op_tmp==1:
    cel_fah()

def cel_fah():
 print("\n--- Convertendo Celsius para Fahrenheit ---")
 celsius=float(input("Insira o valor da temperatura em °C: "))
 fahrenheit=(1.8*celsius)+32
 print("{:.2f}°C são {:.2f}°F".format(celsius,fahrenheit))

 dec_cel=int(input("Deseja fazer a conversão novamente?\nDigite 1 - Sim ou 2 - Não"))
 if dec_cel==2:
  menu_tmp_conv()
 elif dec_cel==1:
  cel_fah()
    
def menu_unt_conv():
 print("Em desenvolvimento")
 mp()

def menu_tm_conv(): #menu das conversões de horas
 op_tm=int(input("*** Digite a opção e pressione ENTER ***\n1 - Converter Horas para Minutos\n2 - Converter Horas para Segundos\n3 - Converter Minutos para Horas\n4 - Converter Minutos para Segundos\nDigite 0 para retornar ao menu\n"))
 if(op_tm==0): #0 - Fechar o Programa:
  thnks()
  mp()
 elif (op_tm==1): #1 - Horas para Minutos:
  hr_mnt()
 elif (op_tm==2): #2 - Horas para Segundos:
  hr_sgd()
 elif (op_tm==3): #3 - Minutos para Horas:
  mnt_hr()
 elif (op_tm==4): #4 - Minutos para Segundos:
  mnt_sgd()
 print("")

def thnks(): #Agradecimentos
 print("\nObrigado por usar o Calculadora de Horas v0.5 (beta)")

def mnt_sgd(): #Minutos>Segundos
 minutos=float(input("\n--- Convertendo Minutos para Segundos ---\n   Digite o valor do Minuto: "))
 resultado=minutos*60
 if (minutos==1):
  print("\n*** Resultado ***\n{} minuto são {} segundos\n".format(minutos, resultado))
 elif (resultado==1):
  print("\n*** Resultado ***\n{} minuto é {} segundo\n".format(minutos, resultado))
 else:
  print("\n*** Resultado ***\n{} minutos são {} segundos\n".format(minutos, resultado))

 denovo=int(input("Deseja fazer essa operação novamente?\nDigite 1 - Sim ou 2 - Não\n"))
 if denovo==1:
  mnt_sgd() 
 else:
  menu_tm_conv()

def mnt_hr(): #Minutos>Horas
 minutos=int(input("\n--- Convertendo Minutos para Horas ---\n  Digite o minuto: "))
 resultado=round(minutos/60,2)
 if (minutos==1):
  print("\n*** Resultado ***\n{} minuto são {} horas\n".format(minutos, resultado))
 elif (resultado==1):
  print("\n*** Resultado ***\n{} minutos é {} hora\n".format(minutos, resultado))
 else:
  print("\n*** Resultado ***\n{} minutos são {} horas\n".format(minutos, resultado))

 denovo=int(input("Deseja fazer essa operação novamente?\nDigite 1 - Sim ou 2 - Não\n"))
 if denovo==1:
  mnt_hr() 
 else:
  menu_tm_conv()

def hr_sgd(): #Horas>Segundos
 hora=float(input("\n--- Convertendo Horas para Segundos ---\n   Digite a hora: "))
 resultado=hora*3600
 if (resultado == 1) or (hora==1):
  print("\n*** Resultado ***\n{} hora são {} segundos\n".format(hora, resultado))
 else:
  print("\n{} horas são {} segundos\n".format(hora, resultado))
 
 denovo=int(input("Deseja fazer essa operação novamente?\nDigite 1 - Sim e 2 - Não\n"))
 if denovo==1:
  hr_sgd() 
 else:
  menu_tm_conv()

def hr_mnt(): #Horas>Minutos
 hora=float(input("\n--- Convertendo Hora para Minuto ---\n   Digite as horas: "))
 resultado=hora*60
 if (hora==1):
  print("\n*** Resultado ***\n{} hora são {} minutos\n".format(hora, resultado))
 else:
  print("\n{} horas são {} minutos\n".format(hora, resultado))
 
 denovo=int(input("Deseja fazer essa operação novamente?\nDigite 1 - Sim ou 2 - Não\n"))
 if denovo==1:
  hr_mnt()
 else:
  menu_tm_conv()

mp()
