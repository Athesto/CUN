# Cuestionario de Programación Web

Proyecto desarrollado para la Actividad de Construcción Aplicada (ACA) de Programación Web de la CUN.

## Página publicada

[Abrir el cuestionario de repaso](https://athesto.github.io/CUN/cursos/programacion-web/)

Tema seleccionado: **Educación**.

## Propósito del proyecto

Esta página permite practicar conceptos básicos de HTML, CSS, formularios y JavaScript. En cada intento se seleccionan cinco preguntas al azar de un banco más amplio. El estudiante responde una pregunta a la vez y recibe una explicación, la sesión de clase y el minuto donde se trató el tema. Al finalizar se muestra la puntuación obtenida y se puede iniciar otro intento con una selección diferente.

La página funciona únicamente en el navegador. No utiliza frameworks, bases de datos ni un servidor de aplicación. `questions.json` es un recurso local que JavaScript carga mediante `fetch()`; no corresponde a una API REST.

## Organización de los archivos

```text
programacion-web/
├── index.html
├── styles.css
├── script.js
├── questions.json
├── README.md
└── images/
    └── educacion-digital.svg
```

- `index.html`: estructura semántica, encabezado, navegación, secciones, imagen, enlaces, formulario, botones y pie de página.
- `styles.css`: paleta, tipografía, espacios, estados de respuesta y diseño responsive con Grid, Flexbox y una media query.
- `script.js`: carga el banco, selecciona cinco preguntas al azar, valida las respuestas, actualiza el progreso, calcula el resultado y permite reiniciar.
- `questions.json`: almacena preguntas, opciones, respuesta correcta, justificación y referencia a la sesión y minuto de clase.
- `images/educacion-digital.svg`: ilustración independiente utilizada en la presentación.

## Integración de las tecnologías

HTML aporta la estructura y los elementos con los que interactúa el usuario. CSS presenta esos elementos con una identidad visual inspirada en paisajes de pixel art. JavaScript escucha eventos, modifica el DOM y actualiza el contenido sin recargar la página.

Las funcionalidades interactivas principales son:

1. Selección aleatoria de cinco preguntas sin repetir las del intento inmediatamente anterior.
2. Comprobación de respuestas con retroalimentación correcta o incorrecta.
3. Presentación de una justificación y una referencia académica.
4. Actualización de la puntuación y la barra de progreso.
5. Resultado final y generación de un nuevo intento.

## Ejecución local

Debido al uso de `fetch()`, se debe ejecutar la página mediante un servidor local. Desde esta carpeta:

```bash
python3 -m http.server 8000
```

Después se abre `http://localhost:8000` en el navegador.

## Libreto para el video explicativo

El video debe durar máximo diez minutos, incluir captura de pantalla y audio, y explicarse con palabras propias. No se debe leer literalmente el código ni utilizar una voz generada por inteligencia artificial.

### 0:00-0:40 - Presentación

- Presentar al estudiante o integrantes.
- Indicar que el tema seleccionado es Educación.
- Explicar que se desarrolló un cuestionario para repasar Programación Web.
- Mencionar el uso de HTML, CSS y JavaScript.

### 0:40-2:00 - Explicación de HTML

- Mostrar `index.html` en el editor.
- Explicar la estructura básica del documento.
- Señalar el encabezado, la navegación y las secciones de inicio, temas, cuestionario y recursos.
- Mostrar la imagen, los enlaces, el formulario, los botones y el pie de página.
- Explicar la utilidad de las etiquetas semánticas.

### 2:00-3:15 - Explicación de CSS

- Mostrar `styles.css`.
- Explicar las variables de la paleta de colores.
- Señalar los estilos de tarjetas, opciones y botones.
- Explicar los estados de respuesta correcta e incorrecta.
- Mostrar el uso de Grid, Flexbox y la media query responsive.

### 3:15-5:00 - Explicación de JavaScript y JSON

- Mostrar `script.js` y explicar la carga de `questions.json` con `fetch()`.
- Aclarar que el JSON es un archivo estático y no una API REST.
- Explicar cómo se baraja el banco y se seleccionan cinco preguntas.
- Mostrar el evento del formulario que comprueba la respuesta.
- Explicar la manipulación del DOM para presentar preguntas, retroalimentación y puntuación.
- Mostrar los campos de cada registro en `questions.json`.

### 5:00-5:30 - Integración

- Resumir que HTML crea la estructura, CSS controla la presentación y JavaScript aporta interactividad.
- Explicar que JavaScript toma los datos del JSON y los coloca en los elementos HTML.

### 5:30-7:30 - Demostración

- Abrir la página y recorrer la navegación.
- Responder correctamente una pregunta.
- Mostrar la justificación y la referencia de sesión y minuto.
- Responder incorrectamente otra pregunta para mostrar el segundo estado.
- Señalar la puntuación y la barra de progreso.

### 7:30-8:30 - Resultado y nuevo intento

- Finalizar las cinco preguntas.
- Explicar el resultado final.
- Pulsar **Intentar de nuevo** y mostrar la nueva selección aleatoria.

### 8:30-9:00 - Diseño responsive y cierre

- Reducir el tamaño de la ventana para demostrar la adaptación.
- Resumir los aprendizajes y la integración de las tecnologías.
- Finalizar agradeciendo la atención.

## Documento académico del ACA

El documento debe entregarse en PDF, tener una extensión sugerida de 8 a 15 páginas y contener, en este orden:

1. Portada con institución, asignatura, actividad, estudiantes, programa, docente y fecha.
2. Introducción que declare el tema Educación, las tecnologías utilizadas y el propósito.
3. Un objetivo general y entre tres y cuatro objetivos específicos redactados en infinitivo.
4. Desarrollo: planeación, estructura, navegación, funcionalidades y explicación de HTML, CSS y JavaScript.
5. Enlace accesible al video de máximo diez minutos.
6. Mínimo tres conclusiones sobre aprendizajes, dificultades e integración.
7. Mínimo tres referencias con formato académico coherente, preferiblemente APA 7.

Las capturas y fragmentos de código deben numerarse y titularse. El formato solicitado es Arial 12 o Times New Roman 12, interlineado 1,5 y márgenes de 2,54 cm.

## Lista de verificación

- [ ] Validar `index.html` con W3C y guardar una captura.
- [ ] Probar navegación, enlaces, imagen, botones y cuestionario.
- [ ] Confirmar que la consola no muestre errores.
- [ ] Tomar y numerar las capturas del documento.
- [ ] Terminar el documento académico y exportarlo como PDF.
- [ ] Grabar un video de máximo diez minutos mostrando código y página.
- [ ] Compartir el video con permisos de visualización.
- [ ] Incluir y comprobar el enlace del video dentro del PDF.
- [ ] Comprimir el proyecto en formato ZIP.
- [ ] Subir el ZIP a Drive con permisos de visualización.
- [ ] Realizar la entrega individual de cada integrante.

## Recursos

- [MDN: aprende desarrollo web](https://developer.mozilla.org/es/docs/Learn_web_development)
- [Validador de HTML del W3C](https://validator.w3.org/)
- [Validador de CSS del W3C](https://jigsaw.w3.org/css-validator/)
