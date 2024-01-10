import os
import sys
import time
import pickle
import tempfile
import re
# modulos propios
from module.config import *
from module.colores import *
from module.cursor_arriba import *
 
from random import uniform
# modulos de terceros
import threading
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from module.selenium_indetectable import iniciar_webdriver
import pandas as pd
def extraer_numeros(oracion):
    numero = re.findall(r'\d+', oracion)
    
    return int(numero[0]) 
def pausa(min=0, max=0.4):

    time.sleep(uniform(min,max))

class Prueba():
    def __init__(self, producto) -> None:
        self.titulo,self.descripcion,self.categoria, self.precio = producto
        self.grupos = [1,2,3,4,5]
        self.mostrar_datos()

    def mostrar_datos(self):
            print(self.titulo)
            print(self.descripcion)
            print(self.categoria)
            print(self.precio)

class Hijo(Prueba):
    def __init__(self, producto) -> None:
          super().__init__(producto)


    def modificar(self):
          self.grupos.append(2)
          print(self.grupos)
if __name__ == "__main__":
    maquillaje = pd.read_excel('./db/Maquillaje.xlsx',sheet_name="Hoja1")
    print(Hijo(maquillaje.values[0]).modificar())
 

