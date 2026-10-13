# Semana 2 — API y análisis de datos meteorológicos

Esta práctica consulta Open-Meteo para obtener el pronóstico de Huancayo y procesa los datos con Python y Pandas.

## Archivos principales

- `clima.py`: consulta la API y guarda los datos originales en JSON y CSV.
- `analisis.py`: calcula la amplitud térmica, clasifica temperaturas y genera resúmenes.
- `pronostico_huancayo.json` y `pronostico_huancayo.csv`: datos obtenidos.
- `pronostico_huancayo_procesado.csv` y `resumen_por_categoria.csv`: resultados del análisis.

## Ejecución

Abre una terminal en la raíz del repositorio y ejecuta:

```bash
cd semana02
python clima.py
python analisis.py
```

Ejecuta primero `clima.py` para generar los datos que necesita `analisis.py`. La consulta requiere conexión a internet. Ejecutar el análisis desde esta carpeta permite que las rutas relativas a los CSV funcionen correctamente.
