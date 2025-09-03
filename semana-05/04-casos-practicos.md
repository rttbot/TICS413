# Casos Prácticos de Análisis de Ataques

## Introducción

Este documento presenta casos prácticos reales para que los estudiantes apliquen los conocimientos adquiridos sobre tipos de ataques, identificación de vulnerabilidades y contramedidas apropiadas.

## Caso 1: Ataque a Empresa de E-commerce

### Escenario

```
┌─────────────────────────────────────────────────────────────┐
│                    CASO 1: E-COMMERCE                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  EMPRESA: TechStore.cl                                     │
│  INDUSTRIA: Comercio electrónico                           │
│  INFRAESTRUCTURA:                                           │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Sitio web con transacciones                       │   │
│  │ • Base de datos de 50,000 clientes                  │   │
│  │ • Red WiFi para empleados                           │   │
│  │ • Sistema de pagos integrado                        │   │
│  │ • Almacén de datos de tarjetas                      │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Incidente Reportado

**Fecha:** 15 de marzo de 2025  
**Hora:** 02:30 AM  
**Descripción:** El equipo de seguridad detectó actividad sospechosa en el sistema de pagos.

### Evidencia Recolectada

```
┌─────────────────────────────────────────────────────────────┐
│                    EVIDENCIA DEL INCIDENTE                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  LOGS DE APLICACIÓN:                                       │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ 02:30:15 - SQL Query: SELECT * FROM users           │   │
│  │ 02:30:16 - SQL Query: SELECT * FROM credit_cards    │   │
│  │ 02:30:17 - SQL Query: SELECT * FROM orders          │   │
│  │ 02:30:18 - Login attempt: admin' OR '1'='1          │   │
│  │ 02:30:19 - Database connection from 192.168.1.100   │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  LOGS DE RED:                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ 02:29:45 - New WiFi connection: "TechStore_Guest"   │   │
│  │ 02:30:00 - Port scan detected on 192.168.1.100      │   │
│  │ 02:30:10 - Multiple SYN packets from 192.168.1.100   │   │
│  │ 02:30:12 - ARP table modification detected           │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  LOGS DE SEGURIDAD:                                        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ 02:30:20 - WAF alert: SQL Injection attempt         │   │
│  │ 02:30:21 - IDS alert: Unauthorized database access  │   │
│  │ 02:30:22 - Firewall: Blocked suspicious IP            │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Análisis Requerido

**Preguntas para el estudiante:**

1. **Identificación de Ataques:**
   - ¿Qué tipos de ataques se pueden identificar en la evidencia?
   - ¿En qué capas del modelo OSI ocurrieron estos ataques?

2. **Análisis de Vulnerabilidades:**
   - ¿Qué vulnerabilidades permitieron estos ataques?
   - ¿Cómo pudo el atacante acceder a la red WiFi?

3. **Contramedidas:**
   - ¿Qué contramedidas deberían implementarse inmediatamente?
   - ¿Qué controles preventivos faltan?

4. **Respuesta al Incidente:**
   - ¿Cuál sería el plan de respuesta inmediata?
   - ¿Qué pasos seguirías para contener el incidente?

### Respuesta Esperada

```
┌─────────────────────────────────────────────────────────────┐
│                    ANÁLISIS DEL CASO                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ATAQUES IDENTIFICADOS:                                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ 1. Evil Twin Attack (Capa 2)                        │   │
│  │    - Punto de acceso falso "TechStore_Guest"       │   │
│  │                                                     │   │
│  │ 2. ARP Poisoning (Capa 2)                           │   │
│  │    - Modificación de tabla ARP                     │   │
│  │                                                     │   │
│  │ 3. SYN Flood (Capa 4)                               │   │
│  │    - Múltiples paquetes SYN                         │   │
│  │                                                     │   │
│  │ 4. SQL Injection (Capa 7)                           │   │
│  │    - Inyección en login: admin' OR '1'='1           │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CONTRAMEDIDAS INMEDIATAS:                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Bloquear IP 192.168.1.100                         │   │
│  │ • Desconectar punto de acceso falso                 │   │
│  │ • Activar modo de emergencia en WAF                │   │
│  │ • Revisar integridad de base de datos               │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Caso 2: Incidente en Hospital

### Escenario

```
┌─────────────────────────────────────────────────────────────┐
│                    CASO 2: HOSPITAL                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  INSTITUCIÓN: Hospital Regional San José                   │
│  INFRAESTRUCTURA:                                           │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Red WiFi separada por departamentos               │   │
│  │ • Sistemas médicos críticos                         │   │
│  │ • Base de datos de pacientes (HIPAA)                │   │
│  │ • Dispositivos IoT médicos                           │   │
│  │ • Acceso remoto para médicos                         │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Incidente Reportado

