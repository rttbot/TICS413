# Semana 2 - Fundamentos de Redes: Capas 1-4 del Modelo OSI

**Fecha:** 11 de agosto, 2025  
**Unidad:** Unidad 1 - Seguridad en Protocolos y Redes  
**Tema:** Fundamentos de redes y protocolos  
**Contenido:** Repaso: Arquitectura de redes y protocolos TCP/IP  
**Profesor:** Danilo Bórquez  
**Libro de Referencia:** Tanenbaum, A. S. (2003). *Redes de computadoras*. Pearson Educación.

---

## Estructura de la Clase

### Bloque 1 (70 minutos)
**Tema:** Capas 1-2 del Modelo OSI: Física y Enlace de Datos

#### Objetivos de Aprendizaje
- Comprender profundamente las capas 1 y 2 del modelo OSI
- Identificar servicios y protocolos de cada capa
- Entender la relación entre capas y su funcionamiento
- Analizar el funcionamiento de dispositivos de red

#### Contenido del Bloque 1
1. **Capa 1 - Física (Physical Layer)** (25 min)
   - **Servicios:** Transmisión de bits entre dispositivos
   - **Funciones:** Codificación, modulación, sincronización
   - **Medios de transmisión:** Par trenzado, coaxial, fibra óptica, inalámbrico
   - **Dispositivos:** Hubs, repetidores, cables
   - **Características:** Ancho de banda, atenuación, interferencia
   - **Estandarización:** IEEE 802.3, 802.11, especificaciones físicas

2. **Capa 2 - Enlace de Datos (Data Link Layer)** (30 min)
   - **Servicios:** Transmisión confiable de frames entre nodos
   - **Funciones:** Control de flujo, detección de errores, control de acceso al medio
   - **Protocolos:** Ethernet (802.3), WiFi (802.11), PPP, HDLC
   - **Dispositivos:** Switches, bridges, tarjetas de red
   - **Subcapas:** LLC (Logical Link Control) y MAC (Media Access Control)
   - **Direccionamiento:** Direcciones MAC, tablas de conmutación

3. **Conmutación en Capa 2** (15 min)
   - **Learning bridges:** Aprendizaje automático de direcciones
   - **Spanning tree:** Prevención de bucles (STP, RSTP)
   - **VLANs:** Segmentación lógica de redes
   - **Switches inteligentes:** Funciones avanzadas de conmutación

---

### Break (15 minutos)

---

### Bloque 2 (70 minutos)
**Tema:** Capas 3-4 del Modelo OSI: Red y Transporte

#### Objetivos de Aprendizaje
- Comprender las funciones de las capas 3 y 4
- Analizar protocolos de enrutamiento y transporte
- Entender la importancia de estas capas para la conectividad
- Identificar servicios críticos de red

#### Contenido del Bloque 2
1. **Capa 3 - Red (Network Layer)** (35 min)
   - **Servicios:** Enrutamiento de paquetes entre redes
   - **Funciones:** Direccionamiento lógico, enrutamiento, fragmentación
   - **Protocolos:** IP (IPv4/IPv6), ICMP, IGMP
   - **Dispositivos:** Routers, gateways
   - **Algoritmos de enrutamiento:** RIP, OSPF, BGP
   - **Control de congestión:** Mecanismos de prevención y control
   - **Direccionamiento:** Subnetting, CIDR, NAT

2. **Capa 4 - Transporte (Transport Layer)** (35 min)
   - **Servicios:** Comunicación end-to-end entre aplicaciones
   - **Funciones:** Segmentación, control de flujo, control de errores
   - **Protocolos:** TCP, UDP, SCTP
   - **Características TCP:** Orientado a conexión, confiable, control de congestión
   - **Características UDP:** Sin conexión, no confiable, bajo overhead
   - **Puertos:** Asignación y rangos de puertos, servicios bien conocidos
   - **Estados de conexión:** Establecimiento, mantenimiento, terminación

---

## Material de Lectura Obligatoria

### Tanenbaum, A. S. (2003). *Redes de computadoras*

#### Capítulo 1: INTRODUCCIÓN
- **1.4 MODELOS DE REFERENCIA** (páginas 35-45)
  - Modelo OSI detallado
  - Comparación con TCP/IP
  - Crítica de ambos modelos

#### Capítulo 2: LA CAPA FÍSICA
- **2.2 MEDIOS DE TRANSMISIÓN GUIADOS** (páginas 82-90)
  - Características de cada medio
  - Limitaciones y capacidades

- **2.3 TRANSMISIÓN INALÁMBRICA** (páginas 91-99)
  - Espectro electromagnético
  - Diferentes tipos de transmisión

