# Laboratorio Tecemer 1

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
├── semana01/
├── semana02/
├── semana03/
├── semana04/
├── semana05/
├── src/
│   └── tecemer_lab1/
│       ├── __init__.py
│       └── app.py
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Autor

Richard Torres Areche46824

## Curso

Tecnologías Emergentes — IS046B

---

# Documentación de las prácticas

## Semana 1 — Fundamentos y configuración

Esta carpeta reúne ejercicios introductorios y material asociado a la configuración del proyecto.

### Contenido

- `numpy_demo.py`: demostración básica de operaciones con NumPy.
- `mini_reto.py`: estadísticas descriptivas de un arreglo de temperaturas.
- La estructura principal del paquete se encuentra en `src/tecemer_lab1/`.
- En esta semana también se trabajó la configuración inicial, el manejo de errores, el formato PEP 8 y la estructura `src-layout`.

### Ejecutar los ejercicios

Desde la raíz del repositorio:

```bash
python semana01/numpy_demo.py
python semana01/mini_reto.py
```

## Semana 2 — API y análisis de datos meteorológicos

Esta práctica consulta Open-Meteo para obtener el pronóstico de Huancayo y procesa los datos con Python y Pandas.

### Archivos principales

- `clima.py`: consulta la API y guarda los datos originales en JSON y CSV.
- `analisis.py`: calcula la amplitud térmica, clasifica temperaturas y genera resúmenes.
- `pronostico_huancayo.json` y `pronostico_huancayo.csv`: datos obtenidos.
- `pronostico_huancayo_procesado.csv` y `resumen_por_categoria.csv`: resultados del análisis.

### Ejecución

Abre una terminal en la raíz del repositorio y ejecuta:

```bash
cd semana02
python clima.py
python analisis.py
```

Ejecuta primero `clima.py` para generar los datos que necesita `analisis.py`. La consulta requiere conexión a internet. Ejecutar el análisis desde esta carpeta permite que las rutas relativas a los CSV funcionen correctamente.

### Flujo de datos

**Fuente:** los datos meteorológicos se obtienen mediante la API Open-Meteo para la ciudad de Huancayo.

**Transformación:** los datos se guardan en JSON y CSV. Luego se procesan con Pandas para convertir fechas, calcular la amplitud térmica, identificar días lluviosos y clasificar las temperaturas en categorías como "cálido" y "templado".

**Salida:** se generan los archivos `pronostico_huancayo.json`, `pronostico_huancayo.csv`, `pronostico_huancayo_procesado.csv` y `resumen_por_categoria.csv`.

## Semana 3 — Automatización y pruebas

Esta práctica desarrolla un organizador que clasifica archivos por extensión y puede simular los movimientos antes de ejecutarlos.

### Archivos

- `organizador.py`: lógica de clasificación y movimiento de archivos.
- `test_organizador.py`: pruebas automatizadas con pytest.

### Uso

Desde la raíz del repositorio, primero simula los cambios:

```bash
python semana03/organizador.py "RUTA_A_LA_CARPETA" --dry-run
```

Si el resultado es correcto, ejecuta sin `--dry-run` para mover los archivos:

```bash
python semana03/organizador.py "RUTA_A_LA_CARPETA"
```

Reemplaza `RUTA_A_LA_CARPETA` por una carpeta de prueba. Se recomienda revisar la simulación antes de mover archivos.

### Ejecutar pruebas

```bash
pytest semana03/test_organizador.py
```

## Semana 4 — Laboratorio de redes neuronales: clasificación de lluvia

En este laboratorio se construyó un clasificador de lluvia para datos de Huancayo utilizando una red neuronal perceptrón multicapa (MLP) con Keras y TensorFlow.

El trabajo comprende la preparación de los datos, el entrenamiento de una red neuronal sobre datos sintéticos y la construcción de un clasificador binario para determinar si un día será lluvioso.

### Actividades realizadas

- Preparación y limpieza del dataset climático.
- Creación de la variable objetivo `dia_lluvioso`.
- Escalado de variables mediante `StandardScaler`.
- División de los datos en conjuntos de entrenamiento y prueba.
- Construcción, entrenamiento y evaluación de un MLP con Keras.
- Comparación con una regresión logística de referencia.
- Generación de curvas de entrenamiento y guardado del modelo en formato `.keras`.
- Creación de un script de predicción y pruebas automatizadas con pytest.

### Archivos principales