**Fecha:** 22 de marzo de 2025  
**Hora:** 11:15 AM  
**Descripción:** Los sistemas de monitoreo de pacientes en la UCI comenzaron a fallar.

### Evidencia Recolectada

```
┌─────────────────────────────────────────────────────────────┐
│                    EVIDENCIA DEL INCIDENTE                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  LOGS DE SISTEMAS MÉDICOS:                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ 11:15:00 - Monitor_ICU_01: Connection lost          │   │
│  │ 11:15:02 - Monitor_ICU_02: Connection lost          │   │
│  │ 11:15:05 - Monitor_ICU_03: Connection lost          │   │
│  │ 11:15:10 - All ICU monitors: Offline                │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  LOGS DE RED WIFI:                                         │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ 11:14:45 - Deauthentication frames detected         │   │
│  │ 11:14:50 - Multiple devices disconnected            │   │
│  │ 11:14:55 - New AP detected: "Hospital_Guest"        │   │
│  │ 11:15:00 - Jamming signal detected on 2.4 GHz      │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  LOGS DE SEGURIDAD:                                        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ 11:15:05 - WIDS alert: Rogue AP detected            │   │
│  │ 11:15:08 - Physical security: Unauthorized access   │   │
│  │ 11:15:10 - Emergency mode activated                 │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Análisis Requerido

**Preguntas para el estudiante:**

1. **Identificación de Ataques:**
   - ¿Qué tipos de ataques están ocurriendo?
   - ¿Por qué son críticos en un entorno hospitalario?

2. **Análisis de Impacto:**
   - ¿Cuál es el impacto en la seguridad de los pacientes?
   - ¿Qué sistemas críticos están afectados?

3. **Contramedidas Específicas:**
   - ¿Qué contramedidas son apropiadas para un hospital?
   - ¿Cómo proteger los sistemas médicos críticos?

4. **Respuesta de Emergencia:**
   - ¿Cuál es el plan de respuesta inmediata?
   - ¿Cómo asegurar la continuidad de servicios críticos?

### Respuesta Esperada

```
┌─────────────────────────────────────────────────────────────┐
│                    ANÁLISIS DEL CASO                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ATAQUES IDENTIFICADOS:                                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ 1. WiFi Jamming (Capa 1)                           │   │
│  │    - Bloqueo de señales en 2.4 GHz                  │   │
│  │                                                     │   │
│  │ 2. Deauthentication Attack (Capa 2)                │   │
│  │    - Desconexión forzada de dispositivos            │   │
│  │                                                     │   │
│  │ 3. Rogue AP (Capa 2)                                │   │
│  │    - Punto de acceso malicioso                      │   │
│  │                                                     │   │
│  │ 4. Physical Access (Capa 1)                         │   │
│  │    - Acceso físico no autorizado                    │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CONTRAMEDIDAS CRÍTICAS:                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Activar modo de emergencia                        │   │
│  │ • Usar sistemas de respaldo cableados              │   │
│  │ • Aislar redes críticas                             │   │
│  │ • Activar protocolos de emergencia médica           │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Caso 3: Ataque a Universidad

### Escenario

