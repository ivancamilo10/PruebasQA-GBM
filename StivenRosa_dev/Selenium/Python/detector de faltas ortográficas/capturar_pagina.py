from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


def capturar_pagina_completa(navegador, nombre_archivo="captura_pagina.png"):
    """
    Recibe un navegador (driver) y guarda una captura de pantalla completa en la carpeta 'screenshots'.
    """
    # Crear la carpeta 'screenshots' si no existe
    carpeta = "screenshots"
    os.makedirs(carpeta, exist_ok=True)

    # Ruta final del archivo dentro de la carpeta
    ruta_archivo = os.path.join(carpeta, nombre_archivo)

    # Esperar un momento para que termine de cargar
    time.sleep(2)

    # Obtener ancho y alto total de la página
    ancho_total = navegador.execute_script("return document.body.scrollWidth")
    alto_total = navegador.execute_script("return document.body.scrollHeight")

    # Ajustar ventana al tamaño de la página
    navegador.set_window_size(ancho_total, alto_total)

    # Guardar captura
    navegador.save_screenshot(ruta_archivo)



