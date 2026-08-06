# Cómo publicar una noticia

1. Crea una carpeta dentro de `noticias/` (por ejemplo, `mi-noticia`).
2. Crea `titulo.txt` y escribe únicamente el título de la noticia.
3. Crea `resumen.txt` y escribe el resumen que aparecerá en la portada.
4. Guarda la imagen de portada con uno de estos nombres:

```text
portada.jpg
portada.jpeg
portada.png
portada.webp
```

Debe haber solamente una de ellas. Los demás archivos multimedia pueden tener
cualquier nombre.

5. Si existe una versión completa, crea también `index.html`. Cuando este archivo
exista, la portada mostrará el botón **Leer más...**. Si no existe, se mostrará el
titular y el resumen sin dicho botón.

6. Desde la raíz del proyecto ejecuta:

```bash
python3 generar-noticias.py
```

El comando valida los textos y las imágenes, y vuelve a crear
`noticias-generadas.js`. La página principal lee ese catálogo y genera una tarjeta
`.noticia` por cada subcarpeta válida.
