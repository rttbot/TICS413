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
**Función:** "La capa física se encarga de transmitir los bits de información a través de medios físicos como cables o ondas. Es como las carreteras por donde circulan los autos. En términos de seguridad, esta capa es importante porque si se compromete físicamente, toda la comunicación se interrumpe."

**Protocolos:** "Los protocolos principales son: Ethernet, WiFi y fibra óptica. Ethernet se usa para transmisión por cable. WiFi se usa para transmisión inalámbrica. Fibra óptica se usa para transmisión por luz."

**Ataques:** "Los ataques más comunes en esta capa son: interceptación física, jamming y sabotaje. Interceptación física funciona cuando alguien instala un dispositivo en el cable. Jamming funciona cuando se bloquean las señales de radio. Sabotaje funciona cuando se cortan los cables físicamente."

**Mitigación:** "Para protegerse, se pueden usar: monitoreo físico, blindaje de cables y análisis de espectro. Monitoreo físico se implementa con cámaras y sensores. Blindaje de cables se implementa con materiales protectores. Análisis de espectro se implementa con analizadores de frecuencia."

---

### **CAPA 2 - ENLACE DE DATOS**
**Función:** "La capa de enlace se encarga de transmitir frames de datos entre dispositivos conectados directamente. Es como el sistema de placas de autos donde cada dispositivo tiene una identidad única. En términos de seguridad, esta capa es importante porque controla el acceso al medio de transmisión."

**Protocolos:** "Los protocolos principales son: Ethernet, WiFi y PPP. Ethernet se usa para redes cableadas. WiFi se usa para redes inalámbricas. PPP se usa para conexiones punto a punto."

**Ataques:** "Los ataques más comunes en esta capa son: MAC spoofing, ARP poisoning y VLAN hopping. MAC spoofing funciona cuando se falsifica la dirección MAC de un dispositivo. ARP poisoning funciona cuando se envenena la tabla ARP. VLAN hopping funciona cuando se salta entre VLANs separadas."

**Mitigación:** "Para protegerse, se pueden usar: port security, VLANs y switches inteligentes. Port security se implementa con bloqueo de puertos por MAC. VLANs se implementa con separación lógica de tráfico. Switches inteligentes se implementa con funciones avanzadas de seguridad."

---

### **CAPA 3 - RED**
**Función:** "La capa de red se encarga de enrutar paquetes entre redes diferentes. Es como el sistema de direcciones y mapas que decide qué ruta tomar. En términos de seguridad, esta capa es importante porque controla el enrutamiento y direccionamiento de toda la red."

**Protocolos:** "Los protocolos principales son: IP, ICMP y OSPF. IP se usa para direccionamiento de paquetes. ICMP se usa para mensajes de control. OSPF se usa para enrutamiento dinámico."

**Ataques:** "Los ataques más comunes en esta capa son: IP spoofing, DDoS y route poisoning. IP spoofing funciona cuando se falsifica la dirección IP de origen. DDoS funciona cuando se satura la red con tráfico falso. Route poisoning funciona cuando se envenenan las tablas de enrutamiento."

**Mitigación:** "Para protegerse, se pueden usar: firewalls, IDS/IPS y routers seguros. Firewalls se implementa con filtros de tráfico. IDS/IPS se implementa con sistemas de detección. Routers seguros se implementa con funciones de seguridad avanzadas."

---

### **CAPA 4 - TRANSPORTE**
**Función:** "La capa de transporte se encarga de la comunicación confiable entre aplicaciones. Es como el sistema de entrega de paquetes que asegura que lleguen completos. En términos de seguridad, esta capa es importante porque garantiza la integridad de la comunicación."

**Protocolos:** "Los protocolos principales son: TCP, UDP y SCTP. TCP se usa para conexiones confiables. UDP se usa para conexiones rápidas. SCTP se usa para conexiones múltiples."

**Ataques:** "Los ataques más comunes en esta capa son: SYN flooding, port scanning y session hijacking. SYN flooding funciona cuando se llenan las colas de conexión. Port scanning funciona cuando se revisan todos los puertos. Session hijacking funciona cuando se roba una sesión activa."

**Mitigación:** "Para protegerse, se pueden usar: firewalls de estado, IDS y honeypots. Firewalls de estado se implementa con control de conexiones. IDS se implementa con detección de anomalías. Honeypots se implementa con trampas para atacantes."

---

### **CAPA 5 - SESIÓN**
**Función:** "La capa de sesión se encarga de mantener el estado de las conexiones entre aplicaciones. Es como un coordinador de reuniones que organiza cuándo empiezan y terminan. En términos de seguridad, esta capa es importante porque controla el ciclo de vida de las sesiones."

**Protocolos:** "Los protocolos principales son: NetBIOS, RPC y SQL*Net. NetBIOS se usa para servicios de red Windows. RPC se usa para llamadas remotas. SQL*Net se usa para conexiones de base de datos."

**Ataques:** "Los ataques más comunes en esta capa son: session fixation, session replay y session hijacking. Session fixation funciona cuando se fuerza una sesión específica. Session replay funciona cuando se graba y repite una conversación. Session hijacking funciona cuando se toma control de una sesión."

**Mitigación:** "Para protegerse, se pueden usar: tokens únicos, timeouts y gestores de sesión. Tokens únicos se implementa con identificadores únicos. Timeouts se implementa con expiración automática. Gestores de sesión se implementa con control centralizado."

---

### **CAPA 6 - PRESENTACIÓN**
**Función:** "La capa de presentación se encarga de convertir datos entre diferentes formatos. Es como un traductor que convierte información de un idioma a otro. En términos de seguridad, esta capa es importante porque controla la codificación y encriptación de datos."

**Protocolos:** "Los protocolos principales son: SSL/TLS, MIME y XDR. SSL/TLS se usa para encriptación de datos. MIME se usa para tipos de archivo. XDR se usa para representación de datos."

**Ataques:** "Los ataques más comunes en esta capa son: format string attacks, encoding attacks y compression bombs. Format string attacks funciona cuando se inyecta código en texto. Encoding attacks funciona cuando se usan caracteres especiales maliciosos. Compression bombs funciona cuando se expanden archivos infinitamente."

**Mitigación:** "Para protegerse, se pueden usar: validación de entrada, filtros de archivo y antivirus. Validación de entrada se implementa con verificación de datos. Filtros de archivo se implementa con bloqueo de tipos peligrosos. Antivirus se implementa con detección de malware."

---

### **CAPA 7 - APLICACIÓN**
**Función:** "La capa de aplicación se encarga de proporcionar servicios directamente al usuario. Es como la interfaz de una tienda donde los clientes interactúan con los servicios. En términos de seguridad, esta capa es importante porque es el punto de entrada directo para los usuarios."

**Protocolos:** "Los protocolos principales son: HTTP/HTTPS, SMTP/POP3 y FTP. HTTP/HTTPS se usa para navegación web. SMTP/POP3 se usa para correo electrónico. FTP se usa para transferencia de archivos."

**Ataques:** "Los ataques más comunes en esta capa son: SQL injection, XSS y phishing. SQL injection funciona cuando se inyectan comandos en bases de datos. XSS funciona cuando se ejecutan scripts maliciosos. Phishing funciona cuando se engaña a los usuarios."

**Mitigación:** "Para protegerse, se pueden usar: WAF, antivirus y filtros de spam. WAF se implementa con firewalls de aplicación. Antivirus se implementa con detección de malware. Filtros de spam se implementa con bloqueo de correo no deseado."

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
