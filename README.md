# Tecemer Lab 1 — Tecnologías Emergentes

Repositorio de prácticas del curso **Tecnologías Emergentes (IS046B)**. El contenido está organizado por semanas para localizar rápidamente el código, los datos y las actividades.

## Índice de prácticas

| Semana | Contenido | Carpeta |
|---|---|---|
| 1 | Estructura del proyecto, PEP 8, manejo de errores y ejercicios introductorios de NumPy | [semana01](semana01/README.md) |
| 2 | API Open-Meteo, datos de Huancayo, JSON/CSV y análisis con Pandas | [semana02](semana02/README.md) |
| 3 | Organizador de archivos, argumentos de terminal y pruebas con pytest | [semana03](semana03/README.md) |
| 4 | Preparación de datos y clasificación de lluvia con regresión logística y MLP | [semana04](semana04/README.md) |
| 5 | Notebooks de redes neuronales, CNN, RNN, NLP y evaluación de modelos | [semana05](semana05/README.md) |

## Instalación

Se requiere Python 3.10 o superior.

```bash
python -m venv .venv
```

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
pip install -e .
```

## Ejecutar la aplicación principal

Desde la raíz del repositorio:

```bash
python -m tecemer_lab1.main
```

La aplicación consulta una API pública de chistes. Requiere conexión a internet.

## Estructura

- `semana01/` a `semana05/`: prácticas organizadas por semana.
- `src/tecemer_lab1/`: paquete Python principal; se conserva el diseño `src-layout`.
- `requirements.txt`: dependencias del entorno.
- `pyproject.toml`: configuración e información del paquete.
- `.gitignore`: exclusiones de archivos locales y generados.

Los archivos de datos y modelos generados por las prácticas se mantienen junto a la semana correspondiente. Consulta el README de cada semana para conocer los comandos de ejecución.

## Autor y curso

Prácticas académicas de Tecnologías Emergentes — IS046B.
