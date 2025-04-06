# TICS413 - Actividades 

Este repositorio contiene las actividades prácticas del curso TICS413 - para eso vaya al sitio web https://rttbot.github.io/TICS413/ - Clone este repo y vaya realizando las actividades en su máquina. 

## Crear una Página Web "Hola Mundo" usando GitHub Pages

Sigue estos pasos para crear y desplegar una página web simple que diga "Hola Mundo" utilizando GitHub Pages:

### Paso 1: Crear el archivo `index.html`

1. Crea una carpeta llamada `docs` en el directorio raíz del proyecto.
2. Dentro de la carpeta `docs`, crea un archivo llamado `index.html`.
3. Añade el siguiente contenido al archivo `index.html`:

    ```html
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hola Mundo</title>
    </head>
    <body>
        <h1>Hola Mundo</h1>
    </body>
    </html>
    ```

### Paso 2: Configurar GitHub Pages

1. Ve a la configuración del repositorio en GitHub.
2. Busca la sección de "GitHub Pages".
3. Selecciona la rama que deseas usar para el sitio (generalmente `main`) y la carpeta `/docs` como la fuente.
4. Guarda los cambios.

### Paso 3: Verificar el Despliegue

1. Una vez configurado, GitHub Pages generará un enlace donde podrás ver tu página web.
2. Visita el enlace proporcionado para ver tu página "Hola Mundo".

Con estos pasos, tendrás una página web simple desplegada en GitHub Pages. Puedes modificar el contenido del `index.html` para personalizar tu página.

## Crear una Cuenta en GitHub

Para aprovechar al máximo las herramientas disponibles, se recomienda crear una cuenta en GitHub utilizando su cuenta de correo UAI de alumnos. Esto les permitirá acceder a beneficios como GitHub Copilot, que puede ser de gran ayuda en sus proyectos de programación.

## Herramientas Recomendadas

Para el desarrollo de las actividades, se recomienda utilizar editores de código como Cursor o Visual Studio Code (VSCode), que ofrecen una excelente experiencia de desarrollo y soporte para múltiples lenguajes de programación.

## Estructura del Proyecto

No se permitirá clonar este repositorio directamente. La idea es que cada estudiante arme la estructura del proyecto en su propia máquina. Se les proporcionará un archivo zip a través de Webcursos, que contendrá los archivos necesarios para comenzar. A partir de ahí, deberán configurar su propio ambiente de desarrollo de manera independiente.



## Pasos Básicos para Crear el Proyecto en Cursor

### Crear un Proyecto en Cursor

1. Abre Cursor y selecciona la opción para crear un nuevo proyecto.
2. Asigna un nombre al proyecto y selecciona la ubicación donde deseas guardarlo.

### Clonar un Repositorio Vacío

1. Abre la terminal en Cursor.
2. Clona el repositorio vacío que has creado en GitHub con el siguiente comando:

    ```bash
    git clone <URL_DEL_REPOSITORIO_VACÍO>
    ```

### Crear Archivos en la Estructura

1. Navega al directorio del proyecto clonado.
2. Crea un archivo `README.md` y otros archivos necesarios para la estructura del proyecto utilizando el comando `touch`:

    ```bash
    touch README.md
    ```

3. Abre los archivos en Cursor y añade el contenido necesario.

### Hacer Públicos los Cambios

1. Añade los archivos al control de versiones:

    ```bash
    git add .
    ```

2. Realiza un commit con un mensaje descriptivo:

    ```bash
    git commit -m "Inicializar proyecto con estructura básica"
    ```

3. Sube los cambios al repositorio remoto:

    ```bash
    git push origin main
    ```

### Trabajo en Grupos

- Las actividades se realizarán en grupos. Un representante del grupo puede crear el repositorio y realizar los pasos iniciales.
- Los demás miembros del grupo pueden unirse al repositorio y colaborar en el desarrollo.

## Recursos Útiles

- [GitHub - Crear una cuenta](https://github.com/join)
- [GitHub Copilot](https://github.com/features/copilot)
- [Visual Studio Code - Descarga](https://code.visualstudio.com/)
- [Documentación de GitHub Pages](https://docs.github.com/en/pages)
- [Curso de Git y GitHub](https://www.udemy.com/course/git-and-github-bootcamp/)