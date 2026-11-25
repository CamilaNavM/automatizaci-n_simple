import re
import sys
# Importamos las funciones de lógica de negocio desde nuestro paquete de funciones
from funciones_agente.obtener_precio_accion import obtener_precio_accion
from funciones_agente.obtener_clima import obtener_clima
# Importamos utilidades para limpiar el texto del usuario
from utils.sanitizar import sanitizar

def procesar_input(user_input):
    if "clima" in user_input or "temperatura" in user_input:
        return obtener_clima
    elif "precio" in user_input or "accion" in user_input or "valor" in user_input:
        return obtener_precio_accion
    return None

driver = None   
print("Hola, soy tu asistente virtual. En que puedo ayudarte? (escribe 'salir' o 'q' para terminar)")
while True:
    user_input = input("---> ").strip().lower()
    if user_input.lower() in ("salir", "exit", "adios", "q"):
        print("¡Hasta luego!")       
        break
    funcion_agente = procesar_input(user_input)
    if funcion_agente is None:
        print("No entendi tu solicitud. Intenta nuevamente")
    else:
        respuesta = funcion_agente(driver, user_input)
        print(f">>> {respuesta}")