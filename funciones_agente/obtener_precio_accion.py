import re
import yfinance as yf
from utils.sanitizar import sanitizar


COMPANY_TICKERS = {
    "microsoft": "MSFT",
    "apple": "AAPL",
    "google": "GOOGL",
    "alphabet": "GOOGL",
    "amazon": "AMZN",
    "tesla": "TSLA",
    "meta": "META",
    "facebook": "META",
    "netflix": "NFLX",
    "nvidia": "NVDA",
    "apple inc": "AAPL",
    "microsoft corp": "MSFT",
    "tesla motors": "TSLA"
}


def obtener_precio_accion(driver, user_input):
    """Busca y retorna el precio actual de una acción usando yfinance."""
    # Limpia la frase y la separa en palabras
    texto = (sanitizar(user_input) or "").lower()
    palabras = re.findall(r"\w+", texto)

    # Busca si alguna empresa del diccionario aparece en la frase
    ticker = None
    for nombre, simbolo in COMPANY_TICKERS.items():
        if nombre in texto:
            ticker = simbolo
            break

    # Si no encontró empresa, usa la última palabra como ticker (ej. "precio TSLA")
    if not ticker and palabras:
        ticker = palabras[-1].upper()

    if not ticker:
        return "¿De qué empresa? Ejemplo: precio de apple"

    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="5d")

        if not data.empty:
            price = data["Close"].iloc[-1]
            return f"{ticker}: ${price:.2f} USD"
        else:
            return f"No encontré datos para '{ticker}'. Revisa el nombre o el símbolo."

    except Exception as e:
        return f"Error al consultar el precio de la acción: {e}"