# Semana 3 — Automatización y pruebas

Esta práctica desarrolla un organizador que clasifica archivos por extensión y puede simular los movimientos antes de ejecutarlos.

## Archivos

- `organizador.py`: lógica de clasificación y movimiento de archivos.
- `test_organizador.py`: pruebas automatizadas con pytest.

## Uso

Desde la raíz del repositorio, primero simula los cambios:

```bash
python semana03/organizador.py "RUTA_A_LA_CARPETA" --dry-run
```

Si el resultado es correcto, ejecuta sin `--dry-run` para mover los archivos:

```bash
python semana03/organizador.py "RUTA_A_LA_CARPETA"
```

Reemplaza `RUTA_A_LA_CARPETA` por una carpeta de prueba. Se recomienda revisar la simulación antes de mover archivos.

## Ejecutar pruebas

```bash
pytest semana03/test_organizador.py
```
