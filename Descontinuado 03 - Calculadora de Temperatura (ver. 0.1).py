#Código descontinuado por conta do Utilitários, mas serviu de base para fazer adições no programa novo
Versões futuras: #Função para chamar a decisão
tw=0
print("Calculadora de temperaturas:")
while tw>=0:
 opcao=int(input("\nDigite o número para a operação \n1 - Celsius > Fahrenheit: "))
 if opcao==1:
  #Celsius para Fahrenheit:
  print("\nConvertendo Celsius para Fahrenheit")
  c=float(input("Informe a Temperatura em °C: "))
  f=(1.8*c)+32
  print("\nA temperatura de {}°C é {:.2f}°F".format(c,f))
  #Função para chamar a decisão
  decisao=str(input("\nDeseja continuar? Digite Sim ou não: "))
  if decisao == "Sim" or "sim":
   tw=tw+1
  else:
   tw=-1
