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