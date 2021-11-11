import pyautogui
import time


def llenar_forms(com, cita, tiempo, emaili, emailf):
    time.sleep(1.5)
    # Posicionamos el click en la primer pregunta
    pyautogui.click(x=488, y = 444, clicks = 1)
    if com == 2:
        pyautogui.press('down')
    elif com == 3:
        pyautogui.press('down')
        pyautogui.press('down')
    elif com == 4:
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
    # Hacemos 2 tabs para llenar el espacio vacio
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite(cita)

    # Presionamos otros 2 tabs, pero con un espacio de 1 segundo
    # Ya que luego se bugea un poco
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    # Damos enter para seleccionar la respuesta
    pyautogui.press('enter')
    # Repetimos la operacion hasta llegar al numero deseado
    for i in range(tiempo - 1):
        pyautogui.press('down')
        time.sleep(1)
    pyautogui.press('enter')

    # Volvemos a tabular para la siguiente opcion 
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite(emaili)
    time.sleep(.5)
    pyautogui.hotkey('altright', '2')
    time.sleep(.5)
    pyautogui.typewrite(emailf)
    # Hacemos un último tab y terminamos con un enter
    pyautogui.press('tab')
    pyautogui.press('enter')

def preguntas():
    comics = int(input("""¿Que prefiere?
[1] Marvel
[2] DC
[3] Ambos
[4] Ninguno
Opcion: """))
    while comics < 0 or comics > 4:
        comics = int(input("Agrege una opcion valida: "))
    cita = input("Agrege una cita, dicho, o frase: ")
    tiempo = int(input("""¿Que hora prefiere para comer pastel?
[1] 8 AM
[2] 9 AM
[3] 10 AM
[4] 11 AM
[5] 12 PM
[6] 1 PM
[7] 2 PM
[8] 3 PM
[9] 4 PM
[10] 5 PM
[11] 6 PM
[12] Despues de las 7 PM
Opcion: """))
    while tiempo < 0 or tiempo > 12:
        tiempo = int(input("Agrege una opcion valida: "))

    emaili = input("Agrege el correo antes del @: ")
    emailf = input("Agrege a que organizacion corresponde(hotmail.com): ")

    return comics, cita, tiempo, emaili, emailf

cont = 0
y = 1
forms = int(input("¿Cuantas veces desea llenar el formulario? "))
if forms > 1:
    y = int(input("""¿Desea usar las mismas respuestas en su llenado?
[1] Si
[2] No
Opcion: """))
while y < 1 or y > 2:
    y = int(input("Ponga una opcion valida: "))
while cont < forms:
    
    if y == 2:
        comics = []
        cita = []
        emaili = []
        emailf = []
        tiempo = []
        for i in range(forms):
            com, cit, tiemp, emai, emaf = preguntas()
            comics.append(com)
            cita.append(cit)
            tiempo.append(tiemp)
            emaili.append(emai)
            emailf.append(emaf)
        for i in range(forms):
            llenar_forms(comics[i], cita[i], tiempo[i], emaili[i], emailf[i])
            if forms - 1 > cont:
                time.sleep(1)
                pyautogui.press('f5')
                time.sleep(1)
                pyautogui.click(x=488, y = 444, clicks = 1)
            cont += 1
    else:
        if cont == 0:
            comics, cita, tiempo, emaili, emailf = preguntas()
        llenar_forms(comics, cita, tiempo, emaili, emailf)
        time.sleep(2)
        if forms - 1 > cont:
            pyautogui.press('f5')
            time.sleep(3)
        cont += 1
