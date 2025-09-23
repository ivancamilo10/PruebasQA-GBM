import os
import sys
import logging
import argparse
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def get_driver(chromedriver_path, use_brave=False):
    options = Options()
    if use_brave:
        # Update this path to the actual Brave browser executable, not chromedriver.exe
        options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
    service = Service(executable_path=chromedriver_path)
    return webdriver.Chrome(service=service, options=options)

def accept_cookies(driver, wait):
    try:
        aceptar = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'Aceptar')]")))
        aceptar.click()
        logging.info("Cookies aceptadas.")
    except Exception:
        logging.info("No apareció el botón de cookies.")

def search_product(driver, wait, product):
    buscador = wait.until(EC.presence_of_element_located((By.NAME, "as_word")))
    buscador.clear()
    buscador.send_keys(product)
    buscador.submit()
    logging.info(f"Búsqueda realizada: {product}")

def scrape_results(driver, wait, max_results=10):
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "li.ui-search-layout__item")))
    items = driver.find_elements(By.CSS_SELECTOR, "li.ui-search-layout__item")[:max_results]
    results = []
    for item in items:
        try:
            title = item.find_element(By.CSS_SELECTOR, "h2.ui-search-item__title").text
            price = item.find_element(By.CSS_SELECTOR, "span.price-tag-fraction").text
            results.append({'title': title, 'price': price})
        except Exception:
            continue
    return results

def save_to_csv(results, filename="resultados.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'price'])
        writer.writeheader()
        writer.writerows(results)
    logging.info(f"Resultados guardados en {filename}")

def main():
    parser = argparse.ArgumentParser(description="Web Scraping MercadoLibre")
    parser.add_argument('--brave', action='store_true', help='Usar Brave en vez de Chrome')
    parser.add_argument('--product', type=str, default='laptop', help='Producto a buscar')
    parser.add_argument('--chromedriver', type=str, default=r"C:\EJERCICIOS DE PRUEBAS\PROGRAMAS\chromedriver.exe", help='Ruta a chromedriver.exe')
    args = parser.parse_args()

    chromedriver_path = args.chromedriver
    if not os.path.exists(chromedriver_path):
        logging.error(f"No se encontró chromedriver en {chromedriver_path}")
        sys.exit(1)

    driver = get_driver(chromedriver_path, use_brave=args.brave)
    wait = WebDriverWait(driver, 15)
    try:
        driver.get("https://www.mercadolibre.com.co/")
        accept_cookies(driver, wait)
        search_product(driver, wait, args.product)
        results = scrape_results(driver, wait)
        if results:
            save_to_csv(results)
        else:
            logging.warning("No se encontraron resultados.")
    except Exception as e:
        logging.error(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
