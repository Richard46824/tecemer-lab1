# Tecemer Lab 1

Proyecto de práctica desarrollado en Python para el curso de Tecnologías Emergentes. En este proyecto se trabaja la estructura `src-layout`, la instalación editable y buenas prácticas de código.

## Instalación

### 1. Crear el entorno virtual

Desde la carpeta principal del proyecto, ejecuta:

```bash
python -m venv .venv
```

### 2. Activar el entorno virtual

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Instalar el proyecto en modo editable

Con el entorno virtual activado:

```bash
pip install -e .
```

## Ejemplo de uso

Para ejecutar la aplicación, desde la carpeta principal del proyecto utiliza:

```bash
python src/tecemer_lab1/app.py
```

La aplicación se ejecutará y mostrará el resultado directamente en la terminal.

## Estructura del proyecto

```text
tecemer-lab1/
├── src/
│   └── tecemer_lab1/
│       ├── __init__.py
│       └── app.py
├── .venv/
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Autor

Richard torres areche46824

## Curso

Tecnologías Emergentes — IS046B

## Flujo de datos — Semana 2

### Fuente

Los datos meteorológicos se obtienen mediante la API Open-Meteo para la ciudad de Huancayo.

### Transformación

Los datos se almacenan en formato JSON y CSV. Luego se procesan utilizando Pandas para convertir las fechas, calcular la amplitud térmica, identificar los días lluviosos y clasificar las temperaturas en las categorías "cálido" y "templado".

### Salida

Se generan los siguientes archivos:

- `pronostico_huancayo.json`
- `pronostico_huancayo.csv`
- `pronostico_huancayo_procesado.csv`
- `resumen_por_categoria.csv`

## Cierre de la Unidad I — Semana 3

Herramienta de automatización: `organizador.py` clasifica y mueve archivos de una carpeta en subcarpetas por tipo (Documentos, Imagenes, Videos, Comprimidos, Otros), con modo de simulacion (`--dry-run`) mediante `argparse`.

Uso:

```bash
python organizador.py <carpeta> [--dry-run]
```

## Cierre de la Unidad I — Semana 3

Herramienta de automatización: `organizador.py` clasifica y mueve archivos
de una carpeta en subcarpetas por tipo (Documentos, Imagenes, Videos,
Comprimidos, Otros), con modo de simulación (`--dry-run`) mediante argparse.

Uso:

```text
python organizador.py <carpeta> [--dry-run]
```

Pruebas: `test_organizador.py` cubre clasificación, movimiento real y modo
simulación, usando la fixture `tmp_path` de pytest para no afectar el
sistema de archivos real.

Ejecutar con:

```text
pytest -v
```


## Semana 4 — Clasificación de lluvia

En esta semana se prepararon datos meteorológicos de Huancayo y se entrenó un modelo de aprendizaje automático para clasificar días lluviosos. Se trabajó con una red neuronal MLP y se compararon sus resultados con una regresión logística. También se guardaron el modelo y el escalador para realizar predicciones.

## Semana 5 — Redes neuronales

Se desarrollaron notebooks prácticos sobre preprocesamiento de datos, perceptrón y MLP, redes convolucionales (CNN), redes recurrentes (RNN), procesamiento de lenguaje natural y evaluación de modelos. Los ejercicios se prepararon para ejecutarse en Google Colab, revisando los resultados y las métricas de cada práctica.
