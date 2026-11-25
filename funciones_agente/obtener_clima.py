import re
import requests


PALABRAS_IGNORAR = {
    "clima", "temperatura", "en", "de", "del", "la", "el", "es",
    "cual", "cuál", "que", "qué", "hace", "hay", "hoy", "actual", "dime",
}

def obtener_clima(driver, user_input):
    """Obtiene la temperatura actual de una ciudad usando wttr.in."""
    palabras = re.findall(r"\w+", user_input.lower())
    ciudad = " ".join(p for p in palabras if p not in PALABRAS_IGNORAR)

    if not ciudad:
        return "¿De qué ciudad? Ejemplo: clima en Monterrey"

    try:
        response = requests.get(f"https://wttr.in/{ciudad.replace(' ', '+')}?format=%t", timeout=10)
        response.encoding = "utf-8"
        if response.status_code == 200:
            return f"La temperatura en {ciudad.title()} es {response.text.strip()}"
        else:
            return "No se pudo obtener el clima para esa ubicación."
    except Exception as e:
        return f"Error de red al obtener el clima: {e}"