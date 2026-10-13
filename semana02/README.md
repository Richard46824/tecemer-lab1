# Semana 2 — Datos del clima

En esta práctica trabajé con datos meteorológicos de Huancayo. Primero consulté la API de Open-Meteo y guardé la información; después usé Python y Pandas para revisar y resumir los datos.

## Archivos que utilicé

- `clima.py`: consulta la API y guarda la información en archivos JSON y CSV.
- `analisis.py`: lee los datos y realiza cálculos y resúmenes de las temperaturas.
- `pronostico_huancayo.json` y `pronostico_huancayo.csv`: guardan los datos obtenidos.
- `pronostico_huancayo_procesado.csv` y `resumen_por_categoria.csv`: contienen resultados del análisis.

## Cómo ejecutar

Abre una terminal en la carpeta principal y entra a esta semana:

```bash
cd semana02
python clima.py
python analisis.py
```

Ejecuta primero `clima.py`, porque genera los archivos que necesita `analisis.py`. Para consultar la API necesitas conexión a internet. Ejecuta los comandos desde esta carpeta para que funcionen las rutas de los archivos.
