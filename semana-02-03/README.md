# 📘 Presentación de Redes - TICS413

## Descripción
Presentación completa en LaTeX sobre fundamentos de redes y el modelo OSI, diseñada para la nivelación teórica del curso TICS413 - Seguridad de Tecnologías de la Información.

## Contenido
La presentación cubre:
- **Fundamentos de Redes**: Definición, tipos y necesidad de protocolos
- **Modelo OSI**: Las 7 capas con analogías y ejemplos
- **TCP/IP**: Conjunto de protocolos y su funcionamiento
- **Capas Detalladas**: Explicación profunda de cada capa del modelo OSI
- **Conceptos Avanzados**: Arquitectura, topologías y rendimiento
- **Glosario y Repaso**: Términos clave y preguntas de evaluación

## Características
- **22 slides** con contenido completo
- **Analogías cotidianas** para facilitar la comprensión
- **Dibujos y diagramas** usando TikZ
- **Iconos FontAwesome** para mejor presentación visual
- **Colores personalizados** de la UAI
- **Formato 16:9** optimizado para pantallas modernas

## Requisitos para Compilación

### Paquetes LaTeX necesarios:
```bash
# En sistemas basados en Debian/Ubuntu
sudo apt-get install texlive-full texlive-latex-extra texlive-fonts-extra

# En macOS con MacTeX
# Instalar MacTeX desde https://www.tug.org/mactex/

# En Windows
# Instalar MiKTeX desde https://miktex.org/
```

### Paquetes específicos:
- `beamer` - Para presentaciones
- `tikz` - Para diagramas
- `fontawesome` - Para iconos
- `babel` - Para soporte en español
- `graphicx` - Para imágenes
- `booktabs` - Para tablas profesionales
- `colortbl` - Para colores en tablas
- `xcolor` - Para colores personalizados

## Compilación

### Compilación básica:
```bash
pdflatex presentacion-redes.tex
```

### Compilación con referencias (si las hay):
```bash
pdflatex presentacion-redes.tex
pdflatex presentacion-redes.tex
```

### Compilación con XeLaTeX (recomendado para fuentes):
```bash
xelatex presentacion-redes.tex
```

## Estructura de Archivos
```
semana-02-03/
├── presentacion-redes.tex    # Archivo principal de LaTeX
├── presentacion-redes.pdf    # Presentación compilada (se genera)
└── README.md                 # Este archivo
```

## Uso de la Presentación

### Para Profesores:
1. Compilar el archivo `.tex` para generar el PDF
2. Usar en clase con un proyector o pantalla
3. Las transiciones están configuradas para revelar contenido progresivamente
4. Incluye preguntas de repaso para evaluar la comprensión

### Para Estudiantes:
1. Revisar la presentación como material de estudio
2. Usar las analogías para entender conceptos complejos
3. Practicar con las preguntas de repaso
4. Consultar el glosario de términos clave

## Personalización

### Cambiar Colores:
Modificar las definiciones de color en la sección de configuración:
```latex
\definecolor{uaiBlue}{RGB}{0,84,147}
\definecolor{uaiOrange}{RGB}{255,102,0}
```

### Agregar Contenido:
- Cada slide está claramente marcado con comentarios
- Fácil agregar nuevas slides siguiendo el patrón existente
- Los iconos se pueden cambiar usando comandos FontAwesome

### Modificar Tema:
Cambiar el tema de Beamer modificando:
```latex
\usetheme{Madrid}
\usecolortheme{whale}
```

## Notas Importantes

### Sobre el Contenido:
- **Enfoque teórico**: No incluye ataques ni defensas de seguridad
- **Nivelación**: Diseñado para estudiantes que necesitan repasar conceptos básicos
- **Analogías**: Usa ejemplos cotidianos para explicar conceptos técnicos

### Sobre la Compilación:
- Asegurarse de tener todos los paquetes instalados
- La primera compilación puede tardar más tiempo
- Si hay errores, verificar que todos los paquetes estén disponibles

## Recursos Adicionales

### Libros Recomendados:
- **Computer Networks** - Andrew S. Tanenbaum
- **Computer Networking: A Top-Down Approach** - James F. Kurose

### Herramientas Prácticas:
- **Packet Tracer** - Simulador de redes de Cisco
- **Wireshark** - Analizador de protocolos de red
- **GNS3** - Simulador de redes avanzado

### Recursos Online:
- Cisco Networking Academy
- YouTube: "Modelo OSI explicado"
- Khan Academy: Computer Science

## Contacto y Soporte
Para dudas sobre la presentación o problemas de compilación, contactar al profesor del curso TICS413.

---

**Universidad Adolfo Ibáñez**  
**Curso: TICS413 - Seguridad de Tecnologías de la Información**  
**Semana: 02-03 - Nivelación Teórica en Redes**
