"""Pruebas para el organizador de archivos."""

import sys
from pathlib import Path

import pytest

# Permite ejecutar pytest desde la raíz del repositorio.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from organizador import clasificar, organizar_carpeta


def test_clasificar_reconoce_imagen(tmp_path):
    archivo = tmp_path / "foto.jpg"
    archivo.write_text("contenido", encoding="utf-8")
    assert clasificar(archivo) == "Imagenes"


def test_organizar_mueve_archivo_a_subcarpeta(tmp_path):
    archivo = tmp_path / "foto.jpg"
    archivo.write_text("contenido", encoding="utf-8")

    total = organizar_carpeta(tmp_path)

    assert total == 1
    assert (tmp_path / "Imagenes" / "foto.jpg").read_text(encoding="utf-8") == "contenido"
    assert not archivo.exists()


def test_organizar_en_modo_simulacion_no_mueve_nada(tmp_path):
    archivo = tmp_path / "foto.jpg"
    archivo.write_text("contenido", encoding="utf-8")

    total = organizar_carpeta(tmp_path, simulacion=True)

    assert total == 1
    assert archivo.exists()
    assert not (tmp_path / "Imagenes").exists()


def test_no_sobrescribe_archivo_existente(tmp_path, capsys):
    archivo = tmp_path / "foto.jpg"
    archivo.write_text("archivo original", encoding="utf-8")
    destino_carpeta = tmp_path / "Imagenes"
    destino_carpeta.mkdir()
    destino = destino_carpeta / "foto.jpg"
    destino.write_text("archivo anterior", encoding="utf-8")

    total = organizar_carpeta(tmp_path)

    assert total == 0
    assert archivo.read_text(encoding="utf-8") == "archivo original"
    assert destino.read_text(encoding="utf-8") == "archivo anterior"
    assert "Omitido" in capsys.readouterr().out


def test_ruta_inexistente_muestra_error(tmp_path):
    with pytest.raises(FileNotFoundError, match="La carpeta no existe"):
        organizar_carpeta(tmp_path / "no-existe")


def test_ignora_archivos_ocultos(tmp_path):
    oculto = tmp_path / ".secreto.txt"
    oculto.write_text("no mover", encoding="utf-8")

    total = organizar_carpeta(tmp_path)

    assert total == 0
    assert oculto.exists()
