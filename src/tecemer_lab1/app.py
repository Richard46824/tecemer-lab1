import requests

try:
    respuesta = requests.get(
        "https://official-joke-api.appspot.com/random_joke", timeout=5
    )

    respuesta.raise_for_status()

    datos = respuesta.json()

    print(datos["setup"])
    print(datos["punchline"])

except requests.exceptions.RequestException as error:
    print("Error al conectar con la API:", error)

except (KeyError, ValueError):
    print("Error: la respuesta de la API no tiene el formato esperado.")
