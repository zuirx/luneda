from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui as p
import pygetwindow as gw
import time

chromedriver_path = "chrome\\chromedriver.exe"
chrome_path = "chrome\\Chromium\\Application\\chrome.exe"
profile_path = "profile"

options = Options()
options.binary_location = chrome_path
options.add_argument("--user-data-dir=./profile")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://web.whatsapp.com")

time.sleep(6)

# VERIFICAR SE HÁ MENSAGEM NÃO LIDA
#   CLICAR NO MAIS ANTIGO (SE POSSÍVEL)
#   OU SÓ VERIFICAR MENSAGEM COM CONTATO PERMITIDO
# SE TIVER, ABRIR MENSAGEM, VERIFICAR ULTIMAS MENSAGENS
# VERIFICAR SE A MENSAGEM JA FOI LIDA (MANTER UM BANCO)
# INTERPRETAR COMANDO, SE NÃO ENTENDER, MANDAR MENSAGEM DE ERRO (SEJA POR NAO INTERPRETAR OU NAO TER IMP. INSTALADA [REGISTRAR])
# COMANDO: Ricoh 3710SF, 1234561441, (Rede <informar ip caso tiver>, USB)

# SE DER CERTO, ENVIAR PARA INTERMEDIÁRIO


# def verificar_mensagem()

while True:

    
    try:

        mensagem_nao_lida = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/div[3]/div/div[3]/div/div/div/div[1]/div/div/div/div[2]/div[2]/div[2]/span[1]/div/span')))
        mensagem_nao_lida.click()

        if mensagem_nao_lida:
            ola = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div[4]//span[contains(text(), "oi")] | /html/body/div[1]/div/div/div[2]/div[4]//p[contains(text(), "oi")]')))

            if ola:
                window = gw.getWindowsWithTitle("WhatsApp - Chromium")[0]  
                window.activate()
                p.sleep(0.2); p.write("Olá")
                p.sleep(0.2); p.press("enter")

        time.sleep(1)

    except Exception as e:
        print("Element not found:", str(e))
        # break
        time.sleep(3)
