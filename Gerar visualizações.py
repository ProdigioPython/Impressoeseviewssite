from selenium import webdriver
import time

# Inicializando o navegador
options = webdriver.ChromeOptions()
options.add_argument("--disable-features=Bluetooth")
driver = webdriver.Chrome(chrome_options=options)

# Acessando o site
driver.get("https://noticiariovipbrasil.blogspot.com/")

# Define a velocidade de rolagem
scroll_speed = 2

while True:
    # Rola a página lentamente para baixo
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_speed)

    # Rola a página lentamente para cima
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(scroll_speed)

    # Atualiza a página
    driver.refresh()
    