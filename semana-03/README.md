# Semana 3 - Fundamentos de Redes: Capas 5-7 del Modelo OSI

**Fecha:** 18 de agosto, 2025  
**Unidad:** Unidad 1 - Seguridad en Protocolos y Redes  
**Tema:** Fundamentos de redes y protocolos  
**Contenido:** Repaso: Arquitectura de redes y protocolos TCP/IP  
**Profesor:** Danilo Bórquez  
**Libro de Referencia:** Tanenbaum, A. S. (2003). *Redes de computadoras*. Pearson Educación.

---

## Estructura de la Clase

### Bloque 1 (70 minutos)
**Tema:** Capas 5-6 del Modelo OSI: Sesión y Presentación

#### Objetivos de Aprendizaje
- Comprender las funciones de las capas 5 y 6 del modelo OSI
- Identificar servicios de sesión y presentación
- Entender la importancia de estas capas para las aplicaciones
- Analizar protocolos de estas capas

#### Contenido del Bloque 1
1. **Capa 5 - Sesión (Session Layer)** (30 min)
   - **Servicios:** Gestión de sesiones entre aplicaciones
   - **Funciones:** Establecimiento, mantenimiento y terminación de sesiones
   - **Protocolos:** NetBIOS, RPC (Remote Procedure Call), SQL*Net
   - **Características:** Checkpointing, recuperación, sincronización
   - **Aplicaciones:** Conexiones persistentes, autenticación de sesión
   - **Ejemplos:** Sesiones web, conexiones de base de datos
   - **Estados de sesión:** Activa, suspendida, terminada

2. **Capa 6 - Presentación (Presentation Layer)** (25 min)
   - **Servicios:** Traducción de datos entre aplicaciones
   - **Funciones:** Codificación, compresión, encriptación
   - **Protocolos:** SSL/TLS, MIME, XDR (External Data Representation)
   - **Formatos:** JPEG, MPEG, ASCII, Unicode, XML, JSON
   - **Conversión de datos:** Transformación entre formatos
   - **Ejemplos:** Conversión de formatos, compresión de archivos
   - **Estandarización:** Formatos de datos, codificación

3. **Interacción entre Capas 5-6** (15 min)
   - **Flujo de datos:** Cómo se comunican las capas
   - **Optimización:** Técnicas de mejora de rendimiento
   - **Mecanismos de coordinación:** Sincronización entre capas
   - **Casos de uso:** Aplicaciones reales

---

### Break (15 minutos)

---

### Bloque 2 (70 minutos)
**Tema:** Capa 7 - Aplicación y Protocolos de Alto Nivel

#### Objetivos de Aprendizaje
- Comprender profundamente la capa de aplicación
- Analizar protocolos de aplicación comunes
- Entender la arquitectura cliente-servidor
- Identificar servicios críticos de red

#### Contenido del Bloque 2
1. **Capa 7 - Aplicación (Application Layer)** (40 min)
   - **Servicios:** Interfaz directa con el usuario
   - **Funciones:** Procesamiento de datos, interfaz de usuario
   - **Arquitectura:** Cliente-servidor, peer-to-peer, distribuida
   - **Protocolos principales:**
     - **HTTP/HTTPS:** Navegación web, métodos, headers, estados
     - **FTP/SFTP:** Transferencia de archivos, comandos, modos
     - **SMTP/POP3/IMAP:** Correo electrónico, flujo de mensajes
     - **DNS:** Resolución de nombres, estructura jerárquica
     - **DHCP:** Configuración automática de red
     - **SNMP:** Gestión de red, MIB, traps

2. **Análisis de Protocolos de Aplicación** (30 min)
   - **HTTP/HTTPS:** Métodos (GET, POST, PUT, DELETE), headers, códigos de estado
   - **DNS:** Estructura jerárquica, tipos de registros (A, AAAA, MX, CNAME)
   - **Correo electrónico:** Flujo de mensajes, protocolos SMTP, POP3, IMAP
   - **FTP:** Modos de conexión (activo/pasivo), comandos, autenticación
   - **Gestión de red:** SNMP, MIB, monitoreo, configuración

---

## Material de Lectura Obligatoria

### Tanenbaum, A. S. (2003). *Redes de computadoras*

