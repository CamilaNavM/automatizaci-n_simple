import re
import sys
# Importamos las funciones de lógica de negocio desde nuestro paquete de funciones
from funciones_agente.obtener_precio_accion import obtener_precio_accion
from funciones_agente.obtener_clima import obtener_clima
# Importamos utilidades para limpiar el texto del usuario
from utils.sanitizar import sanitizar

def procesar_input(user_input):
    if "clima" in user_input or "temperatura" in user_input:
        return "clima"
    elif "precio" in user_input or "accion" in user_input or "valor" in user_input:
        return "precio"
    return None

print("Hola, soy tu asistente virtual. En que puedo ayudarte?")
while True:
    user_input = sanitizar(input("---> "))
    funcion_agente = procesar_input(user_input)
    print(funcion_agente)