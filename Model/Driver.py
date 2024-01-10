import os
import sys
import time
import pickle
import re
from random import uniform
import threading
# modulos de terceros
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# modulos propios
from module.helpers import *
from module.colores import * 
from module.config import *
from module.colores import *
from module.cursor_arriba import *
from module.selenium_indetectable import iniciar_webdriver
 
class Driver():
    def __init__(self, usuario, headless=False) -> None:
        self.carpeta = 'cookies'
        self.COOKIES_FILE = f"./cookies/{usuario}.cookies"
        print(f'{azul}Iniciando webdriver{gris_claro}')
        self.driver = iniciar_webdriver(headless=headless)
        self.lock = threading.Lock()
        self.wait = WebDriverWait(self.driver, 30)


    def scrolling_into_container(self,y,aux,container):
        while True:
            current_scroll = aux
            if current_scroll > y:
                break
      
                # Desplaza la página hacia abajo en la cantidad definida por current_scroll
            for i in range(100):
                if current_scroll > y:
                    break

                self.driver.execute_script(f"arguments[0].scrollTo(0, {current_scroll})", container)
                pausa(0,0.01)
                current_scroll += uniform(13.04,14.70)

                # si current_scroll es mayo a height se rompe el bucle

            pausa(0.4,0.5)
            tiempo = uniform(0.3,1.7)

            # Espera un momento para que se cargue más contenido dentro del div de comentarios
            self.driver.implicitly_wait(tiempo) # Ajusta el tiempo según sea necesario
            aux = current_scroll

    def scrolling_into_view(self,y,aux):
            while True:
                current_scroll = aux
                if current_scroll > y:
                    break
                # Desplaza la página hacia abajo en la cantidad definida por current_scroll
                while True:
                    if current_scroll > y:
                        break
                    for i in range(100):
                        if current_scroll > y:
                            break
                        self.driver.execute_script(f"window.scrollTo(0, {current_scroll})")
                        pausa(0,0.01)
                        current_scroll += uniform(13.04,14.70)
    
                pausa(0.4,0.5)
                tiempo = uniform(0.3,1.7)

                # Espera un momento para que se cargue más contenido dentro del div de comentarios
                self.driver.implicitly_wait(tiempo) # Ajusta el tiempo según sea necesario
                aux = current_scroll
    def cerrar(self):
        print(f"\33[K{azul}Saliendo...{gris_claro}")
        self.driver.quit()