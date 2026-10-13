# Semana 3 — Organizador de archivos

En esta semana hice un programa para ordenar archivos según su extensión. Antes de moverlos, puedo probar qué cambios realizaría usando la opción `--dry-run`. También preparé pruebas automáticas con pytest.

## Archivos

- `organizador.py`: contiene el programa que clasifica y mueve los archivos.
- `test_organizador.py`: comprueba el funcionamiento del organizador.

## Cómo probar el programa

Desde la carpeta principal del repositorio, ejecuta el comando de abajo y reemplaza la ruta por una carpeta de prueba:

```bash
python semana03/organizador.py "RUTA_A_LA_CARPETA" --dry-run
```

Primero revisa el resultado de la simulación. Si todo está bien, puedes ejecutar el programa sin `--dry-run` para realizar los movimientos:

```bash
python semana03/organizador.py "RUTA_A_LA_CARPETA"
```

## Ejecutar las pruebas

```bash
pytest semana03/test_organizador.py
```

Es mejor probar con una carpeta que contenga archivos de ejemplo y revisar la simulación antes de moverlos.
