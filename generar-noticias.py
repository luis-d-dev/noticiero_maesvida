#!/usr/bin/env python3
"""Genera el catálogo que index.html usa para mostrar las noticias."""

import json
import posixpath
from pathlib import Path


RAIZ = Path(__file__).resolve().parent
DIRECTORIO_NOTICIAS = RAIZ / "noticias"
ARCHIVO_SALIDA = DIRECTORIO_NOTICIAS / "noticias-generadas.js"
EXTENSIONES_PORTADA = (".jpg", ".jpeg", ".png", ".webp")


def leer_noticia(carpeta):
    archivo_titulo = carpeta / "titulo.txt"
    archivo_resumen = carpeta / "resumen.txt"

    faltantes = [
        archivo.name
        for archivo in (archivo_titulo, archivo_resumen)
        if not archivo.is_file()
    ]
    if faltantes:
        raise ValueError(
            f"Faltan archivos en noticias/{carpeta.name}: {', '.join(faltantes)}"
        )

    titulo = archivo_titulo.read_text(encoding="utf-8").strip()
    resumen = archivo_resumen.read_text(encoding="utf-8").strip()
    if not titulo or not resumen:
        raise ValueError(
            f"titulo.txt y resumen.txt no pueden estar vacíos en "
            f"noticias/{carpeta.name}"
        )

    portadas = [
        carpeta / f"portada{extension}" for extension in EXTENSIONES_PORTADA
        if (carpeta / f"portada{extension}").is_file()
    ]
    if not portadas:
        extensiones = ", ".join(f"portada{ext}" for ext in EXTENSIONES_PORTADA)
        raise ValueError(
            f"Falta una imagen de portada en noticias/{carpeta.name}. "
            f"Nombres admitidos: {extensiones}"
        )
    if len(portadas) > 1:
        raise ValueError(
            f"Hay más de una imagen de portada en noticias/{carpeta.name}; "
            "deja solamente una"
        )

    imagen = portadas[0]

    documento = carpeta / "index.html"

    noticia = {
        "titulo": titulo,
        "resumen": resumen,
        "imagen": posixpath.normpath(
            posixpath.join("noticias", carpeta.name, imagen.name)
        ),
    }
    if documento.is_file():
        noticia["enlace"] = posixpath.join("noticias", carpeta.name, "index.html")

    return noticia


def main():
    carpetas = sorted(
        (ruta for ruta in DIRECTORIO_NOTICIAS.iterdir() if ruta.is_dir()),
        key=lambda ruta: ruta.name,
    )
    noticias = [leer_noticia(carpeta) for carpeta in carpetas]
    catalogo = json.dumps(noticias, ensure_ascii=False, indent=4)
    ARCHIVO_SALIDA.write_text(
        f"// Archivo generado automáticamente. No editar.\nwindow.NOTICIAS = {catalogo};\n",
        encoding="utf-8",
    )
    print(
        f"{len(noticias)} noticia(s) escrita(s) en "
        "noticias/noticias-generadas.js"
    )


if __name__ == "__main__":
    main()
