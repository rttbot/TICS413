# Respuestas del Top Table Exercise: Simulación de Seguridad en Redes

## Objetivo

Este documento contiene las respuestas correctas para el ejercicio de tarjetas de amenazas, permitiendo a los docentes evaluar las respuestas de los estudiantes y proporcionar retroalimentación adecuada.

## Tabla de Respuestas Completas

```
┌─────────────────────────────────────────────────────────────┐
│                TABLA DE RESPUESTAS CORRECTAS                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  TARJETA │ CAPA OSI │ TIPO DE ATAQUE │ CONTRAMEDIDAS        │
│  ┌───────┼─────────┼───────────────┼─────────────────────┐ │
│  │   1   │ Capa 2  │ Interceptación│ • WPA3/WPA2          │ │
│  │       │ Enlace  │ WiFi          │ • Monitoreo de red   │ │
│  │       │ Datos   │               │ • WIDS/WIPS          │ │
│  │       │         │               │ • Segmentación VLAN  │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┤ │
│  │   2   │ Capa 2  │ Evil Twin     │ • Verificar SSID     │ │
│  │       │ Enlace  │ Attack        │ • Certificados SSL   │ │
│  │       │ Datos   │               │ • VPN obligatorio    │ │
│  │       │         │               │ • WIDS/WIPS          │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┤ │
│  │   3   │ Capa 4  │ SYN Flood     │ • SYN Cookies        │ │
│  │       │ Transp. │ (DDoS)        │ • Rate Limiting      │ │
│  │       │         │               │ • Firewalls          │ │
│  │       │         │               │ • DDoS Protection    │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┤ │
│  │   4   │ Capa 5  │ Session       │ • Timeouts           │ │
│  │       │ Sesión  │ Hijacking     │ • Regeneración IDs   │ │
│  │       │         │               │ • HTTPS obligatorio │ │
│  │       │         │               │ • Logout automático  │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┤ │
│  │   5   │ Capa 7  │ SQL Injection │ • Prepared Statements│ │
│  │       │ Aplic.  │               │ • Input Validation   │ │
│  │       │         │               │ • WAF               │ │
│  │       │         │               │ • Least Privilege    │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┤ │
│  │   6   │ Capa 3  │ IP Spoofing   │ • BCP38              │ │
│  │       │ Red     │               │ • Egress Filtering   │ │
│  │       │         │               │ • Firewalls          │ │
│  │       │         │               │ • Monitoreo de red   │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┤ │
│  │   7   │ Capa 1  │ WiFi Jamming │ • Redundancia        │ │
│  │       │ Física  │ (Multi-Capa) │ • Backup cableado    │ │
│  │       │ + Capa 2│               │ • Detección RF       │ │
│  │       │ Enlace  │               │ • Planes de respaldo │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┤ │
│  │   8   │ Multi- │ Malware       │ • Antivirus           │ │
│  │       │ Capa    │ Propagation   │ • Segmentación       │ │
│  │       │         │               │ • Monitoreo          │ │
│  │       │         │               │ • Educación usuarios │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┤ │
│  │   9   │ Capa 6  │ Man-in-the-   │ • Certificados SSL   │ │
│  │       │ Presen. │ Middle        │ • Certificate Pinning│ │
│  │       │         │               │ • VPN                │ │
│  │       │         │               │ • Validación cert.   │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┤ │
│  │  10   │ Capa 2  │ ARP Poisoning │ • ARP Monitoring     │ │
│  │       │ Enlace  │               │ • Static ARP         │ │
│  │       │ Datos   │               │ • VLANs              │ │
│  │       │         │               │ • Port Security      │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┤ │
│  │  11   │ Capa 4  │ Port Scanning │ • Firewalls          │ │
│  │       │ Transp. │               │ • IDS/IPS            │ │
│  │       │         │               │ • Honeypots          │ │
│  │       │         │               │ • Monitoreo          │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┤ │
│  │  12   │ Capa 7  │ Brute Force   │ • Rate Limiting      │ │
│  │       │ Aplic.  │ Attack        │ • MFA                │ │
│  │       │         │               │ • Account Lockout    │ │
│  │       │         │               │ • CAPTCHA            │ │
│  └───────┴─────────┴───────────────┴─────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Respuestas Detalladas por Tarjeta

### Tarjeta 1: Ataque de Interceptación WiFi

**Capa OSI:** Capa 2 (Enlace de Datos)
**Tipo de Ataque:** Interceptación WiFi / Packet Sniffing
**Explicación:** El atacante captura paquetes de datos que viajan por la red WiFi, accediendo a información sensible.

**Contramedidas Principales:**
- **WPA3/WPA2:** Usar protocolos de encriptación WiFi seguros
- **Monitoreo de Red:** Detectar usuarios no autorizados
- **WIDS/WIPS:** Sistemas de detección de intrusión inalámbrica
- **Segmentación VLAN:** Aislar tráfico sensible

### Tarjeta 2: Suplantación de Punto de Acceso

**Capa OSI:** Capa 2 (Enlace de Datos)
**Tipo de Ataque:** Evil Twin Attack
**Explicación:** El atacante crea un punto de acceso falso que imita la red legítima para interceptar conexiones.

**Contramedidas Principales:**
- **Verificar SSID:** Confirmar el nombre exacto de la red
- **Certificados SSL:** Usar conexiones HTTPS
- **VPN Obligatorio:** Encriptar todo el tráfico
- **WIDS/WIPS:** Detectar puntos de acceso maliciosos

### Tarjeta 3: Sobreflujo de Conexiones

**Capa OSI:** Capa 4 (Transporte)
**Tipo de Ataque:** SYN Flood / DDoS
**Explicación:** El atacante envía múltiples solicitudes SYN para agotar los recursos del servidor.

**Contramedidas Principales:**
- **SYN Cookies:** Proteger contra ataques SYN flood
- **Rate Limiting:** Limitar conexiones por IP
- **Firewalls:** Filtrar tráfico malicioso
- **DDoS Protection:** Servicios especializados

### Tarjeta 4: Robo de Sesiones

**Capa OSI:** Capa 5 (Sesión)
**Tipo de Ataque:** Session Hijacking
**Explicación:** El atacante secuestra una sesión activa para acceder como el usuario legítimo.

**Contramedidas Principales:**
- **Timeouts:** Cerrar sesiones inactivas
- **Regeneración IDs:** Cambiar IDs de sesión frecuentemente
- **HTTPS Obligatorio:** Encriptar comunicaciones
- **Logout Automático:** Cerrar sesiones automáticamente

### Tarjeta 5: Inyección de Código Web

**Capa OSI:** Capa 7 (Aplicación)
**Tipo de Ataque:** SQL Injection
**Explicación:** El atacante inserta código SQL malicioso en formularios web para acceder a la base de datos.

**Contramedidas Principales:**
- **Prepared Statements:** Usar consultas parametrizadas
- **Input Validation:** Validar todas las entradas
- **WAF:** Web Application Firewall
- **Least Privilege:** Mínimos permisos necesarios

### Tarjeta 6: Falsificación de Direcciones

**Capa OSI:** Capa 3 (Red)
**Tipo de Ataque:** IP Spoofing
**Explicación:** El atacante falsifica direcciones IP para ocultar su identidad real.

**Contramedidas Principales:**
- **BCP38:** Filtrar tráfico con IPs falsas
- **Egress Filtering:** Filtrar tráfico saliente
- **Firewalls:** Bloquear IPs maliciosas
- **Monitoreo de Red:** Detectar patrones anómalos

### Tarjeta 7: Bloqueo de Señales WiFi

**Capa OSI:** Capa 1 (Física) + Capa 2 (Enlace de Datos)
**Tipo de Ataque:** WiFi Jamming (Multi-Capa)
**Explicación:** El atacante interfiere con las comunicaciones WiFi tanto a nivel físico (interferencia electromagnética) como a nivel de protocolo (deauthentication frames, beacon flooding).

**Contramedidas Principales:**
- **Redundancia:** Múltiples puntos de acceso
- **Backup Cableado:** Conexiones físicas de respaldo
- **Detección RF:** Monitorear interferencias físicas
- **WIDS/WIPS:** Detectar ataques de protocolo
- **Planes de Respaldo:** Estrategias alternativas

### Tarjeta 8: Propagación de Malware

**Capa OSI:** Multi-Capa (1, 2, 3, 4, 7)
**Tipo de Ataque:** Malware Propagation
**Explicación:** El malware se propaga automáticamente a través de múltiples capas de la red.

**Contramedidas Principales:**
- **Antivirus:** Software de protección
- **Segmentación:** Aislar redes infectadas
- **Monitoreo:** Detectar comportamiento anómalo
- **Educación Usuarios:** Prevenir infecciones

### Tarjeta 9: Interceptación de Comunicaciones

**Capa OSI:** Capa 6 (Presentación)
**Tipo de Ataque:** Man-in-the-Middle (SSL/TLS)
**Explicación:** El atacante se posiciona entre dos dispositivos para interceptar comunicaciones encriptadas.

**Contramedidas Principales:**
- **Certificados SSL:** Verificar autenticidad
- **Certificate Pinning:** Fijar certificados válidos
- **VPN:** Túneles seguros
- **Validación Certificados:** Verificar cadena de confianza

### Tarjeta 10: Envenenamiento de Tabla ARP

**Capa OSI:** Capa 2 (Enlace de Datos)
**Tipo de Ataque:** ARP Poisoning
**Explicación:** El atacante manipula la tabla ARP para redirigir tráfico a su dispositivo.

**Contramedidas Principales:**
- **ARP Monitoring:** Monitorear cambios en tabla ARP
- **Static ARP:** Configurar entradas ARP estáticas
- **VLANs:** Segmentar redes
- **Port Security:** Restringir dispositivos por puerto

### Tarjeta 11: Escaneo de Puertos

**Capa OSI:** Capa 4 (Transporte)
**Tipo de Ataque:** Port Scanning
**Explicación:** El atacante prueba múltiples puertos para identificar servicios vulnerables.

**Contramedidas Principales:**
- **Firewalls:** Bloquear puertos innecesarios
- **IDS/IPS:** Detectar escaneos
- **Honeypots:** Trampas para atacantes
- **Monitoreo:** Detectar actividad sospechosa

### Tarjeta 12: Ataque de Fuerza Bruta

**Capa OSI:** Capa 7 (Aplicación)
**Tipo de Ataque:** Brute Force Attack
**Explicación:** El atacante prueba múltiples combinaciones de credenciales para acceder a cuentas.

**Contramedidas Principales:**
- **Rate Limiting:** Limitar intentos de login
- **MFA:** Autenticación de múltiples factores
- **Account Lockout:** Bloquear cuentas después de intentos fallidos
- **CAPTCHA:** Verificar que es un humano

## Criterios de Evaluación

### Excelente (90-100%):
- Identificación correcta de capa OSI para todas las tarjetas
- Contramedidas específicas y efectivas
- Comprensión profunda de los ataques
- Explicación clara de la relación entre capa y ataque

### Bueno (80-89%):
- Identificación correcta de la mayoría de capas OSI
- Contramedidas apropiadas
- Comprensión básica de los ataques
- Algunas explicaciones de la relación capa-ataque

### Satisfactorio (70-79%):
- Identificación parcial de capas OSI
- Contramedidas básicas
- Comprensión superficial de ataques
- Pocas explicaciones de relaciones

### Necesita Mejora (<70%):
- Múltiples errores en identificación de capas
- Contramedidas inadecuadas o ausentes
- Comprensión limitada de ataques
- Sin explicaciones de relaciones

## Puntos de Discusión para el Debate

### 1. Defensa en Profundidad:
- ¿Cómo se complementan las contramedidas de diferentes capas?
- ¿Qué capas son más críticas para proteger?

### 2. Priorización de Contramedidas:
- ¿Qué contramedidas son más efectivas por costo-beneficio?
- ¿Cómo balancear seguridad y usabilidad?

### 3. Tendencias Emergentes:
- ¿Cómo evolucionan estos ataques con nuevas tecnologías?
- ¿Qué nuevos tipos de ataques están surgiendo?

### 4. Contexto Organizacional:
- ¿Cómo adaptar estas contramedidas a diferentes tipos de organizaciones?
- ¿Qué consideraciones especiales hay para infraestructura crítica?

## Notas para Docentes

### Variaciones Aceptables:
- Algunos ataques pueden manifestarse en múltiples capas
- Las contramedidas pueden variar según el contexto
- Los estudiantes pueden proponer contramedidas adicionales válidas

### Puntos Clave a Evaluar:
- Comprensión del modelo OSI
- Capacidad de análisis de amenazas
- Pensamiento crítico en contramedidas
- Trabajo colaborativo en grupo

### Adaptaciones Posibles:
- Modificar escenarios según el contexto local
- Agregar tarjetas específicas de la industria
- Incluir casos de estudio reales
- Personalizar según nivel de experiencia de los estudiantes