```
┌─────────────────────────────────────────────────────────────┐
│                    CASO 3: UNIVERSIDAD                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  INSTITUCIÓN: Universidad Tecnológica del Sur              │
│  INFRAESTRUCTURA:                                           │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Red WiFi pública para estudiantes                 │   │
│  │ • Red WiFi privada para administración              │   │
│  │ • Laboratorios de computación                       │   │
│  │ • Biblioteca digital                                 │   │
│  │ • Sistema de gestión académica                      │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Incidente Reportado

**Fecha:** 28 de marzo de 2025  
**Hora:** 09:30 AM  
**Descripción:** Estudiantes reportan que no pueden acceder a la red WiFi y el sistema de gestión académica está caído.

### Evidencia Recolectada

```
┌─────────────────────────────────────────────────────────────┐
│                    EVIDENCIA DEL INCIDENTE                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  LOGS DE RED WIFI:                                         │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ 09:25:00 - Beacon flood detected                    │   │
│  │ 09:25:05 - Multiple SSIDs: "UTS_WiFi_1", "UTS_WiFi_2" │   │
│  │ 09:25:10 - Channel congestion on all bands         │   │
│  │ 09:25:15 - Authentication server overload          │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  LOGS DE SISTEMA ACADÉMICO:                                │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ 09:30:00 - DDoS attack detected                     │   │
│  │ 09:30:05 - Database connection pool exhausted       │   │
│  │ 09:30:10 - Web server: 503 Service Unavailable     │   │
│  │ 09:30:15 - Load balancer: Overloaded                 │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  LOGS DE SEGURIDAD:                                        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ 09:25:20 - WIDS: Beacon flooding attack             │   │
│  │ 09:30:00 - IDS: DDoS attack from multiple IPs      │   │
│  │ 09:30:10 - Firewall: Rate limiting activated        │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Análisis Requerido

**Preguntas para el estudiante:**

1. **Identificación de Ataques:**
   - ¿Qué tipos de ataques están ocurriendo simultáneamente?
   - ¿Cómo se relacionan estos ataques?

2. **Análisis de Vulnerabilidades:**
   - ¿Qué vulnerabilidades permiten estos ataques?
   - ¿Por qué es vulnerable una red universitaria?

3. **Contramedidas Apropiadas:**
   - ¿Qué contramedidas son apropiadas para una universidad?
   - ¿Cómo balancear seguridad y accesibilidad?

4. **Plan de Recuperación:**
   - ¿Cómo restaurar servicios críticos?
   - ¿Qué medidas preventivas implementar?

### Respuesta Esperada

```
┌─────────────────────────────────────────────────────────────┐
│                    ANÁLISIS DEL CASO                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ATAQUES IDENTIFICADOS:                                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ 1. Beacon Flooding (Capa 2)                         │   │
│  │    - Sobreflujo de beacons WiFi                     │   │
│  │                                                     │   │
│  │ 2. Channel Congestion (Capa 1)                      │   │
│  │    - Interferencia en todas las bandas              │   │
│  │                                                     │   │
│  │ 3. DDoS Attack (Capa 3)                             │   │
│  │    - Ataque distribuido contra servidores           │   │
│  │                                                     │   │
│  │ 4. Authentication Server Attack (Capa 5)           │   │
│  │    - Sobreflujo del servidor de autenticación       │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CONTRAMEDIDAS UNIVERSITARIAS:                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Segmentar redes por tipo de usuario              │   │
│  │ • Implementar rate limiting                         │   │
│  │ • Usar DDoS protection services                     │   │
│  │ • Educar estudiantes sobre seguridad               │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Caso 4: Incidente Crítico en Infraestructura de Telecomunicaciones

### Escenario Complejo

```
┌─────────────────────────────────────────────────────────────┐
│                CASO 4: INFRAESTRUCTURA CRÍTICA              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  EMPRESA: TelecomLatina S.A.                              │
│  INDUSTRIA: Telecomunicaciones (ISP Principal)             │
│  UBICACIÓN: Santiago, Chile                               │
│  INFRAESTRUCTURA CRÍTICA:                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Red de fibra óptica nacional                      │   │
│  │ • Centros de datos distribuidos                     │   │
│  │ • Servicios de Internet para 2M+ usuarios          │   │
│  │ • Conexiones internacionales (Asia, Norteamérica)  │   │
│  │ • Servicios críticos: bancos, hospitales, gobierno  │   │
│  │ • Red WiFi corporativa y puntos de acceso público  │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CONTEXTO GEOPOLÍTICO:                                     │
│  • Tensiones comerciales Chile-China                      │   │
│  • Aumento de ataques a infraestructura crítica          │   │
│  • Nueva regulación de ciberseguridad (Ley 21.500)       │   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Cronología del Incidente (3 Días)

