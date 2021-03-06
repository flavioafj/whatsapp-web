import datetime
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.remote.webelement import WebElement
import os

def resposta(driver,a):
    resp = switch_demo(a.lower())
    global ultima_mensagem
    if resp != "":
       
        if ultima_mensagem != a:        
            send_keys2(driver, resp)
            time.sleep(1)


            # vamos checar se a mensagem foi mesmo
            #se a mensagem não tiver sido enviada, tenta-se mais uma vez
            if not msg_foi(resp): 
                send_keys2(driver, resp)
                time.sleep(3)
                if msg_foi(resp):
                    ultima_mensagem = resp
                else:
                    resposta(driver,resp)
            
    else:
        ultima_mensagem = a
  
   
def msg_foi(a):
    retorno = bool(False)
    msg2 = driver.find_element(By.CSS_SELECTOR, '#main div[aria-label="Lista de mensagens. Pressione a seta para direita em uma mensagem para abrir o menu da mensagem."]')
    mensagens2 = msg2.find_elements(By.CSS_SELECTOR, 'span.copyable-text')
    quantas_mensagens2 = len(mensagens2)
    ultima_msg = mensagens2[quantas_mensagens2-1].text
    if limpa_espaco(a)[0:250] == limpa_espaco(ultima_msg)[0:250]: 
        retorno = bool(True)
    msg2 = mensagens2 = None
    quantas_mensagens2 = None
    return retorno

def limpa_espaco(a):
    r = ["\\n", "\\r","\n", "\r", "\\", "*", "```","_"]

    for i in r:
        a = a.replace(i, "")

    return a


def send_keys2(driver, keys: str):
    #função que escreve o texto (send_keys estava enviando mensagens com caracteres faltando)
    q_caixaTexto = "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa"
    q_caixaTexto2 = "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div"
    q_caixaTexto3 = "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1"
    q_verifica = "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text" 
    q_verifica = "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div.p3_M1"        
    q_botaoClica = "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k > button"

    #driver.execute_script('document.querySelector("' + q_verifica + '").innerText = "' + keys + '";')

    driver.find_element(By.CSS_SELECTOR, q_caixaTexto3).send_keys("1")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, q_caixaTexto3).send_keys(Keys.BACKSPACE)
    time.sleep(1)

    for parte in keys.split("\\r"):

        driver.find_element(By.CSS_SELECTOR, q_caixaTexto3).send_keys(parte)
        driver.find_element(By.CSS_SELECTOR, q_caixaTexto3).send_keys(Keys.SHIFT+Keys.ENTER)

    #driver.find_element(By.CSS_SELECTOR, q_caixaTexto3).send_keys(keys)

    if len(driver.find_elements(By.CSS_SELECTOR, q_botaoClica))==1:

        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, q_botaoClica).click()

    else:
        driver.find_element(By.CSS_SELECTOR, q_caixaTexto2).send_keys("2")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, q_caixaTexto2).send_keys(Keys.BACKSPACE)

        if len(driver.find_elements(By.CSS_SELECTOR, q_botaoClica))==1:
        
            time.sleep(1)

            driver.find_element(By.CSS_SELECTOR, q_botaoClica).click()
        
        else:

            driver.find_element(By.CSS_SELECTOR, q_caixaTexto).send_keys("3")
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, q_caixaTexto).send_keys(Keys.BACKSPACE)

            if len(driver.find_elements(By.CSS_SELECTOR, q_botaoClica))==1:

                time.sleep(1)

                driver.find_element(By.CSS_SELECTOR, q_botaoClica).click()