- `ampliar_dataset.py`: amplía el dataset climático.
- `preparar_dataset.py`: prepara y escala los datos.
- `perceptron_sintetico.py`: entrena un MLP con datos sintéticos.
- `clasificador_lluvia.py`: entrena y evalúa el clasificador.
- `predecir.py`: realiza predicciones con el modelo entrenado.
- `dataset_preparado.npz`: datos preparados para entrenamiento.
- `escalador_lluvia.joblib`: escalador ajustado con el conjunto de entrenamiento y reutilizado en predicciones.
- `modelo_lluvia.keras`: modelo neuronal entrenado.
- `curvas_entrenamiento_lluvia.png` y `curvas_entrenamiento_sintetico.png`: curvas generadas durante el entrenamiento.
- `tests/test_preparacion.py`: pruebas automatizadas.

### Dependencias adicionales

Además de las dependencias generales del repositorio, esta semana se utilizan scikit-learn, TensorFlow y Matplotlib:

```bash
python -m pip install scikit-learn tensorflow matplotlib
```

### Ejecución y pruebas

Abre la terminal dentro de la carpeta de esta semana:

```bash
cd semana04
python preparar_dataset.py
python clasificador_lluvia.py
python predecir.py
python -m pytest tests/ -v
```

Ejecuta los pasos en ese orden. `predecir.py` requiere que existan `modelo_lluvia.keras` y `escalador_lluvia.joblib`, generados por los pasos anteriores.

## Semana 5 — Ejercicios de redes neuronales

Esta carpeta reúne notebooks prácticos de aprendizaje automático y redes neuronales. Están diseñados principalmente para ejecutarse en **Google Colab** o Jupyter Notebook.

### Orden de los ejercicios

| Orden | Notebook | Tema principal |
|---|---|---|
| 1 | [Ejercicio 01 — Preprocesamiento y exploración](semana05/Ejercicio_01_Preprocesamiento_Exploracion_Datos.ipynb) | Valores faltantes, visualización, codificación y escalado |
| 2 | [Ejercicio 02 — Perceptrón y MLP](semana05/Ejercicio_02_Perceptron_MLP.ipynb) | AND, XOR, funciones de activación y clasificación no lineal |
| 3 | [Ejercicio 03a — CNN para clasificación de imágenes](semana05/Ejercicio_03a_CNN_Clasificacion_Imagenes_completado.ipynb) | Fashion-MNIST, convoluciones y matriz de confusión |
| 4 | [Ejercicio 03b — CNN para detección de objetos](semana05/Ejercicio_03b_CNN_Deteccion_Objetos_completado.ipynb) | Cajas delimitadoras y Faster R-CNN |
| 5 | [Ejercicio 04a — RNN y análisis de sentimientos](semana05/Ejercicio_04a_RNN_NLP_Analisis_Sentimientos_completado.ipynb) | Clasificación de reseñas de texto |
| 6 | [Ejercicio 04b — RNN para series temporales](semana05/Ejercicio_04b_RNN_Series_Temporales_completado.ipynb) | Pronóstico con LSTM |
| 7 | [Ejercicio 04c — Descripción de imágenes](semana05/Ejercicio_04c_RNN_Descripcion_Imagenes%20_completado.ipynb) | Generación de descripciones a partir de imágenes |
| 8 | [Ejercicio 04d — NLP para triaje clínico](semana05/Ejercicio_04d_RNN_NLP_Salud_Triaje_Clinico_completado.ipynb) | Ejemplo educativo de clasificación de texto |
| 9 | [Ejercicio 05 — Entrenamiento e hiperparámetros](semana05/Ejercicio_05_Entrenamiento_Ajuste_Hiperparametros_completado.ipynb) | Ajuste de parámetros del entrenamiento |
| 10 | [Ejercicio 06 — Evaluación y despliegue](semana05/Ejercicio_06_Evaluacion_Despliegue_Modelos_completado.ipynb) | Métricas y guardado de modelos |

### Cómo ejecutarlos en Google Colab

1. Abre [Google Colab](https://colab.research.google.com/).
2. Descarga el notebook desde GitHub o súbelo a Colab.
3. Ejecuta las celdas en orden, desde la primera hasta la última.
4. Si modificas una celda anterior, vuelve a ejecutar las celdas posteriores que dependan de ella.
5. Guarda las gráficas y resultados que solicite el docente.

### Dependencias y buenas prácticas

- Los notebooks pueden utilizar NumPy, Pandas, Matplotlib, scikit-learn, TensorFlow/Keras o PyTorch.
- Algunos ejercicios descargan datos o imágenes de internet y necesitan conexión.
- Ejecuta las celdas en orden y revisa los errores antes de continuar.
- Los resultados pueden variar según las versiones de las bibliotecas y los recursos disponibles.
- El ejercicio de triaje clínico es material académico y no debe utilizarse para tomar decisiones médicas reales.
- Antes de entregar, reinicia el entorno y ejecuta todas las celdas para comprobar que el notebook funciona desde el principio.
