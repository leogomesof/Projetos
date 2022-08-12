#Utilitários versão 0.1: criação da função mp para escolher qual cálculo realizar
#Conversão de Horas versão 0.5: Correção de variáveis inteiras para pontos flutuantes e remoção de vários if's por bloco de funções
#Conversão de Temperaturas: Em desenvolvimento
#Conversão  de Unidades de Medida: em desenvolvimento

#versões futuras:
#1 - fazer uma função para voltar no menu: ok (cdh0.5 e u0.1)
#2 - fazer uma nova operação ou não: ok (cdh0.5)
#3 - histórico de cálculos

global menu_tm_conv
global menu_tmp_conv
global menu_unt_conv
global mp

def mp():
 tst=int(input("*** Utilitários ver:0.1 ***\n1 - Conversão de Horas\n2 - Conversão de Temperatura\n3 - Conversão de Unidades de Medida\n"))
 if tst==1:
  menu_tm_conv()
 elif tst==2:
  menu_tmp_conv()
 elif tst==3:
  menu_unt_conv()

def menu_tmp_conv():
 print("Em desenvolvimento")
 mp()

def menu_unt_conv():
 print("Em desenvolvimento")
 mp()

def menu_tm_conv(): #menu das conversões de horas
 opcao=int(input("*** Digite a opção e pressione ENTER: ***\n1 - Converter Horas para Minutos\n2 - Converter Horas para Segundos\n3 - Converter Minutos para Horas\n4 - Converter Minutos para Segundos\nDigite 0 para retornar ao menu\n"))
 if(opcao==0): #0 - Fechar o Programa:
  thnks()
  mp()
 elif (opcao==1): #1 - Horas para Minutos:
  hr_mnt()
 elif (opcao==2): #2 - Horas para Segundos:
  hr_sgd()
 elif (opcao==3): #3 - Minutos para Horas:
  mnt_hr()
 elif (opcao==4): #4 - Minutos para Segundos:
  mnt_sgd()
 print("")

def thnks(): #Agradecimentos
 print("\nObrigado por usar o Calculadora de Horas ver.0.5 (beta)")

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
