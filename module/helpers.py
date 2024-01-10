import time
import re
from random import uniform
def nueva_lista(lista = []):
    nueva_lista = []
    aux = 0
    for i, elem in enumerate(lista):
        if elem == 0:
            if i > 0:
                nueva_lista.append(lista[i-1])
        else:
            aux = elem
    nueva_lista.append(aux)
    return nueva_lista
def extraer_numeros(oracion):
    numero = re.findall(r'\d+', oracion)
    
    return int(numero[0]) 
 
def pausa(min=0, max=0.20):

    time.sleep(uniform(min,max))

def tecleo_lento(elemento, texto):

    for letra in texto:
        pausa()
        elemento.send_keys(letra)