#esses valores de pixeis no .click() são de acordo com a minha resolução (1920x1080)
import pyautogui
import time
#abrindo navegador
pyautogui.alert(text='Iniciando o programa', title='Nead Opener 2.0', button='OK')
pyautogui.hotkey("winleft", "d")
pyautogui.write("c")
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey("winleft", "up")
#acessando o site
pyautogui.write("http://www2.ugb.edu.br/")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(715,107)
time.sleep(1)
pyautogui.click(745,505)
#colocando a matrícula e a senha
a=pyautogui.password(text='Digite a sua matrícula: ', title='Nead Opener 2.0')
pyautogui.write(a)
pyautogui.click(723,567)
b=pyautogui.password(text='Digite a sua senha: ', title='Nead Opener 2.0', mask='*')
pyautogui.write(b)
pyautogui.press("enter")
#acessando o NEAD
time.sleep(2)
pyautogui.click(146,799)
time.sleep(3)
pyautogui.alert("Bem-vindo ao NEAD-UGB")
