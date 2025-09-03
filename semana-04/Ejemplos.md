# **Pauta de Respuesta para Actividad "Seguridad por Capas - Modelo OSI"**

## **Instrucciones Generales**
Cada grupo debe responder **EXACTAMENTE** estos 4 puntos para su capa asignada. Usar lenguaje sencillo y analogías del mundo real.

---

## **ESTRUCTURA OBLIGATORIA (5 minutos total)**

### **1. FUNCIÓN DE LA CAPA (2 minutos)**
**¿Qué responder?**
- Explicar en 2-3 oraciones qué hace esta capa
- Usar analogía del mundo real
- Conectar con la seguridad de la organización

**Ejemplo de estructura:**
- "La capa [X] se encarga de [función específica]"
- "Es como [analogía del mundo real]"
- "En términos de seguridad, esta capa es importante porque [razón]"

---

### **2. SERVICIOS Y PROTOCOLOS (1 minuto)**
**¿Qué responder?**
- Mencionar 2-3 protocolos principales de la capa
- Explicar brevemente para qué sirve cada uno
- Conectar con la seguridad

**Ejemplo de estructura:**
- "Los protocolos principales son: [protocolo 1], [protocolo 2], [protocolo 3]"
- "[Protocolo 1] se usa para [función]"
- "[Protocolo 2] se usa para [función]"
- "[Protocolo 3] se usa para [función]"

---

### **3. VULNERABILIDADES Y ATAQUES TÍPICOS (1 minuto)**
**¿Qué responder?**
- Describir 2-3 ataques específicos de esta capa
- Explicar cómo funcionan en lenguaje sencillo
- Usar analogía si es posible

**Ejemplo de estructura:**
- "Los ataques más comunes en esta capa son: [ataque 1], [ataque 2], [ataque 3]"
- "[Ataque 1] funciona cuando [explicación simple]"
- "[Ataque 2] funciona cuando [explicación simple]"
- "[Ataque 3] funciona cuando [explicación simple]"

---

### **4. MEDIDAS DE MITIGACIÓN (1 minuto)**
**¿Qué responder?**
- Mencionar 2-3 controles de seguridad específicos
- Explicar software/herramientas que ayudan
- Dar ejemplos de buenas prácticas

**Ejemplo de estructura:**
- "Para protegerse, se pueden usar: [control 1], [control 2], [control 3]"
- "[Control 1] se implementa con [herramienta/software]"
- "[Control 2] se implementa con [herramienta/software]"
- "[Control 3] se implementa con [herramienta/software]"

---

## **EJEMPLOS POR CAPA**

### **CAPA 1 - FÍSICA**
**Función:** "La capa física se encarga de transmitir los bits de información a través de medios físicos como cables o ondas. Es como las carreteras por donde circulan los autos - si se rompen, nada puede pasar."

**Protocolos:** "Los estándares principales son Ethernet (cable), WiFi (inalámbrico) y fibra óptica. Ethernet define cómo se transmiten los datos por cable, WiFi por ondas de radio, y fibra óptica por luz."

**Ataques:** "Los ataques más comunes son: interceptación física (como instalar un dispositivo en el cable), jamming (como bloquear señales de radio), y sabotaje (como cortar cables)."

**Mitigación:** "Para protegerse, se usan: monitoreo físico (cámaras, sensores), blindaje de cables, y herramientas como analizadores de espectro para detectar interferencias."

---

### **CAPA 2 - ENLACE DE DATOS**
**Función:** "La capa de enlace se encarga de transmitir frames de datos entre dispositivos conectados directamente. Es como el sistema de placas de autos - cada dispositivo tiene una identidad única en la red local."

**Protocolos:** "Los protocolos principales son: Ethernet (para redes cableadas), WiFi (para redes inalámbricas), y PPP (para conexiones punto a punto)."

**Ataques:** "Los ataques más comunes son: MAC spoofing (como falsificar una placa de auto), ARP poisoning (como cambiar direcciones en un mapa), y VLAN hopping (como saltar entre carriles separados)."

**Mitigación:** "Para protegerse, se usan: port security (bloquear puertos por MAC), VLANs (separar tráfico), y herramientas como switches inteligentes con funciones de seguridad."

---

### **CAPA 3 - RED**
**Función:** "La capa de red se encarga de enrutar paquetes entre redes diferentes. Es como el sistema de direcciones y mapas - decide qué ruta tomar para llegar de un lugar a otro."