#### Capítulo 4: LA CAPA DE ENLACE DE DATOS
- **4.1 SERVICIOS DE LA CAPA DE ENLACE DE DATOS** (páginas 205-210)
- **4.2 DETECCIÓN DE ERRORES** (páginas 210-215)
- **4.3 PROTOCOLOS ELEMENTALES DE ENLACE DE DATOS** (páginas 215-225)
- **4.8 CONMUTACIÓN DE LA CAPA DE ENLACE DE DATOS** (páginas 285-299)

#### Capítulo 5: LA CAPA DE RED
- **5.1 ASPECTOS DE DISEÑO DE LA CAPA DE RED** (páginas 305-310)
- **5.2 ALGORITMOS DE ENRUTAMIENTO** (páginas 311-336)
- **5.6 LA CAPA DE RED DE INTERNET** (páginas 374-418)

#### Capítulo 6: LA CAPA DE TRANSPORTE
- **6.1 EL SERVICIO DE TRANSPORTE** (páginas 425-435)
- **6.2 ELEMENTOS DE LOS PROTOCOLOS DE TRANSPORTE** (páginas 436-453)
- **6.4 LOS PROTOCOLOS DE TRANSPORTE DE INTERNET: UDP** (páginas 464-473)
- **6.5 LOS PROTOCOLOS DE TRANSPORTE DE INTERNET: TCP** (páginas 474-499)

---

## Actividades Teóricas

### Actividad 1: Mapeo de Capas OSI (Grupos de 3-4 personas)
**Duración:** 20 minutos  
**Objetivo:** Comprender la relación entre capas y protocolos

**Instrucciones:**
1. Formen grupos de 3-4 personas
2. Reciban una lista de protocolos y dispositivos
3. Mapeen cada elemento a su capa OSI correspondiente
4. Expliquen la función de cada protocolo en su capa

### Actividad 2: Análisis de Headers (Individual)
**Duración:** 15 minutos  
**Objetivo:** Entender la estructura de datos en cada capa

**Instrucciones:**
1. Analicen headers de diferentes capas
2. Identifiquen campos importantes en cada header
3. Expliquen la función de cada campo
4. Comparen headers de diferentes protocolos

### Actividad 3: Simulación de Comunicación (Demostración)
**Duración:** 15 minutos  
**Objetivo:** Visualizar el proceso de encapsulación/desencapsulación

**Herramientas:**
- Simulador de red (Packet Tracer o similar)
- Análisis de trazas de paquetes
- Visualización de headers en tiempo real

---

## Recursos Adicionales

### Videos Recomendados
- [Modelo OSI explicado paso a paso](https://www.youtube.com/watch?v=vv4y_uOneC0)
- [Protocolos de la capa de enlace](https://www.youtube.com/watch?v=4XeJdJ9Xlfs)
- [Enrutamiento y protocolos de red](https://www.youtube.com/watch?v=PpsEaqJV_A0)
- [TCP vs UDP explicado](https://www.youtube.com/watch?v=qqRYWctL6cY)

### Artículos de Interés
- [Guía completa del modelo OSI](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html)
- [Protocolos de enrutamiento](https://www.ietf.org/rfc/rfc2453.txt)
- [Especificación TCP](https://tools.ietf.org/html/rfc793)

### Herramientas para Experimentar
- **Wireshark:** Análisis de headers de todas las capas
- **Cisco Packet Tracer:** Simulación de redes
- **GNS3:** Emulación de routers
- **tcpdump:** Captura y análisis de paquetes

---

## Evaluación y Seguimiento

### Preguntas de Reflexión
1. ¿Por qué es importante entender cada capa del modelo OSI?
2. ¿Cómo se relacionan las capas entre sí y qué implicaciones tiene esto?
3. ¿Cuáles son las principales diferencias entre TCP y UDP?
4. ¿Cómo afecta la elección de protocolos en cada capa al rendimiento de la red?

### Tarea para la Próxima Clase
- Leer Capítulos 7.1-7.5 de Tanenbaum (Capa de Aplicación)
- Investigar un protocolo de aplicación específico (HTTP, FTP, SMTP, etc.)
- Preparar una presentación de 5 minutos sobre un protocolo de aplicación
- Completar ejercicios de mapeo de capas OSI

---

## Notas Importantes

- **Participación activa:** Se espera participación en las discusiones sobre capas
- **Comprensión profunda:** Es fundamental entender bien estas capas
- **Material:** El libro de Tanenbaum es referencia obligatoria
- **Contacto:** Para dudas fuera de clase, usar el correo oficial del curso

---

**Próxima clase:** Semana 3 - Modelo OSI: Capas 5-7 (Sesión, Presentación, Aplicación) - Prof. Danilo Bórquez
