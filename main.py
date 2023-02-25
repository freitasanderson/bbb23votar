import pyautogui
import time

time.sleep(3)

repeat = 10000

for i in range(repeat):
    pyautogui.press('PageDown')

    print(f'Votos até o momento: {i}')
######## Selecionar voto

    quemVotar = pyautogui.locateOnScreen('img/QuemVotar.png',confidence=.65)

    
    while not quemVotar:

        print(f'Como não achei to descendo')

        time.sleep(1)

        quemVotar = pyautogui.locateOnScreen('img/QuemVotar.png',confidence=.65)

        print(quemVotar)
        
        if quemVotar:
            print(f'Valor: X:{quemVotar.left} Y:{quemVotar.top}')


    x = quemVotar.left + (quemVotar.width / 2)
    y = quemVotar.top + (quemVotar.height / 2)

    print(f'x:{x} y:{y}')

    pyautogui.click(x, y)


######## Captcha
    time.sleep(2)

    captcha = pyautogui.locateOnScreen('img/captcha.png',confidence=.65)
    print(f'Captcha: {captcha}')

    while not captcha:

        captcha = pyautogui.locateOnScreen('img/captcha.png',confidence=.65)

        if not captcha:
            quemVotar = pyautogui.locateOnScreen('img/QuemVotar.png',confidence=.65)

            if quemVotar:
                x = quemVotar.left + (quemVotar.width / 2)
                y = quemVotar.top + (quemVotar.height / 2)
                pyautogui.click(x, y)
            
            if not quemVotar:
                repeat = pyautogui.locateOnScreen('img/botao.png',confidence=.65)
                
                if repeat:
                    x = repeat.left + (repeat.width / 2)
                    y = repeat.top + (repeat.height / 2)

                    pyautogui.click(x, y)


    x = captcha.left + (captcha.width / 2)
    y = captcha.top + (captcha.height / 2)
    
    pyautogui.click(x, y)

###### Votar novamente
    time.sleep(1)

    repeat = pyautogui.locateOnScreen('img/botao.png',confidence=.65)

    print(f'Repeat:{repeat}')

    while not repeat:
        time.sleep(1)

        repeat = pyautogui.locateOnScreen('img/botao.png',confidence=.65)
        
        time.sleep(1)

        if not repeat:
            time.sleep(1)

            captcha = pyautogui.locateOnScreen('img/captcha.png',confidence=.65)
            
            time.sleep(1)
        
            if captcha:
                time.sleep(1)

                x = captcha.left + (captcha.width / 2)
                y = captcha.top + (captcha.height / 2)
                pyautogui.click(x, y)

    time.sleep(2)

    botao = pyautogui.locateCenterOnScreen('img/botao.png',confidence=.65)
    
    time.sleep(1)

    while not botao:
        botao = pyautogui.locateCenterOnScreen('img/botao.png',confidence=.65)

    time.sleep(1)
    print(f'Botão: {botao}')

    x , y = botao

    print(f'Repeat:{repeat}')

    pyautogui.click(x, y)

    time.sleep(2)