#### Capítulo 7: LA CAPA DE APLICACIÓN
- **7.1 DNS: EL SISTEMA DE NOMBRES DE DOMINIO** (páginas 525-534)
  - El espacio de nombres del DNS
  - Registros de recursos de dominio
  - Servidores de nombres

- **7.2 CORREO ELECTRÓNICO** (páginas 535-553)
  - Arquitectura y servicios
  - El agente de usuario
  - Formatos de mensaje
  - Transferencia de mensajes
  - Entrega final

- **7.3 LA WORLD WIDE WEB** (páginas 554-580)
  - Arquitectura general
  - El lado estático
  - El lado dinámico
  - HTTP: el protocolo de transferencia de hipertexto
  - Rendimiento mejorado

- **7.4 MULTIMEDIA** (páginas 581-600)
  - Aplicaciones multimedia digital
  - Compresión de audio y video
  - Streaming de audio y video
  - Videoconferencia

---

## Actividades Teóricas

### Actividad 1: Análisis de Protocolos de Aplicación (Grupos de 3-4 personas)
**Duración:** 25 minutos  
**Objetivo:** Comprender el funcionamiento de protocolos de aplicación

**Instrucciones:**
1. Formen grupos de 3-4 personas
2. Cada grupo analiza un protocolo específico (HTTP, DNS, SMTP, FTP)
3. Identifiquen:
   - Estructura del protocolo
   - Métodos/comandos principales
   - Puertos utilizados
   - Flujo de comunicación

### Actividad 2: Simulación de Comunicación Cliente-Servidor (Individual)
**Duración:** 20 minutos  
**Objetivo:** Entender la arquitectura cliente-servidor

**Instrucciones:**
1. Simulen una comunicación HTTP básica
2. Analicen el flujo de datos entre cliente y servidor
3. Identifiquen los headers y su función
4. Comparen con otros protocolos

### Actividad 3: Análisis de Tráfico de Aplicación (Demostración)
**Duración:** 15 minutos  
**Objetivo:** Observar tráfico real de aplicaciones

**Herramientas:**
- Wireshark para captura de tráfico HTTP/DNS
- Análisis de headers de aplicación
- Identificación de servicios activos

---

## Recursos Adicionales

### Videos Recomendados
- [Protocolos de aplicación explicados](https://www.youtube.com/watch?v=4XeJdJ9Xlfs)
- [HTTP y HTTPS en detalle](https://www.youtube.com/watch?v=wW1A3nFhxX0)
- [DNS explicado paso a paso](https://www.youtube.com/watch?v=72snZctFFtA)
- [Correo electrónico y protocolos](https://www.youtube.com/watch?v=JRCJ6RtE3xU)

### Artículos de Interés
- [Guía completa de HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- [Protocolo DNS](https://tools.ietf.org/html/rfc1035)
- [Especificación SMTP](https://tools.ietf.org/html/rfc5321)
- [Arquitectura cliente-servidor](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html)

### Herramientas para Experimentar
- **Wireshark:** Análisis de tráfico de aplicación
- **Postman:** Pruebas de APIs HTTP
- **nslookup/dig:** Consultas DNS
- **telnet:** Conexiones a puertos específicos
- **curl:** Cliente HTTP de línea de comandos

---

## Evaluación y Seguimiento

### Preguntas de Reflexión
1. ¿Por qué es importante entender las capas de aplicación?
2. ¿Cómo se relacionan las capas 5-7 con las capas inferiores?
3. ¿Cuáles son las principales diferencias entre HTTP y HTTPS?
4. ¿Cómo funciona la arquitectura cliente-servidor?

### Tarea para la Próxima Clase
- Leer Capítulos 8.1-8.5 de Tanenbaum (Criptografía y algoritmos)
- Investigar un protocolo de aplicación específico (máximo 1 página)
- Preparar una presentación de 5 minutos sobre un protocolo de aplicación
- Completar ejercicios de análisis de protocolos de aplicación

---

## Notas Importantes

- **Participación activa:** Se espera participación en las discusiones sobre protocolos
- **Comprensión profunda:** Es fundamental entender estos protocolos
- **Material:** El libro de Tanenbaum es referencia obligatoria
- **Contacto:** Para dudas fuera de clase, usar el correo oficial del curso

---

**Próxima clase:** Semana 4 - Protocolos de seguridad de Internet y Aplicaciones de autenticación (Lab 2) 