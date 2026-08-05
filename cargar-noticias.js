(function () {
    "use strict";

    const contenedor = document.getElementById("contenedorNoticias");
    const noticias = Array.isArray(window.NOTICIAS) ? window.NOTICIAS : [];

    contenedor.replaceChildren();

    if (noticias.length === 0) {
        const aviso = document.createElement("p");
        aviso.className = "estado-noticias";
        aviso.textContent = "No hay noticias publicadas.";
        contenedor.append(aviso);
        return;
    }

    noticias.forEach(function (datos) {
        const noticia = document.createElement("article");
        noticia.className = "noticia";
        noticia.style.backgroundImage = `url(${JSON.stringify(datos.imagen)})`;

        const contenido = document.createElement("div");
        contenido.className = "mitad vertical";

        const titulo = document.createElement("h2");
        titulo.className = "titulo";
        titulo.textContent = datos.titulo;

        const resumen = document.createElement("p");
        resumen.className = "resumen";
        resumen.textContent = datos.resumen;

        const espacio = document.createElement("div");
        espacio.className = "mitad";
        espacio.setAttribute("aria-hidden", "true");

        contenido.append(titulo, resumen);

        if (datos.enlace) {
            const leerMas = document.createElement("a");
            leerMas.className = "leer-mas";
            leerMas.href = datos.enlace;
            leerMas.textContent = "Leer más...";
            contenido.append(leerMas);
        }

        noticia.append(contenido, espacio);
        contenedor.append(noticia);
    });

    contenedor.addEventListener("wheel", function (evento) {
        if (Math.abs(evento.deltaY) > Math.abs(evento.deltaX)) {
            evento.preventDefault();
            contenedor.scrollBy({ left: evento.deltaY, behavior: "smooth" });
        }
    }, { passive: false });
}());