#### DÍA 1 - DETECCIÓN INICIAL (15 de Abril, 2025)

**08:30 AM - Email Interno:**
```
De: Carlos Mendoza - Director de Operaciones
Para: Equipo de Seguridad
Asunto: Problemas de conectividad en centro de datos norte

Hemos detectado interrupciones intermitentes en el centro de datos 
de Antofagasta. Los monitores muestran:
- Latencia aumentada en 300%
- Pérdida de paquetes del 15%
- Múltiples reconexiones de routers
- Alertas de temperatura en racks críticos

¿Alguien puede revisar los logs de seguridad?
```

**10:15 AM - Reporte de Seguridad:**
```
┌─────────────────────────────────────────────────────────────┐
│                    REPORTE DE SEGURIDAD                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ANÁLISIS PRELIMINAR:                                      │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Múltiples conexiones SSH desde IPs chinas        │   │
│  │ • Intentos de fuerza bruta en routers principales  │   │
│  │ • Modificación de tablas de enrutamiento           │   │
│  │ • Nuevos puntos de acceso WiFi no autorizados       │   │
│  │ • Interferencia en frecuencias de radio             │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CLASIFICACIÓN: ATAQUE COORDINADO MULTI-CAPA              │
│  IMPACTO: CRÍTICO - INFRAESTRUCTURA NACIONAL             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### DÍA 2 - ESCALACIÓN (16 de Abril, 2025)

**09:00 AM - Comunicado de Prensa:**
```
TELECOMLATINA S.A. - COMUNICADO OFICIAL

Santiago, 16 de abril de 2025

TelecomLatina S.A. informa que desde la madrugada de hoy hemos 
experimentado interrupciones significativas en nuestros servicios 
de Internet en las regiones del norte del país.

Nuestros equipos técnicos están trabajando activamente para 
restaurar la conectividad completa. Estimamos que el 40% de 
nuestros usuarios se han visto afectados.

Pedimos disculpas por las molestias y mantendremos informados 
a nuestros clientes sobre el progreso de la restauración.

Contacto: prensa@telecomlatina.cl
```

**11:30 AM - Alertas de Gobierno:**
```
┌─────────────────────────────────────────────────────────────┐
│                ALERTA CSIRT CHILE                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  FECHA: 16 de Abril, 2025                                 │
│  NIVEL: CRÍTICO                                            │
│                                                             │
│  SE HA DETECTADO UN ATAQUE COORDINADO CONTRA               │
│  INFRAESTRUCTURA CRÍTICA DE TELECOMUNICACIONES             │
│                                                             │
│  CARACTERÍSTICAS:                                          │
│  • Ataques simultáneos en múltiples ISP                   │
│  • Técnicas de interferencia física                       │
│  • Compromiso de equipos de red                            │
│  • Posible origen extranjero                              │
│                                                             │
│  RECOMENDACIONES:                                          │
│  • Activar protocolos de emergencia                       │
│  • Revisar configuraciones de seguridad                   │
│  • Coordinar con autoridades                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### DÍA 3 - CRISIS TOTAL (17 de Abril, 2025)