def switch_demo(argument):
    newline = '\n'
    switcher = {
        '1': f"""Nossas diárias são as seguintes:\\r\
        \\r\
        R$ 15,9 - vaga descoberta;\\r\
        R$ 23,9 - vaga coberta.\\r\
        \\r\
        Ressalto que as horas adicionais são cobradas da seguinte forma:\\r\
        \\r\
        primeira hora - R$ 3,5 (vaga descoberta) /R$ 4 (vaga coberta)\\r\
        demais horas - R$ 2,5 (vaga descoberta) /R$ 3 (vaga coberta)\\r\
        \\r\
        Os clientes que permanecem por 7 ou mais dias conosco, fazem jus a promoção de semana, pagando uma diária de *R$ 16,36* para vaga coberta e *R$ 14* para descoberta.\\r\
        \\r\
        Faça uma simulação do provável valor da sua estadia, colocando a hora de entrada e de saída estimada no site: https://estacionamentopatioconfins.com.br/wp/reservas/.\\r\
        Estamos muito próximos ao aeroporto, cerca de 4 km. Visite nosso site e veja: https://estacionamentopatioconfins.com.br/estacionamento-proximo-ao-aeroporto-de-confins/\\r\
        \\r\
        Venha nos conhecer, temos translado gratuito (ida e volta) 24 horas para/de o aeroporto, estacionamento com segurança  e seguro.""",

        '2': f"""Estamos cerca de 4 minutos, ou 3 km, do Aeroporto de Confins.\\r\
            \\r\
        A maneira mais fácil de chegar ao nosso estacionamento é procurando por “Estacionamento Pátio Confins” no Waze ou Google Maps.\\r\
            \\r\
        Clique aqui para o passo a passo detalhado: https://estacionamentopatioconfins.com.br/wp/estacionamento-proximo-ao-aeroporto-de-confins/""",
        '3': "Faça sua reserva gratuita em três passos. Clique no link a seguir: https://estacionamentopatioconfins.com.br/wp/reservas/",
        '4': f"""Chame sua van, tire suas dúvidas, entre em contato com um dos seguintes números:\\r\
        \\r\
        (31) 3-665-7777\\r\
        \\r\
        (31) 9-8473-1607\\r\
        \\r\
        (31) 9-8478-6316\\r\
        \\r\
        sac@estacionamentopatioconfins.com.br""",
        '5': "Nossos transportes, são gratuitos, funcionam 24 horas e saem imediatamente após a chegada dos nossos clientes. Recomendamos chegar em nosso estacionamento 15 minutos antes do horário pretendido de estar no aeroporto (diferente de horário do voo), pois nossos veículos podem estar ocupados no momento da sua chegada. No seu retorno, você nos liga e te buscamos na sua área de desembarque. O trajeto do estacionamento ao aeroporto não leva mais que 5 minutos.",
        '6':f"""Aceitamos pagamento antecipado por pix. Funciona assim:\\r\
            \\r\
            1. *Faça o pix no valor informado para o CNPJ*\\r\
            *_25.042.876/0001-21_*\\r\
            \\r\
            2. *Envie o comprovante para esse número*\\r\
            \\r\
            Pronto!!\\r\
            \\r\
            \\r\
            ```Caso o carro``` *saia antes de 48 horas* ```do término da estadia, devolveremos proporcionalmente o valor pago.```\\r\
            \\r\
            ```Caso você permaneça``` *além de 24 horas* ```do término da estadia, será cobrado o período adicional.```""",
        'sim': f"""Estamos cerca de 4 minutos, ou 3 km, do Aeroporto de Confins.\\r\
            \\r\
        A maneira mais fácil de chegar ao nosso estacionamento é procurando por “Estacionamento Pátio Confins” no Waze ou Google Maps.\\r\
            \\r\
        Clique aqui para o passo a passo detalhado: https://estacionamentopatioconfins.com.br/wp/estacionamento-proximo-ao-aeroporto-de-confins/""",
        'não': f"""Caro cliente, \\r\
        \\r\
        \\r\
        \\r\
        Peço gentilmente que nos informe o motivo do seu não comparecimento, para que possamos entender melhor a necessidade dos nossos clientes.\\r\
        Sua colaboração é muito importante, desde já, muito obrigado pela participação.\\r\
        \\r\
        \\r\
        \\r\
        Atenciosamente,""",
        'nao': f"""Caro cliente, \\r\
        \\r\
        \\r\
        \\r\
        Peço gentilmente que nos informe o motivo do seu não comparecimento, para que possamos entender melhor a necessidade dos nossos clientes.\\r\
        Sua colaboração é muito importante, desde já, muito obrigado pela participação.\\r\
        \\r\
        \\r\
        \\r\
        Atenciosamente,""",
        'só preciso passar um recado importante:': """Este número só funciona em horário comercial e na maior parte do tempo é respondido por um bot, assim utilize os números que vou te passar para chamar sua van no momento do desembarque ou para atendimento imediato.\\r\
        \\r\
        (31) 3-665-7777\\r\
        \\r\
        (31) 9-8473-1607\\r\
        \\r\
        (31) 9-8478-6316""",
        'em relação aos pagamentos': f"Aceitamos todos os principais cartões de crédito, débito e dinheiro. O pagamento é feito somente no final do período, pois para cobrança é levada em consideração sua efetiva hora de saída. Os valores a pagar mostrados no momento da sua reserva são estimados.",
        'eu preciso que você me informe:': f"""Seu nome,\\r\
    Seu e-mail,\\r\
    Modelo do veículo, \\r\
    Placa do veículo.""",
        'peço gentilmente que': f"""Após a retirada das malas, avise sua chegada nos seguintes números.  Esse número é para reservas. Não falo do estacionamento.\\r\
        \\r\
        Entre em contato com um dos seguintes números:\\r\
        \\r\
        (31) 3-665-7777\\r\
        \\r\
        (31) 9-8473-1607\\r\
        \\r\
        (31) 9-8478-6316""",
        '13': f"""oi \n
        tudo bem \n
        """,
        '14': """oi 
        tudo bem 
        """,
        '15': f"""oi 
        tudo bem 
        """,
        '16': r"""oi 
        tudo bem 
        """
    }
    return switcher.get(argument, "")





