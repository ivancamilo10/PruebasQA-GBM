from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, TimeoutException
import time


from ElementData import ElementData
# from detector import detectar_falta_ortografica
from revisar_ortografia import revisar_ortografia as detectar_falta_ortografica

def initialize_driver(URL='https://www.google.com'):
    driver = webdriver.Chrome()
    driver.get(URL)
    return driver






def extract_elements_info(driver):
    etiquetas = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 
                 'li', 'span', 'a', 'strong', 'em', 
                 'blockquote', 'label', 'button', 'td', 'th']
    
    elementos_info = []

    for tag in etiquetas:
        elementos = driver.find_elements(By.TAG_NAME, tag)
        for el in elementos:
            if el.text.strip():
                data = ElementData(
                    tag=el.tag_name,
                    text=el.text.strip(),
                    element_id=el.get_attribute("id"),
                    element_class=el.get_attribute("class"),
                    location=el.location,
                    displayed=el.is_displayed(),
                    is_active=el.is_enabled()
                )
                elementos_info.append(data)

    return elementos_info






def main():
    try:
        elementos_faltas = []
        elementos_bien = []
        driver = initialize_driver('https://tecnomarketrd.com/')
        time.sleep(1)
        elementos_info = extract_elements_info(driver)

        for elemento in elementos_info:
            # print(detectar_falta_ortografica(elemento.text))
            if detectar_falta_ortografica(elemento.text)[0] == 1:
                elementos_faltas.append(elemento)
            else:
                elementos_bien.append(elemento)

        print(f"Elementos con faltas ortográficas: {len(elementos_faltas)}")
        print(f"Elementos sin faltas ortográficas: {len(elementos_bien)}")










    except (WebDriverException, TimeoutException) as e:
        print(f"❌ Ocurrió un error al abrir la página o con el driver: {e}")
    finally:
        try:
            driver.quit()
        except:
            pass




if __name__ == '__main__':
    main()