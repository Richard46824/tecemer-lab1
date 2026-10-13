# Laboratorio Tecemer 1

Este repositorio contiene los trabajos que voy desarrollando en el curso de **Tecnologías Emergentes (IS046B)**. Para tener los ejercicios ordenados, los fui separando por semanas. En cada carpeta está el código y un LÉAME con una explicación de lo que se trabajó y cómo ejecutarlo.

## Trabajos por semana

| Semana | ¿Qué trabajé? | Documentación |
|---|---|---|
| 1 | Configuración del proyecto, Python, NumPy y ejercicios iniciales. | [Ver Semana 1](semana01/README.md) |
| 2 | Consulta de datos del clima de Huancayo usando Open-Meteo y análisis con Pandas. | [Ver Semana 2](semana02/README.md) |
| 3 | Un programa para organizar archivos y pruebas con pytest. | [Ver Semana 3](semana03/README.md) |
| 4 | Preparación de datos y una red neuronal para clasificar días lluviosos. | [Ver Semana 4](semana04/README.md) |
| 5 | Ejercicios de preprocesamiento, MLP, CNN, RNN y evaluación de modelos. | [Ver Semana 5](semana05/README.md) |

## Cómo preparar el proyecto

Necesitas tener Python 3.10 o una versión posterior. Abre una terminal en la carpeta del repositorio y crea un entorno virtual:

```bash
python -m venv .venv
```

En Windows PowerShell, actívalo con:

```powershell
.venv\Scripts\Activate.ps1
```

Después instala las dependencias y el proyecto en modo editable:

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
```

## Ejecutar la aplicación

Desde la carpeta principal puedes ejecutar:

```bash
python -m tecemer_lab1.main
```

La aplicación consulta una API pública de chistes, por lo que necesitas conexión a internet. Los ejercicios de cada semana tienen sus propios comandos; revisa el LÉAME de la carpeta antes de ejecutarlos.

## Cómo está organizado

- `semana01/` a `semana05/`: ejercicios y archivos de cada semana.
- `src/tecemer_lab1/`: código de la aplicación principal.
- `requirements.txt`: bibliotecas que utiliza el proyecto.
- `pyproject.toml`: configuración del paquete de Python.
- `.gitignore`: archivos locales que no se suben al repositorio.

## Datos del curso

**Curso:** Tecnologías Emergentes — IS046B  
**Autor:** Richard Torres Areche  