**07:00 AM - Fallo Masivo:**
```
┌─────────────────────────────────────────────────────────────┐
│                SITUACIÓN CRÍTICA                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ESTADO ACTUAL:                                            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • 80% de usuarios sin Internet                      │   │
│  │ • Centros de datos principales offline              │   │
│  │ • Servicios bancarios interrumpidos                 │   │
│  │ • Hospitales sin conectividad crítica               │   │
│  │ • Gobierno declarando estado de emergencia          │   │
│  │ • Competidores también afectados                    │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ATAQUES IDENTIFICADOS:                                   │
│  • Jamming de señales WiFi y radio                      │
│  • ARP Poisoning masivo                                   │
│  • DDoS distribuido                                       │
│  • Compromiso de routers principales                     │
│  • Ataques físicos a fibra óptica                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Documentos de Evidencia

#### Documento 1: Logs de Red Críticos
```
┌─────────────────────────────────────────────────────────────┐
│                    LOGS DE RED - DÍA 1                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  08:30:15 - Router_Antofagasta_01: ARP table overflow      │
│  08:30:16 - Router_Antofagasta_01: Multiple MAC addresses │
│  08:30:17 - Router_Antofagasta_01: Routing table modified  │
│  08:30:18 - Router_Antofagasta_01: Temperature warning     │
│  08:30:19 - Router_Antofagasta_01: CPU usage 95%           │
│                                                             │
│  08:31:00 - WiFi_AP_01: Beacon flood detected             │
│  08:31:01 - WiFi_AP_01: Deauthentication frames           │
│  08:31:02 - WiFi_AP_01: Rogue AP detected                  │
│  08:31:03 - WiFi_AP_01: Channel congestion                │
│                                                             │
│  08:32:00 - Firewall_01: SYN flood from 203.45.67.89      │
│  08:32:01 - Firewall_01: Port scan detected               │
│  08:32:02 - Firewall_01: DDoS attack in progress          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### Documento 2: Reporte de Inteligencia
```
┌─────────────────────────────────────────────────────────────┐
│                REPORTE DE INTELIGENCIA                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ANÁLISIS DE AMENAZAS:                                     │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ GRUPO SOSPECHOSO: APT-41 (China)                   │   │
│  │ TÉCNICAS IDENTIFICADAS:                             │   │
│  │ • Interferencia física de señales                   │   │
│  │ • Compromiso de equipos de red                      │   │
│  │ • Ataques coordinados multi-capa                     │   │
│  │ • Objetivo: Infraestructura crítica                  │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CONTEXTO GEOPOLÍTICO:                                     │
│  • Tensiones comerciales Chile-China                    │   │
│  • Nuevas regulaciones de telecomunicaciones            │   │
│  • Interés chino en infraestructura latinoamericana      │   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### Documento 3: Comunicaciones Internas
```
┌─────────────────────────────────────────────────────────────┐
│                EMAILS INTERNOS                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  De: Ana Silva - CISO                                     │
│  Para: Equipo Ejecutivo                                   │
│  Asunto: URGENTE - Ataque coordinado detectado            │
│  Fecha: 16 de Abril, 2025 - 10:00 AM                     │
│                                                             │
│  Equipo,                                                  │
│                                                             │
│  Confirmamos que estamos bajo un ataque coordinado       │
│  contra nuestra infraestructura crítica. Los atacantes   │
│  están usando técnicas de interferencia física y          │
│  compromiso de equipos de red simultáneamente.            │
│                                                             │
│  RECOMENDACIONES INMEDIATAS:                              │
│  • Activar modo de emergencia                            │
│  • Contactar autoridades                                  │
│  • Preparar comunicado público                           │
│  • Coordinar con otros ISP                               │
│                                                             │
│  Ana                                                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Roles del Equipo de Respuesta

