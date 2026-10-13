# Semana 2 — API y análisis de datos meteorológicos

Esta práctica obtiene el pronóstico de Huancayo desde la API pública Open-Meteo y lo procesa con Python y Pandas.

## Archivos principales

- `clima.py`: solicita el pronóstico y genera los archivos de datos.
- `pronostico_huancayo.json`: respuesta almacenada en JSON.
- `pronostico_huancayo.csv`: datos meteorológicos en CSV.
- `analisis.py`: convierte fechas, calcula amplitud térmica, clasifica temperaturas y resume los resultados.
- `pronostico_huancayo_procesado.csv`: datos procesados.
- `resumen_por_categoria.csv`: resumen agrupado por categoría.

## Ejecución

Desde la raíz del repositorio:

```bash
python semana02/clima.py
python semana02/analisis.py
```

La consulta requiere conexión a internet. Ejecutar `clima.py` vuelve a generar los archivos de pronóstico; después puede ejecutarse el análisis.

## Flujo de trabajo

1. Consultar la API Open-Meteo.
2. Guardar los datos originales en JSON y CSV.
3. Procesar las fechas y derivar variables.
4. Clasificar temperaturas y resumir los resultados.
