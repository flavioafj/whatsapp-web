from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time
import main
import os


def resposta(driver, escolha):
    
    

    if escolha == "1":

        resp = f"""Caro cliente,\\n\
        \\n\
        Estamos entrando em contato para confirmar sua reserva no estacionamento Pátio Confins para amanhã. Peço gentilmente que responda com *SIM*, caso a reserva esteja confirmada, e com *NÃO*, caso você não possa comparecer.\\n\
        \\n\
        Muito obrigado,"""

    elif escolha == "-1":

        resp = f"""Caro cliente,\\n\
        \\n\
        Somos do estacionamento Pátio Confins e estamos entrando em contato com o intuito de aprimorar nossos serviços. Peço gentilmente que nos informe o motivo do seu não comparecimento, conforme reserva marcada para ontem, para que possamos entender melhor a necessidade dos nossos clientes.\\n\
        Sua colaboração é muito importante, desde já, muito obrigado pela participação.\\n\
        \\n\
        Atenciosamente,"""

    else:

        print("Resposta inválida")


    global ultima_mensagem
    if resp != "":
       
        if ultima_mensagem != resp:        
            main.send_keys2(driver, resp)
            time.sleep(1)


if __name__ == "__main__":

    diretorio = "Cliente"

    driver = webdriver.Chrome(executable_path=r'chromedriver.exe')

    driver.get("https://web.whatsapp.com/")
    el = WebDriverWait(driver, timeout=60).until(lambda d: d.find_element(By.CSS_SELECTOR, '#pane-side'))

    x = datetime.datetime.now()

    nome =str('{:02d}'.format(x.year)) + "-" + str('{:02d}'.format(x.month)) + "-" + str(x.day)
    ultima_mensagem = ""
    
    
    escolha = "9"

    while escolha != "0":

        escolha = input("Digite -1 para mensagens de ontem, 1 para mensagens de amanhã ou 0 para terminar:")
        
        if escolha != "0":

            j = open("C:\\Users\\" + diretorio + "\\Downloads\\" + nome + ".txt", "r", encoding="utf-8")
            numeros = j.read()

            matriz_numeros =  numeros.split("\n")

            for n in matriz_numeros:

                if n != '':


                    #n = n.replace("550","55")
                    driver.get("https://wa.me/" + n.replace("+",""))
                    time.sleep(1)
                    
                    try:
                        el = WebDriverWait(driver, timeout=2).until(lambda d: d.find_element(By.CSS_SELECTOR, '#action-button'))
                        
                        el.click()
                    except:

                        time.sleep(2)
                        driver.get("https://wa.me/" + n.replace("+",""))
                        time.sleep(1)
                        el = WebDriverWait(driver, timeout=2).until(lambda d: d.find_element(By.CSS_SELECTOR, '#action-button'))
                        
                        el.click()

                    time.sleep(1)
                    el2 = WebDriverWait(driver, timeout=4).until(lambda d: d.find_element(By.CSS_SELECTOR, '#fallback_block > div > div > a'))
                    el2.click()

                    try:
                        msg = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CSS_SELECTOR, '#main div[aria-label="Lista de mensagens. Pressione a seta para direita em uma mensagem para abrir o menu da mensagem."]'))
                    except:
                        

                        if len(driver.find_elements(By.CSS_SELECTOR, "._3J6wB"))>0:

                            print("Não foi possível enviar mensagem para o número " + n + " devido a: " + driver.find_element(By.CSS_SELECTOR, "._3J6wB").text)

                            continue

                    try:
                        mensagens = msg.find_elements(By.CSS_SELECTOR, 'span.copyable-text')
                    except:
                        msg = WebDriverWait(driver, timeout=4).until(lambda d: d.find_element(By.CSS_SELECTOR, '#main div[aria-label="Lista de mensagens. Pressione a seta para direita em uma mensagem para abrir o menu da mensagem."]'))
                        mensagens = msg.find_elements(By.CSS_SELECTOR, 'span.copyable-text')
                        
                    resposta(driver, escolha)
                    print(n.replace("+",""))

            j.close()
            os.remove("C:\\Users\\"+ diretorio + "\\Downloads\\" + nome + ".txt")
            matriz_numeros.clear()