```
┌─────────────────────────────────────────────────────────────┐
│                EQUIPO DE RESPUESTA                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ROLES ASIGNADOS:                                          │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ 1. DIRECTOR DE OPERACIONES                         │   │
│  │    • Mantener servicios críticos                     │   │
│  │    • Coordinar equipos técnicos                     │   │
│  │    • Minimizar impacto en usuarios                  │   │
│  │                                                     │   │
│  │ 2. CHIEF INFORMATION SECURITY OFFICER (CISO)        │   │
│  │    • Análisis forense del incidente                 │   │
│  │    • Coordinación con autoridades                   │   │
│  │    • Plan de respuesta de seguridad                 │   │
│  │                                                     │   │
│  │ 3. DIRECTOR DE COMUNICACIONES                       │   │
│  │    • Gestión de crisis mediática                     │   │
│  │    • Comunicación con stakeholders                   │   │
│  │    • Relaciones públicas                             │   │
│  │                                                     │   │
│  │ 4. DIRECTOR LEGAL                                    │   │
│  │    • Cumplimiento regulatorio                        │   │
│  │    • Responsabilidades legales                       │   │
│  │    • Coordinación con autoridades                   │   │
│  │                                                     │   │
│  │ 5. DIRECTOR DE TECNOLOGÍA                           │   │
│  │    • Análisis técnico detallado                      │   │
│  │    • Plan de recuperación                            │   │
│  │    • Coordinación con proveedores                   │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Análisis Requerido por Rol

#### Para el Director de Operaciones:
1. **Gestión de Crisis Operacional:**
   - ¿Cómo mantener servicios críticos funcionando?
   - ¿Qué prioridades establecer para la restauración?
   - ¿Cómo coordinar con otros ISP afectados?

2. **Análisis de Impacto:**
   - ¿Cuál es el impacto económico del incidente?
   - ¿Qué servicios críticos están en riesgo?
   - ¿Cómo minimizar el impacto en usuarios?

#### Para el CISO:
1. **Análisis Forense:**
   - ¿Qué tipos de ataques están ocurriendo?
   - ¿En qué capas OSI se manifiestan?
   - ¿Cuál es el origen y motivación del ataque?

2. **Respuesta de Seguridad:**
   - ¿Qué contramedidas implementar inmediatamente?
   - ¿Cómo coordinar con autoridades?
   - ¿Qué medidas preventivas faltan?

#### Para el Director de Comunicaciones:
1. **Gestión de Crisis:**
   - ¿Qué comunicar al público?
   - ¿Cómo manejar la prensa?
   - ¿Qué información compartir con stakeholders?

2. **Estrategia de Comunicación:**
   - ¿Cómo mantener la confianza de los usuarios?
   - ¿Qué mensajes transmitir a las autoridades?
   - ¿Cómo coordinar con otros ISP?

#### Para el Director Legal:
1. **Cumplimiento Regulatorio:**
   - ¿Qué obligaciones legales tenemos?
   - ¿Cómo cumplir con la Ley 21.500?
   - ¿Qué responsabilidades tenemos con usuarios?

2. **Coordinación Legal:**
   - ¿Cómo trabajar con autoridades?
   - ¿Qué información compartir legalmente?
   - ¿Qué acciones legales tomar?

#### Para el Director de Tecnología:
1. **Análisis Técnico:**
   - ¿Qué vulnerabilidades fueron explotadas?
   - ¿Cómo restaurar la infraestructura?
   - ¿Qué mejoras técnicas implementar?

2. **Plan de Recuperación:**
   - ¿Cuál es el timeline de restauración?
   - ¿Qué recursos técnicos necesitamos?
   - ¿Cómo prevenir futuros ataques?

### Respuesta Integrada Esperada

```
┌─────────────────────────────────────────────────────────────┐
│                PLAN DE RESPUESTA INTEGRADO                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  FASE 1: CONTENCIÓN INMEDIATA (0-2 horas)                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ OPERACIONES:                                        │   │
│  │ • Activar modo de emergencia                        │   │
│  │ • Priorizar servicios críticos                       │   │
│  │ • Coordinar con otros ISP                           │   │
│  │                                                     │   │
│  │ SEGURIDAD:                                          │   │
│  │ • Bloquear IPs maliciosas                           │   │
│  │ • Aislar equipos comprometidos                      │   │
│  │ • Contactar autoridades                             │   │
│  │                                                     │   │
│  │ COMUNICACIONES:                                      │   │
│  │ • Comunicado público inmediato                      │   │
│  │ • Notificación a stakeholders                       │   │
│  │ • Coordinación con prensa                           │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  FASE 2: ESTABILIZACIÓN (2-24 horas)                       │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ OPERACIONES:                                        │   │
│  │ • Restaurar servicios prioritarios                   │   │
│  │ • Implementar redundancias                          │   │
│  │ • Monitoreo continuo                                │   │
│  │                                                     │   │
│  │ SEGURIDAD:                                          │   │
│  │ • Análisis forense completo                         │   │
│  │ • Implementar contramedidas                         │   │
│  │ • Coordinar con CSIRT Chile                         │   │
│  │                                                     │   │
│  │ COMUNICACIONES:                                      │   │
│  │ • Actualizaciones regulares                          │   │
│  │ • Gestión de expectativas                            │   │
│  │ • Coordinación con gobierno                          │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  FASE 3: RECUPERACIÓN (24-72 horas)                        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ OPERACIONES:                                        │   │
│  │ • Restauración completa                              │   │
│  │ • Implementar mejoras                                │   │
│  │ • Monitoreo reforzado                               │   │
│  │                                                     │   │
│  │ SEGURIDAD:                                          │   │
│  │ • Auditoría de seguridad                            │   │
│  │ • Implementar lecciones aprendidas                  │   │
│  │ • Plan de resiliencia                                │   │
│  │                                                     │   │
│  │ COMUNICACIONES:                                      │   │
│  │ • Reporte final público                              │   │
│  │ • Restauración de confianza                          │   │
│  │ • Plan de mejora                                     │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Evaluación del Caso Integrador

