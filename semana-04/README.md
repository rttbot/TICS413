# Semana 3 - Fundamentos de Redes y Protocolos (Lab 1)

**Fecha:** 18 de agosto, 2025  
**Unidad:** Unidad 1 - Seguridad en Protocolos y Redes  
**Tema:** Fundamentos de redes y protocolos  
**Contenido:** Repaso: Arquitectura de redes y protocolos TCP/IP  
**Lab:** Lab 1 - Análisis de tráfico de red  
**Libro de Referencia:** Tanenbaum, A. S. (2003). *Redes de computadoras*. Pearson Educación.

---

## Estructura de la Clase

### Bloque 1 (70 minutos)
**Tema:** Medios de transmisión y seguridad física

#### Objetivos de Aprendizaje
- Comprender las características de los diferentes medios de transmisión
- Identificar vulnerabilidades en medios guiados e inalámbricos
- Analizar técnicas de interceptación y contramedidas
- Entender la importancia de la seguridad física en redes

#### Contenido del Bloque 1
1. **Medios de Transmisión Guiados** (30 min)
   - Par trenzado: características y vulnerabilidades
   - Cable coaxial: ventajas y limitaciones de seguridad
   - Fibra óptica: seguridad y técnicas de interceptación
   - Líneas eléctricas: riesgos y consideraciones

2. **Transmisión Inalámbrica** (25 min)
   - Espectro electromagnético y asignación de frecuencias
   - Radiotransmisión: vulnerabilidades y jamming
   - Transmisión por microondas: interceptación y contramedidas
   - Transmisión infrarroja: limitaciones y aplicaciones

3. **Seguridad Física en Redes** (15 min)
   - Técnicas de interceptación física
   - Contramedidas y buenas prácticas
   - Auditoría de seguridad física

---

### Break (15 minutos)

---

### Bloque 2 (70 minutos)
**Tema:** Lab 1 - Análisis de tráfico de red

#### Objetivos de Aprendizaje
- Utilizar herramientas de análisis de tráfico de red
- Identificar patrones de tráfico normal y anómalo
- Detectar posibles ataques en tiempo real
- Comprender la importancia del monitoreo de red

#### Contenido del Bloque 2
1. **Introducción a Wireshark** (20 min)
   - Instalación y configuración básica
   - Interfaz de usuario y filtros
   - Captura de paquetes en diferentes interfaces
   - Análisis de headers TCP/IP

2. **Análisis de Tráfico Normal** (25 min)
   - Identificación de protocolos comunes
   - Análisis de patrones de tráfico HTTP/HTTPS
   - Detección de servicios activos
   - Interpretación de logs de red

3. **Detección de Anomalías** (25 min)
   - Identificación de tráfico sospechoso
   - Detección de escaneos de puertos
   - Análisis de ataques de denegación de servicio
   - Herramientas de monitoreo en tiempo real

---

## Material de Lectura Obligatoria

### Tanenbaum, A. S. (2003). *Redes de computadoras*

#### Capítulo 2: LA CAPA FÍSICA
- **2.2 MEDIOS DE TRANSMISIÓN GUIADOS** (páginas 82-90)
  - Medios magnéticos
  - Par trenzado
  - Cable coaxial
  - Líneas eléctricas
  - Fibra óptica

- **2.3 TRANSMISIÓN INALÁMBRICA** (páginas 91-99)
  - El espectro electromagnético
  - Radiotransmisión
  - Transmisión por microondas
  - Transmisión infrarroja
  - Transmisión por ondas de luz

#### Capítulo 4: LA CAPA DE ENLACE DE DATOS
- **4.8 CONMUTACIÓN DE LA CAPA DE ENLACE DE DATOS** (páginas 285-299)
  - Usos de bridges
  - Learning bridges
  - Bridges con spanning tree
  - Virtual LANs

---

## Lab 1: Análisis de Tráfico de Red

### Objetivos del Laboratorio
1. Familiarizarse con herramientas de análisis de tráfico
2. Identificar diferentes tipos de tráfico de red
3. Detectar patrones anómalos y posibles ataques
4. Generar reportes de seguridad basados en análisis de tráfico

### Materiales Requeridos
- Computadora con Wireshark instalado
- Acceso a red (preferiblemente con tráfico real)
- Archivos de captura de ejemplo (se proporcionarán)
- Documentación de referencia

### Ejercicios Prácticos

#### Ejercicio 1: Configuración Inicial (15 min)
1. Instalar y configurar Wireshark
2. Familiarizarse con la interfaz
3. Configurar filtros básicos
4. Realizar primera captura de tráfico

#### Ejercicio 2: Análisis de Protocolos (20 min)
1. Identificar protocolos en el tráfico capturado
2. Analizar headers TCP/IP
3. Mapear puertos y servicios
4. Documentar hallazgos

#### Ejercicio 3: Detección de Anomalías (25 min)
1. Analizar archivos de captura con tráfico anómalo
2. Identificar patrones de ataque
3. Generar alertas de seguridad
4. Crear reporte de incidentes

#### Ejercicio 4: Análisis de Seguridad (10 min)
1. Evaluar vulnerabilidades en el tráfico observado
2. Proponer contramedidas
3. Documentar recomendaciones de seguridad

---

## Recursos Adicionales

### Videos Recomendados
- [Wireshark Tutorial para Principiantes](https://www.youtube.com/watch?v=TkCSr30UojM)
- [Análisis de Tráfico de Red](https://www.youtube.com/watch?v=4XeJdJ9Xlfs)
- [Detección de Intrusiones con Wireshark](https://www.youtube.com/watch?v=0KqRX9u6PQM)

### Artículos de Interés
- [Guía de Wireshark para Análisis de Seguridad](https://www.wireshark.org/docs/wsug_html_chunked/)
- [Técnicas de Interceptación de Fibra Óptica](https://www.sans.org/white-papers/60/)
- [Seguridad en Redes Inalámbricas](https://www.csoonline.com/article/2124697/wireless-security.html)

### Herramientas para Experimentar
- **Wireshark:** Análisis de tráfico de red
- **tcpdump:** Captura de paquetes en línea de comandos
- **Nmap:** Escaneo de puertos y servicios
- **Netcat:** Herramienta de red multipropósito
- **Ettercap:** Análisis de red y sniffing

---

## Evaluación y Seguimiento

### Preguntas de Reflexión
1. ¿Por qué es importante entender los medios de transmisión para la seguridad?
2. ¿Cuáles son las principales vulnerabilidades de las redes inalámbricas?
3. ¿Cómo puede el análisis de tráfico ayudar a detectar ataques?
4. ¿Qué herramientas son más efectivas para el monitoreo de red?

### Tarea para la Próxima Clase
- Completar el reporte del Lab 1 (máximo 3 páginas)
- Leer Capítulos 4.8 y 4.9 de Tanenbaum (Conmutación de capa de enlace)
- Investigar un caso real de interceptación de tráfico de red (máximo 1 página)
- Preparar 2 preguntas sobre protocolos de seguridad de Internet

---

## Notas Importantes

- **Laboratorio práctico:** Esta sesión incluye trabajo práctico con herramientas reales
- **Participación activa:** Se espera participación en los ejercicios del laboratorio
- **Material:** Traer computadora con Wireshark instalado
- **Contacto:** Para dudas fuera de clase, usar el correo oficial del curso

---

**Próxima clase:** Semana 4 - Protocolos de seguridad de Internet y Aplicaciones de autenticación (Lab 2)
