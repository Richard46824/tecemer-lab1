"""Pruebas para el organizador de archivos."""

import sys
from pathlib import Path

# Permite ejecutar pytest desde la raíz del repositorio.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from organizador import clasificar, organizar_carpeta


def test_clasificar_reconoce_imagen(tmp_path):
    archivo = tmp_path / "foto.jpg"
    archivo.write_text("contenido")
    assert clasificar(archivo) == "Imagenes"


def test_organizar_mueve_archivo_a_subcarpeta(tmp_path):
    archivo = tmp_path / "foto.jpg"
    archivo.write_text("contenido")

    organizar_carpeta(tmp_path)

    assert (tmp_path / "Imagenes" / "foto.jpg").exists()
    assert not archivo.exists()


def test_organizar_en_modo_simulacion_no_mueve_nada(tmp_path):
    archivo = tmp_path / "foto.jpg"
    archivo.write_text("contenido")

    organizar_carpeta(tmp_path, simulacion=True)

    assert archivo.exists()
    assert not (tmp_path / "Imagenes").exists()