#### Criterios de Evaluación Avanzados:

| Criterio | Puntuación | Descripción |
|----------|------------|-------------|
| **Análisis Multi-Perspectiva** | 25% | Comprensión de diferentes roles y responsabilidades |
| **Coordinación Interdisciplinaria** | 20% | Capacidad de trabajar entre diferentes áreas |
| **Gestión de Crisis** | 20% | Manejo de situaciones de alta presión |
| **Análisis Técnico Profundo** | 15% | Comprensión técnica de ataques por capas OSI |
| **Comunicación Estratégica** | 10% | Habilidad para comunicar efectivamente |
| **Cumplimiento Legal** | 10% | Entendimiento de obligaciones regulatorias |

#### Rúbrica de Evaluación Integrada:

```
┌─────────────────────────────────────────────────────────────┐
│                RÚBRICA INTEGRADA                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  EXCELENTE (90-100%):                                      │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Análisis completo desde todas las perspectivas    │   │
│  │ • Plan de respuesta integrado y realista            │   │
│  │ • Coordinación efectiva entre roles                  │   │
│  │ • Comprensión profunda de ataques por capas OSI     │   │
│  │ • Gestión de crisis profesional                      │   │
│  │ • Comunicación estratégica efectiva                  │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  BUENO (80-89%):                                           │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Análisis desde múltiples perspectivas             │   │
│  │ • Plan de respuesta estructurado                     │   │
│  │ • Coordinación básica entre roles                    │   │
│  │ • Comprensión de ataques principales                 │   │
│  │ • Gestión de crisis adecuada                         │   │
│  │ • Comunicación apropiada                             │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  SATISFACTORIO (70-79%):                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Análisis desde algunas perspectivas               │   │
│  │ • Plan de respuesta básico                          │   │
│  │ • Coordinación limitada                              │   │
│  │ • Comprensión parcial de ataques                     │   │
│  │ • Gestión de crisis básica                          │   │
│  │ • Comunicación limitada                              │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Conclusiones del Caso Integrador

Este caso integrador permite a los estudiantes:

1. **Aplicar conocimiento técnico** en un contexto realista y complejo
2. **Desarrollar habilidades de gestión** de crisis y comunicación
3. **Entender la interconexión** entre diferentes áreas de una organización
4. **Practicar coordinación** entre múltiples stakeholders
5. **Analizar ataques complejos** que involucran múltiples capas OSI
6. **Desarrollar pensamiento estratégico** en situaciones de crisis

El caso fomenta el aprendizaje colaborativo y prepara a los estudiantes para situaciones reales de ciberseguridad en infraestructura crítica.

## Ejercicio de Aplicación

### Matriz de Análisis

```
┌─────────────────────────────────────────────────────────────┐
│                    MATRIZ DE ANÁLISIS                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CASO          ATAQUES PRINCIPALES    CONTRAMEDIDAS        │
│  ┌─────────────┐ ┌─────────────────┐ ┌─────────────────┐   │
│  │             │ │                 │ │                 │   │
│  │ E-commerce  │ │ • Evil Twin     │ │ • WAF           │   │
│  │             │ │ • SQL Injection │ │ • VLANs         │   │
│  │             │ │ • ARP Poisoning │ │ • 802.1X       │   │
│  │             │ │ • SYN Flood     │ │ • IDS/IPS       │   │
│  │             │ │                 │ │                 │   │
│  └─────────────┘ └─────────────────┘ └─────────────────┘   │
│                                                             │
│  ┌─────────────┐ ┌─────────────────┐ ┌─────────────────┐   │
│  │             │ │                 │ │                 │   │
│  │ Hospital    │ │ • WiFi Jamming  │ │ • Redes críticas│   │
│  │             │ │ • Deauth Attack │ │   aisladas      │   │
│  │             │ │ • Rogue AP      │ │ • Backup cableado│   │
│  │             │ │ • Physical      │ │ • WIDS/WIPS     │   │
│  │             │ │   Access        │ │                 │   │
│  └─────────────┘ └─────────────────┘ └─────────────────┘   │
│                                                             │
│  ┌─────────────┐ ┌─────────────────┐ ┌─────────────────┐   │
│  │             │ │                 │ │                 │   │
│  │ Universidad │ │ • Beacon Flood  │ │ • Segmentación  │   │
│  │             │ │ • DDoS Attack   │ │ • Rate Limiting │   │
│  │             │ │ • Channel Cong. │ │ • Educación     │   │
│  │             │ │ • Auth Server    │ │ • Monitoreo     │   │
│  │             │ │   Attack        │ │                 │   │
│  └─────────────┘ └─────────────────┘ └─────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Evaluación de Casos