if __name__ == "__main__":

    driver = webdriver.Chrome(executable_path=r'chromedriver.exe')

    driver.get("https://web.whatsapp.com/")
    el = WebDriverWait(driver, timeout=60).until(lambda d: d.find_element(By.CSS_SELECTOR, '#pane-side'))
    passagem = True
    ultima_mensagem = ""
    print("Whatsapp web iniciado...")
    while True:
       
        time.sleep(3)
  
        try:
            #são feitas  2 verifiicações: 1) se há mensagens novas no painel principal e 2) se já notificações no painel esquerdo
            #1
            if not (passagem):
                msg = driver.find_element(By.CSS_SELECTOR, '#main div[aria-label="Lista de mensagens. Pressione a seta para direita em uma mensagem para abrir o menu da mensagem."]')
                mensagens = msg.find_elements(By.CSS_SELECTOR, 'span.copyable-text')

                quantas_mensagens = len(mensagens)
                if ultima_mensagem != mensagens[quantas_mensagens-1].text: 
                    print(mensagens[quantas_mensagens-1].text)
                    resposta(driver, mensagens[quantas_mensagens-1].text)
                   
            #2
            

            #notificação de nova mensagem e clica
            driver.find_element(By.CSS_SELECTOR, '._1pJ9J').click()
            #lista todas as mensagens da nova notificação e procura pela última
            msg = driver.find_element(By.CSS_SELECTOR, '#main div[aria-label="Lista de mensagens. Pressione a seta para direita em uma mensagem para abrir o menu da mensagem."]')
            mensagens = msg.find_elements(By.CSS_SELECTOR, 'span.copyable-text')

            quantas_mensagens = len(mensagens)
            if ultima_mensagem != mensagens[quantas_mensagens-1].text: 
                print(mensagens[quantas_mensagens-1].text)
                resposta(driver, mensagens[quantas_mensagens-1].text)

          

            passagem = False
            ultima_mensagem = mensagens[quantas_mensagens-1].text

        except:
            #mensagens antigas
            #driver.find_element(By.CSS_SELECTOR, '._2aBzC')
            pass
    