**Protocolos:** "Los protocolos principales son: IP (para direccionamiento), ICMP (para mensajes de control), y protocolos de enrutamiento como OSPF y BGP."

**Ataques:** "Los ataques más comunes son: IP spoofing (como usar una dirección falsa), DDoS (como saturar las carreteras), y route poisoning (como cambiar las direcciones en los mapas)."

**Mitigación:** "Para protegerse, se usan: firewalls (filtros de tráfico), IDS/IPS (sistemas de detección), y herramientas como routers con funciones de seguridad."

---

### **CAPA 4 - TRANSPORTE**
**Función:** "La capa de transporte se encarga de la comunicación confiable entre aplicaciones. Es como el sistema de entrega de paquetes - asegura que lleguen completos y en orden."

**Protocolos:** "Los protocolos principales son: TCP (conexión confiable) y UDP (conexión rápida). TCP garantiza entrega, UDP prioriza velocidad."

**Ataques:** "Los ataques más comunes son: SYN flooding (como llenar la sala de espera), port scanning (como revisar todas las puertas), y session hijacking (como robar una conversación en curso)."

**Mitigación:** "Para protegerse, se usan: firewalls de estado (controlar conexiones), IDS (detección de anomalías), y herramientas como honeypots para atrapar atacantes."

---

### **CAPA 5 - SESIÓN**
**Función:** "La capa de sesión se encarga de mantener el estado de las conexiones entre aplicaciones. Es como un coordinador de reuniones - organiza cuándo empiezan y terminan las conversaciones."

**Protocolos:** "Los protocolos principales son: NetBIOS (para redes Windows), RPC (para llamadas remotas), y SQL*Net (para bases de datos)."

**Ataques:** "Los ataques más comunes son: session fixation (como forzar una sesión específica), session replay (como grabar y repetir una conversación), y session hijacking (como tomar control de una sesión activa)."

**Mitigación:** "Para protegerse, se usan: tokens de sesión únicos, timeouts automáticos, y herramientas como gestores de sesión seguros."

---

### **CAPA 6 - PRESENTACIÓN**
**Función:** "La capa de presentación se encarga de convertir datos entre diferentes formatos. Es como un traductor - convierte información de un idioma a otro para que las aplicaciones se entiendan."

**Protocolos:** "Los protocolos principales son: SSL/TLS (para encriptación), MIME (para tipos de archivo), y formatos como JPEG, MPEG, XML."

**Ataques:** "Los ataques más comunes son: format string attacks (como inyectar código en texto), encoding attacks (como usar caracteres especiales maliciosos), y compression bombs (como archivos que se expanden infinitamente)."

**Mitigación:** "Para protegerse, se usan: validación de entrada, filtros de archivos, y herramientas como antivirus y analizadores de malware."

---

### **CAPA 7 - APLICACIÓN**
**Función:** "La capa de aplicación se encarga de proporcionar servicios directamente al usuario. Es como la interfaz de una tienda - donde los clientes interactúan directamente con los servicios."

**Protocolos:** "Los protocolos principales son: HTTP/HTTPS (para web), SMTP/POP3 (para email), FTP (para archivos), DNS (para nombres), y DHCP (para configuración)."

**Ataques:** "Los ataques más comunes son: SQL injection (como inyectar comandos maliciosos), XSS (como ejecutar scripts en navegadores), phishing (como engañar usuarios), y DDoS a nivel de aplicación."

**Mitigación:** "Para protegerse, se usan: WAF (firewalls de aplicación), antivirus, filtros de spam, y herramientas como sistemas de detección de intrusiones."

---

## **CONSEJOS IMPORTANTES**

✅ **Usar analogías del mundo real** - Piensa en ejemplos cotidianos  
✅ **Lenguaje sencillo** - Evita jerga técnica compleja  
✅ **Conectar con seguridad** - Siempre explica por qué es importante para la organización  
✅ **Tiempo estricto** - 5 minutos exactos, no más  
✅ **Estructura clara** - Seguir los 4 puntos en orden  

## **CRITERIOS DE EVALUACIÓN**

- **Claridad de explicación (40%)** - ¿Se entiende bien?
- **Uso de analogías (30%)** - ¿Son útiles y claras?
- **Precisión técnica (20%)** - ¿La información es correcta?
- **Creatividad (10%)** - ¿Son originales los ejemplos?