### Criterios de Evaluación

| Criterio | Puntuación | Descripción |
|----------|------------|-------------|
| **Identificación de Ataques** | 30% | Correcta clasificación por capa OSI |
| **Análisis de Vulnerabilidades** | 25% | Comprensión de causas raíz |
| **Contramedidas Apropiadas** | 25% | Soluciones efectivas y realistas |
| **Respuesta al Incidente** | 20% | Plan de acción inmediato |

### Rúbrica de Evaluación

```
┌─────────────────────────────────────────────────────────────┐
│                    RÚBRICA DE EVALUACIÓN                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  EXCELENTE (90-100%):                                       │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Identificación completa de todos los ataques      │   │
│  │ • Análisis profundo de vulnerabilidades             │   │
│  │ • Contramedidas específicas y efectivas             │   │
│  │ • Plan de respuesta detallado y realista            │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  BUENO (80-89%):                                            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Identificación de ataques principales             │   │
│  │ • Análisis básico de vulnerabilidades              │   │
│  │ • Contramedidas apropiadas                          │   │
│  │ • Plan de respuesta básico                          │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  SATISFACTORIO (70-79%):                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Identificación parcial de ataques                 │   │
│  │ • Análisis superficial                              │   │
│  │ • Contramedidas básicas                             │   │
│  │ • Plan de respuesta limitado                        │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Conclusiones

Los casos prácticos permiten a los estudiantes:

1. **Aplicar conocimiento teórico** a situaciones reales
2. **Desarrollar pensamiento analítico** sobre seguridad
3. **Entender la complejidad** de incidentes reales
4. **Practicar respuesta a incidentes** de manera estructurada
5. **Mejorar habilidades de comunicación** técnica

Estos casos fomentan el aprendizaje activo y la preparación para situaciones reales de seguridad de redes.

