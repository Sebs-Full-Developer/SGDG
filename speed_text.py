import time
import sys
import threading

def imprimir_letra_por_letra(texto, delay=0.02):
    """Imprime un texto letra por letra con un retraso especificado."""
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(delay)

def input_animado(prompt, delay=0.1):
    """Imprime el prompt letra por letra y espera la entrada del usuario."""
    imprimir_letra_por_letra(prompt, delay)
    return input()  # Captura la entrada del usuario

