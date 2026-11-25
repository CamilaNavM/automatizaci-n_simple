# Módulo para consultar precios de acciones en tiempo real usando yfinance
import re 
import yfinance as yf
from utils.sanitizar import sanitizar

# Diccionario para mapear nombres comunes de empresas a sus Tickers de bolsa correspondientes
COMPANY_TICKERS = {
    "microsoft": "MSFT",
    "apple": "AAPL",
    "google": "GOOGL",
    "alphabet": "GOOGL",
    "amazon": "AMZN",
    "meta": "META",
    "facebook": "META",
    "netflix": "NFLX",
    "nvidia": "NVDA",
    "apple inc": "AAPL",
    "microsoft corp": "MSFT",

}

def obtener_precio_accion(driver, user_input):
    """
    Busca y retorna el precio actual de una acción utilizando la librería yfinance.
    
    Argumentos:
        driver: Instancia de Selenium WebDriver (opcional).
        user_input: Input del usuario que contiene el nombre de la empresa.
    
    Retorna:
        El precio formateado como cadena o un mensaje explicativo si no se encuentra.
    """
        # Limpia la frase y la separa en palabras
    texto = sanitizar(user_input).lower()
    palabras = re.findall(r"\w+", texto)

    ticker = None
    for nombre, simbolo in COMPANY_TICKERS.items():
        if nombre in texto:
            ticker = simbolo
            break

    if not ticker and palabras:
        ticker = palabras[-1].upper()

    if not ticker:
        return "¿De qué empresa? Ejemplo: precio de apple"