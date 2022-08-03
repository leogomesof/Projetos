#***Atenção***
#***Para usar esse programa, você precisa do pyautogui instalado na tua máquina***
#***Caso não tenha jogue no seu terminal esse comando: "install pip pyautogui" sem áspas e execute o programa***

#Esses valores de pixeis no .click() são de acordo com a minha resolução (1920x1080)
#Para ajustar a resolução, recomendo rodar um time.sleep(4) print(pyautogui.position()) para descobrir a posição do mouse e colocar no .click()

import pyautogui
import time

#bloco de função para inserir os dados
def data_input():
 global a
 a=pyautogui.password("Digite a sua matrícula: ",mask="*")
 if a==None:
  pyautogui.alert("Obrigado por usar o NEAD Opener 1.0")
 else:
  global b
  b=pyautogui.password('Digite a sua senha: ',mask="*")
  if b==None:
   pyautogui.alert("Obrigado por usar o NEAD Opener 1.0")

#bloco de função para abrir o chrome e acessar o nead
def chrm_NEAD():
 pyautogui.hotkey("winleft", "d")
 pyautogui.hotkey("winleft", "r")
 pyautogui.write("C:\Program Files\Google\Chrome\Application\chrome.exe")
 pyautogui.press("enter")
 time.sleep(1)
 pyautogui.hotkey("winleft", "up")
 pyautogui.write("http://www2.ugb.edu.br/")

#bloco de função para acessar a aba do nead
def nead_login():
 pyautogui.press("enter")
 time.sleep(2)
 pyautogui.click(715,107)
 time.sleep(1)
 pyautogui.click(745,505)
 time.sleep(5)
 pyautogui.click(121,852)
 time.sleep(1)

#bloco de função para receber os dados inseridos e colocá-los no site
def data_write():
 pyautogui.press("enter")
 time.sleep(2)
 pyautogui.click(715,107)
 time.sleep(1)
 pyautogui.click(745,505)
 pyautogui.write(a)
 pyautogui.click(723,567)
 pyautogui.write(b)
 pyautogui.press("enter")
 time.sleep(5)
 pyautogui.click(121,852)
 time.sleep(1)

#bloco de função para acessar o nead caso o usuário já tenha logado no site
def nav_acessoSL():
 pyautogui.hotkey("winleft", "d")
 pyautogui.write("c")
 pyautogui.press("enter")
 time.sleep(1)
 pyautogui.hotkey("winleft", "up")
 pyautogui.write("http://www2.ugb.edu.br/")
 pyautogui.press("enter")
 time.sleep(2)
 pyautogui.click(715,107)
 time.sleep(6)
 pyautogui.click(82,863)
 time.sleep(1)

#bloco de função para agradecimento
def obrigado():
  pyautogui.alert("Obrigado por usar o NEAD Opener 1.0\nAté logo!")

#bloco de função para boas vindas
def bem_vindo():
 pyautogui.alert("Bem-vindo ao NEAD-UGB\nObrigado por usar o programa!")

#início da programação
D1=pyautogui.confirm("Bem-vindo ao NEAD Opener 1.0.\nAperte OK para continuar ou Cancel para sair")
if D1=="Cancel":
 obrigado()
else:
 confirma=pyautogui.confirm("Para digitar sua matrícula aperte OK\nCaso já tenha aberto o NEAD aperte Cancel")
 if confirma=="OK":
  data_input()
  if a==None or b==None:
   print("")
  else:  
   chrm_NEAD()
   data_write()
   bem_vindo()
 elif confirma == "Cancel":
  chrm_NEAD()
  nead_login()
  bem_vindo()
