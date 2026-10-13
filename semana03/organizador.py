"""Organiza archivos en subcarpetas según su extensión sin sobrescribirlos."""

import argparse
import shutil
from pathlib import Path

CATEGORIAS = {
    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".txt": "Documentos",
    ".jpg": "Imagenes",
    ".jpeg": "Imagenes",
    ".png": "Imagenes",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".zip": "Comprimidos",
    ".rar": "Comprimidos",
}


def clasificar(archivo: Path) -> str:
    """Devuelve la categoría del archivo según su extensión."""
    return CATEGORIAS.get(archivo.suffix.lower(), "Otros")


def organizar_carpeta(carpeta: Path, simulacion: bool = False) -> int:
    """Organiza archivos sin sobrescribir destinos que ya existen.

    En modo simulación no mueve archivos ni crea carpetas.
    Devuelve el número de archivos que movió o que movería.
    """
    carpeta = Path(carpeta)
    if not carpeta.exists():
        raise FileNotFoundError(f"La carpeta no existe: {carpeta}")
    if not carpeta.is_dir():
        raise NotADirectoryError(f"La ruta no es una carpeta: {carpeta}")

    procesados = 0
    for archivo in carpeta.iterdir():
        if archivo.is_dir() or archivo.name.startswith("."):
            continue

        categoria = clasificar(archivo)
        destino_carpeta = carpeta / categoria
        destino = destino_carpeta / archivo.name

        if destino.exists():
            print(f"Omitido: {archivo.name}; ya existe en {categoria}")
            continue

        if simulacion:
            print(f"[SIMULACIÓN] {archivo.name} -> {categoria}")
        else:
            destino_carpeta.mkdir(exist_ok=True)
            # Comprueba otra vez antes de mover para no reemplazar un archivo
            # que haya aparecido en el destino mientras se ejecutaba el script.
            if destino.exists():
                print(f"Omitido: {archivo.name}; el destino ya existe")
                continue
            shutil.move(str(archivo), str(destino))
            print(f"Movido: {archivo.name} -> {categoria}")

        procesados += 1

    return procesados


def main() -> None:
    """Punto de entrada de la aplicación de terminal."""
    parser = argparse.ArgumentParser(description="Organiza archivos por tipo.")
    parser.add_argument("carpeta", type=Path, help="Carpeta a organizar")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simula los movimientos sin modificar archivos",
    )
    args = parser.parse_args()

    try:
        total = organizar_carpeta(args.carpeta, simulacion=args.dry_run)
    except (FileNotFoundError, NotADirectoryError) as error:
        parser.error(str(error))
    print(f"Total de archivos procesados: {total}")


if __name__ == "__main__":
    main()
