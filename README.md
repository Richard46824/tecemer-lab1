# Laboratorio Tecemer 1

Prácticas del curso Tecnologías Emergentes (IS046B), organizadas por semanas.

## Semana 1: Configuración y NumPy

Se trabajó la estructura del proyecto en Python, el formato PEP 8 y ejercicios introductorios con NumPy.

Archivos principales: `numpy_demo.py` y `mini_reto.py`.

## Semana 2: Datos meteorológicos

Se consultó la API Open-Meteo para obtener el pronóstico de Huancayo y analizarlo con Pandas.

Archivos principales: `clima.py`, `analisis.py` y los archivos de datos JSON/CSV generados.

Para ejecutar:

```bash
cd semana02
python clima.py
python analisis.py
```

## Semana 3: Organizador de archivos

Se creó un programa para organizar archivos por extensión y se añadieron pruebas con pytest.

Archivo principal: `organizador.py`.

Primero se puede simular el proceso:

```bash
python semana03/organizador.py "RUTA_A_LA_CARPETA" --dry-run
```

Pruebas:

```bash
pytest semana03/test_organizador.py
```

## Instalación del proyecto

Crear y activar el entorno virtual en Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .
```

## Estructura

```text
tecemer-lab1/
├── semana01/
├── semana02/
├── semana03/
├── semana04/
├── semana05/
├── src/
├── pyproject.toml
└── requirements.txt
```

**Autor:** Richard Torres Areche46824  
**Curso:** Tecnologías Emergentes — IS046B
