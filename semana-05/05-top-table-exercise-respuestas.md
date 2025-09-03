# Respuestas del Top Table Exercise: Simulación de Seguridad en Redes

## Objetivo

Este documento contiene las respuestas correctas para el ejercicio de tarjetas de amenazas, permitiendo a los docentes evaluar las respuestas de los estudiantes y proporcionar retroalimentación adecuada.

## Estructura del Documento

1. **Tabla de Clasificación Grupal Completa** - Respuestas principales
2. **Resumen por Tarjeta** - Análisis detallado de cada amenaza
3. **Aplicación a Casos Prácticos** - Conexión con escenarios reales
4. **Criterios de Evaluación** - Rúbrica para calificar
5. **Puntos de Discusión** - Temas para debate en clase

---

## 1. Tabla de Clasificación Grupal Completa

```
┌─────────────────────────────────────────────────────────────┐
│                TABLA DE CLASIFICACIÓN GRUPAL                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  TARJETA │ CAPA OSI │ TIPO DE ATAQUE │ CONTRAMEDIDAS        │ EJEMPLO SIMILAR │ TARJETA RISKIO │
│  ┌───────┼─────────┼───────────────┼─────────────────────┼─────────────────┼───────────────┐ │
│  │   1   │ Capa 2  │ Interceptación│ • WPA3/WPA2          │ Packet Sniffing │ 8 - Seguridad │ │
│  │       │ Enlace  │ WiFi          │ • Monitoreo de red   │ en cafés        │ física        │ │
│  │       │ Datos   │               │ • WIDS/WIPS          │ públicos         │               │ │
│  │       │         │               │ • Segmentación VLAN │                 │               │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┼─────────────────┼───────────────┤ │
│  │   2   │ Capa 2  │ Evil Twin     │ • Verificar SSID     │ Red WiFi falsa  │ K - Firewalls │ │
│  │       │ Enlace  │ Attack        │ • Certificados SSL   │ "Starbucks_Free"│ perimetrales  │ │
│  │       │ Datos   │               │ • VPN obligatorio    │ en aeropuerto   │               │ │
│  │       │         │               │ • WIDS/WIPS          │                 │               │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┼─────────────────┼───────────────┤ │
│  │   3   │ Capa 4  │ SYN Flood     │ • SYN Cookies        │ Ataque a       │ 9 - Monitoreo │ │
│  │       │ Transp. │ (DDoS)        │ • Rate Limiting      │ servidor web    │ de red        │ │
│  │       │         │               │ • Firewalls          │ de banco        │               │ │
│  │       │         │               │ • DDoS Protection    │                 │               │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┼─────────────────┼───────────────┤ │
│  │   4   │ Capa 5  │ Session       │ • Timeouts           │ Robo de        │ 4 - Control de │ │
│  │       │ Sesión  │ Hijacking     │ • Regeneración IDs   │ sesión bancaria│ acceso        │ │
│  │       │         │               │ • HTTPS obligatorio │ en cibercafé   │               │ │
│  │       │         │               │ • Logout automático  │                 │               │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┼─────────────────┼───────────────┤ │
│  │   5   │ Capa 7  │ SQL Injection │ • Prepared Statements│ Inyección en   │ 3 - Configura-│ │
│  │       │ Aplic.  │               │ • Input Validation   │ formulario de   │ ción segura   │ │
│  │       │         │               │ • WAF               │ login           │               │ │
│  │       │         │               │ • Least Privilege    │                 │               │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┼─────────────────┼───────────────┤ │
│  │   6   │ Capa 3  │ IP Spoofing   │ • BCP38              │ Falsificación   │ K - Firewalls │ │
│  │       │ Red     │               │ • Egress Filtering   │ IP en ataques   │ perimetrales  │ │
│  │       │         │               │ • Firewalls          │ DDoS            │               │ │
│  │       │         │               │ • Monitoreo de red   │                 │               │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┼─────────────────┼───────────────┤ │
│  │   7   │ Capa 1  │ WiFi Jamming │ • Redundancia        │ Interferencia   │ J - Respaldo  │ │
│  │       │ Física  │ (Multi-Capa) │ • Backup cableado    │ en hospital     │ de datos      │ │
│  │       │ + Capa 2│               │ • Detección RF       │ con equipos     │               │ │
│  │       │ Enlace  │               │ • Planes de respaldo │ médicos         │               │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┼─────────────────┼───────────────┤ │
│  │   8   │ Capa 7  │ Malware       │ • Antivirus          │ WannaCry en     │ 5 - Protección│ │
│  │       │ + Capa 3│ Propagation   │ • Segmentación      │ red corporativa │ contra malware│ │
│  │       │ + Capa 4│               │ • Monitoreo          │                 │               │ │
│  │       │         │               │ • Educación usuarios│                 │               │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┼─────────────────┼───────────────┤ │
│  │   9   │ Capa 6  │ Man-in-the-   │ • Certificados SSL   │ Interceptación  │ K - Firewalls │ │
│  │       │ Presen. │ Middle        │ • Certificate Pinning│ en red WiFi     │ perimetrales  │ │
│  │       │         │               │ • VPN                │ pública         │               │ │
│  │       │         │               │ • Validación cert.  │                 │               │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┼─────────────────┼───────────────┤ │
│  │  10   │ Capa 2  │ ARP Poisoning │ • ARP Monitoring     │ Redirección     │ 9 - Monitoreo │ │
│  │       │ Enlace  │               │ • Static ARP         │ tráfico en      │ de red        │ │
│  │       │ Datos   │               │ • VLANs              │ red local       │               │ │
│  │       │         │               │ • Port Security      │                 │               │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┼─────────────────┼───────────────┤ │
│  │  11   │ Capa 4  │ Port Scanning │ • Firewalls          │ Escaneo de      │ 2 - Asegurar  │ │
│  │       │ Transp. │               │ • IDS/IPS            │ puertos en      │ portátiles/PC │ │
│  │       │         │               │ • Honeypots          │ servidor web    │               │ │
│  │       │         │               │ • Monitoreo          │                 │               │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┼─────────────────┼───────────────┤ │
│  │  12   │ Capa 7  │ Brute Force   │ • Rate Limiting      │ Ataque a        │ 4 - Control de │ │
│  │       │ Aplic.  │ Attack        │ • MFA                │ panel admin     │ acceso        │ │
│  │       │         │               │ • Account Lockout    │ web             │               │ │
│  │       │         │               │ • CAPTCHA            │                 │               │ │
│  └───────┴─────────┴───────────────┴─────────────────────┴─────────────────┴───────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Resumen por Tarjeta

### Tarjeta 1: Interceptación WiFi

**ESCENARIO:** Un atacante se conecta a la red WiFi de una empresa y comienza a capturar todo el tráfico de red.

**SÍNTOMAS:**
- Usuario desconocido conectado a la red
- Tráfico de red inusualmente alto
- Dispositivos experimentan lentitud

**ANÁLISIS:**
- **Capa OSI:** Capa 2 (Enlace de Datos)
- **Justificación:** El ataque ocurre en la capa de enlace de datos porque:
  - Los frames WiFi (802.11) se transmiten en esta capa
  - El atacante intercepta frames de datos en el medio físico (aire)
  - La dirección MAC y el control de acceso al medio (CSMA/CA) operan en esta capa
  - Los protocolos WPA/WPA2/WPA3 funcionan en la capa de enlace
- **Ataque:** Packet Sniffing en redes WiFi (El atacante utiliza herramientas como Wireshark para capturar y analizar todo el tráfico de red que pasa por la red WiFi. Este ataque aprovecha que las redes WiFi transmiten datos por el aire, permitiendo interceptar comunicaciones no cifradas como correos electrónicos, contraseñas y datos sensibles. Es especialmente peligroso en redes WiFi públicas o con cifrado débil.)
- **Ejemplo Real:** Interceptación en cafés públicos
- **Caso Similar:** Caso 1 (E-commerce) - Nueva conexión WiFi "TechStore_Guest" detectada
- **Tarjeta RISKIO:** "8 - Seguridad física" (CCTV, acceso controlado)
- **Justificación RISKIO:** La interceptación WiFi se previene con controles físicos como CCTV para detectar intrusos, acceso controlado a salas de servidores, y seguridad del edificio para prevenir acceso no autorizado a la infraestructura de red.
- **Contramedidas Adicionales de Casos:**
  - WIDS/WIPS para detección automática (Caso 1)
  - Monitoreo continuo de usuarios conectados (Caso 1)
  - Segmentación VLAN para aislar tráfico sensible (Caso 1)

### Tarjeta 2: Evil Twin Attack

**ESCENARIO:** Los empleados ven una red WiFi llamada "Empresa_Gratis" junto a la red oficial de la empresa.

**SÍNTOMAS:**
- Nueva red WiFi con nombre similar
- Usuarios se conectan accidentalmente
- Datos sensibles aparecen en lugares extraños

**ANÁLISIS:**
- **Capa OSI:** Capa 2 (Enlace de Datos)
- **Justificación:** El Evil Twin Attack opera en la capa de enlace porque:
  - El atacante crea un punto de acceso falso que emite frames 802.11
  - La autenticación y asociación WiFi ocurren en esta capa
  - El SSID (Service Set Identifier) es un elemento de la capa de enlace
  - Los beacons y probe responses se manejan en esta capa
- **Ataque:** Punto de acceso falso
- **Ejemplo Real:** Red "Starbucks_Free" en aeropuertos
- **Caso Similar:** Caso 1 (E-commerce) - Punto de acceso falso "TechStore_Guest" y Caso 2 (Hospital) - Rogue AP "Hospital_Guest"
- **Tarjeta RISKIO:** "K - Firewalls perimetrales" (prevenir acceso no autorizado)
- **Justificación RISKIO:** Los firewalls perimetrales previenen el acceso no autorizado bloqueando tráfico malicioso, filtrando conexiones a puntos de acceso falsos, y controlando el flujo de datos entre redes internas y externas.
- **Contramedidas Adicionales de Casos:**
  - Verificar SSID oficial (Caso 1, Caso 2)
  - VPN obligatorio para empleados (Caso 1)
  - Certificados SSL en todas las conexiones (Caso 1)
  - Red WiFi aislada para equipos críticos (Caso 2)

### Tarjeta 3: SYN Flood (DDoS)

**ESCENARIO:** El servidor web de la empresa deja de responder porque recibe miles de solicitudes de conexión.

**SÍNTOMAS:**
- Servidor no responde a usuarios legítimos
- Conexiones quedan "colgadas"
- Recursos del servidor agotados

**ANÁLISIS:**
- **Capa OSI:** Capa 4 (Transporte)
- **Justificación:** El SYN Flood ataca la capa de transporte porque:
  - El handshake TCP (SYN, SYN-ACK, ACK) ocurre en esta capa
  - Los puertos TCP/UDP se manejan en la capa de transporte
  - El atacante explota el mecanismo de conexión TCP
  - Los SYN Cookies son una defensa específica de esta capa
- **Ataque:** Denegación de servicio distribuida
- **Ejemplo Real:** Ataque a servidor web de banco
- **Caso Similar:** Caso 1 (E-commerce) - Múltiples SYN packets desde 192.168.1.100 y Caso 4 (TelecomLatina) - DDoS distribuido
- **Tarjeta RISKIO:** "9 - Monitoreo de red" (alertas 24x7)
- **Justificación RISKIO:** El monitoreo de red 24x7 permite detectar patrones anómalos, generar alertas en tiempo real, y monitorear eventos clave para identificar ataques DDoS antes de que afecten los servicios.
- **Contramedidas Adicionales de Casos:**
  - SYN Cookies en servidores web (Caso 1)
  - Rate limiting por IP (Caso 1, Caso 3)
  - DDoS protection services (Caso 1, Caso 3, Caso 4)
  - Coordinación con CSIRT Chile (Caso 4)

### Tarjeta 4: Session Hijacking

**ESCENARIO:** Un usuario reporta que alguien accedió a su cuenta bancaria sin su autorización.

**SÍNTOMAS:**
- Actividad sospechosa en la cuenta
- Sesión activa desde ubicación desconocida
- Usuario no cerró sesión en computadora pública

**ANÁLISIS:**
- **Capa OSI:** Capa 5 (Sesión)
- **Justificación:** El Session Hijacking ocurre en la capa de sesión porque:
  - Esta capa maneja el establecimiento, mantenimiento y terminación de sesiones
  - Los IDs de sesión y tokens se gestionan en esta capa
  - El atacante secuestra una sesión activa entre aplicaciones
  - Los timeouts y regeneración de sesiones son funciones de esta capa
- **Ataque:** Robo de sesión activa
- **Ejemplo Real:** Robo de sesión bancaria en cibercafé
- **Caso Similar:** Caso 3 (Universidad) - Servidor de autenticación sobrecargado
- **Tarjeta RISKIO:** "4 - Control de acceso" (nivel apropiado de acceso)
- **Justificación RISKIO:** El control de acceso asegura que solo quienes deben tener acceso al sistema lo tengan y al nivel apropiado, previniendo el secuestro de sesiones mediante autenticación robusta y gestión de permisos.
- **Contramedidas Adicionales de Casos:**
  - Rate limiting + Timeouts (Caso 3)
  - Múltiples servidores de autenticación (Caso 3)
  - HTTPS obligatorio para encriptar comunicaciones
  - Logout automático de sesiones inactivas

### Tarjeta 5: SQL Injection

**ESCENARIO:** Un formulario web acepta código malicioso que permite acceder a la base de datos.

**SÍNTOMAS:**
- Mensajes de error extraños en la web
- Datos de usuarios aparecen donde no deberían
- Comportamiento inesperado del sitio web

**ANÁLISIS:**
- **Capa OSI:** Capa 7 (Aplicación)
- **Justificación:** La SQL Injection ataca la capa de aplicación porque:
  - El ataque se ejecuta contra aplicaciones web (HTTP/HTTPS)
  - Las consultas SQL se procesan en el nivel de aplicación
  - Los formularios web y validación de entrada son funciones de esta capa
  - Los Web Application Firewalls (WAF) protegen esta capa específicamente
- **Ataque:** Inyección de código SQL
- **Ejemplo Real:** Inyección en formulario de login
- **Caso Similar:** Caso 1 (E-commerce) - Login attempt: admin' OR '1'='1' detectado
- **Tarjeta RISKIO:** "3 - Configuración segura" (sistemas configurados de manera segura)
- **Justificación RISKIO:** La configuración segura asegura que los sistemas estén configurados de la manera más segura para las necesidades de la organización, incluyendo validación de entrada, prepared statements, y configuración de bases de datos seguras.
- **Contramedidas Adicionales de Casos:**
  - WAF para bloquear inyecciones (Caso 1)
  - Prepared statements en código (Caso 1)
  - Input validation en formularios (Caso 1)
  - Least privilege en bases de datos

### Tarjeta 6: IP Spoofing

**ESCENARIO:** Los logs de red muestran paquetes que parecen venir de direcciones IP internas pero no existen.

**SÍNTOMAS:**
- Paquetes con IPs internas falsas
- Tráfico sospechoso desde "dentro" de la red
- Firewall confundido sobre origen del tráfico

**ANÁLISIS:**
- **Capa OSI:** Capa 3 (Red)
- **Justificación:** El IP Spoofing ocurre en la capa de red porque:
  - Las direcciones IP se manejan en esta capa
  - El enrutamiento y forwarding de paquetes ocurre aquí
  - Los protocolos como IP, ICMP, OSPF operan en esta capa
  - Los firewalls de red filtran basándose en direcciones IP
- **Ataque:** Falsificación de dirección IP
- **Ejemplo Real:** Falsificación IP en ataques DDoS
- **Caso Similar:** Caso 4 (TelecomLatina) - Múltiples IPs falsas en ataque coordinado
- **Tarjeta RISKIO:** "K - Firewalls perimetrales" (prevenir acceso no autorizado)
- **Justificación RISKIO:** Los firewalls perimetrales previenen el acceso no autorizado mediante filtrado de tráfico, detección de IPs falsas, y control del flujo de datos entre redes, bloqueando paquetes con direcciones IP falsificadas.
- **Contramedidas Adicionales de Casos:**
  - BCP38 para filtrar tráfico con IPs falsas
  - Egress filtering para tráfico saliente
  - Monitoreo de patrones anómalos (Caso 4)
  - Coordinación con otros ISP (Caso 4)

### Tarjeta 7: WiFi Jamming

**ESCENARIO:** Todos los dispositivos WiFi de la oficina pierden conexión simultáneamente sin razón aparente.

**SÍNTOMAS:**
- Conexiones WiFi se cortan de repente
- Dispositivos no pueden reconectarse
- Interferencia en la banda de frecuencia WiFi

**ANÁLISIS:**
- **Capa OSI:** Capa 1 + Capa 2 (Física + Enlace)
- **Justificación:** El WiFi Jamming es multi-capa porque:
  - **Capa 1 (Física):** Interferencia electromagnética en el espectro de radio
  - **Capa 2 (Enlace):** Ataques de protocolo como deauthentication frames y beacon flooding
  - El atacante puede interferir tanto en el nivel físico como en el de protocolo
  - Las contramedidas deben considerar ambos niveles
- **Ataque:** Interferencia electromagnética
- **Ejemplo Real:** Interferencia en hospital con equipos médicos
- **Caso Similar:** Caso 2 (Hospital) - Jamming signal detected on 2.4 GHz y Caso 4 (TelecomLatina) - Interferencia física en señales WiFi/radio
- **Tarjeta RISKIO:** "J - Respaldo de datos" (restaurar en caso de pérdida)
- **Justificación RISKIO:** El respaldo de datos permite restaurar servicios críticos en caso de pérdida de conectividad, proporcionando alternativas cuando la infraestructura principal está comprometida por interferencia física.
- **Contramedidas Adicionales de Casos:**
  - Backup cableado para equipos críticos (Caso 2, Caso 4)
  - Monitoreo RF continuo (Caso 2)
  - Protocolos de emergencia médica (Caso 2)
  - Redundancia en infraestructura crítica (Caso 4)

### Tarjeta 8: Malware Propagation

**ESCENARIO:** Un virus se propaga automáticamente entre computadoras de la red sin que los usuarios hagan nada.

**SÍNTOMAS:**
- Múltiples computadoras infectadas
- Propagación automática por la red
- Uso excesivo de ancho de banda
- Comportamiento extraño en dispositivos

**ANÁLISIS:**
- **Capa OSI:** Capa 7 (Aplicación) + Capa 3 (Red)
- **Justificación:** El malware se propaga principalmente en:
  - **Capa 7 (Aplicación):** Se ejecuta como aplicación y puede propagarse por email/web
  - **Capa 3 (Red):** Utiliza direcciones IP para propagación en red y comunicación con servidores C&C
  - **Capa 4 (Transporte):** Explota puertos TCP/UDP para conexiones de red
- **Ataque:** Propagación automática de malware
- **Ejemplo Real:** WannaCry en red corporativa
- **Caso Similar:** Caso 4 (TelecomLatina) - Propagación automática por múltiples capas de red
- **Tarjeta RISKIO:** "5 - Protección contra malware" (antivirus instalado y actualizado)
- **Justificación RISKIO:** La protección contra malware asegura que la protección contra virus y malware esté instalada y actualizada, previniendo la propagación automática de malware a través de múltiples capas de la red.
- **Contramedidas Adicionales de Casos:**
  - Segmentación de redes infectadas (Caso 4)
  - Monitoreo de comportamiento anómalo (Caso 4)
  - Educación de usuarios sobre seguridad
  - Aislamiento de sistemas comprometidos

### Tarjeta 9: Man-in-the-Middle

**ESCENARIO:** Un atacante se posiciona entre dos dispositivos que se comunican y puede ver todos los mensajes.

**SÍNTOMAS:**
- Comunicaciones interceptadas
- Datos sensibles comprometidos
- Certificados SSL inválidos

**ANÁLISIS:**
- **Capa OSI:** Capa 6 (Presentación)
- **Justificación:** El Man-in-the-Middle ataca la capa de presentación porque:
  - Esta capa maneja la encriptación/desencriptación SSL/TLS
  - Los certificados digitales se validan en esta capa
  - La presentación de datos (formato, encriptación) ocurre aquí
  - Los ataques a certificados SSL/TLS son específicos de esta capa
- **Ataque:** Interceptación de comunicaciones SSL/TLS
- **Ejemplo Real:** Interceptación en red WiFi pública
- **Caso Similar:** Caso 1 (E-commerce) - Interceptación de datos sensibles y Caso 2 (Hospital) - Datos de pacientes comprometidos
- **Tarjeta RISKIO:** "K - Firewalls perimetrales" (prevenir acceso no autorizado)
- **Justificación RISKIO:** Los firewalls perimetrales previenen el acceso no autorizado bloqueando conexiones maliciosas, filtrando tráfico interceptado, y controlando el flujo de datos para prevenir ataques Man-in-the-Middle.
- **Contramedidas Adicionales de Casos:**
  - Certificados SSL válidos (Caso 1, Caso 2)
  - Certificate pinning para fijar certificados
  - VPN para túneles seguros (Caso 1)
  - Validación de cadena de certificados

### Tarjeta 10: ARP Poisoning

**ESCENARIO:** Los dispositivos de la red local envían todo su tráfico a una computadora que no es el gateway real.

**SÍNTOMAS:**
- Tráfico redirigido incorrectamente
- Lentitud en la red local
- Comunicaciones interceptadas

**ANÁLISIS:**
- **Capa OSI:** Capa 2 (Enlace de Datos)
- **Justificación:** El ARP Poisoning ocurre en la capa de enlace porque:
  - El protocolo ARP (Address Resolution Protocol) opera en esta capa
  - La tabla ARP mapea direcciones IP a direcciones MAC
  - Los frames Ethernet con direcciones MAC se manejan en esta capa
  - El atacante manipula la resolución de direcciones IP a MAC
- **Ataque:** Manipulación de tabla ARP
- **Ejemplo Real:** Redirección de tráfico en red local
- **Caso Similar:** Caso 1 (E-commerce) - ARP table modification detected y Caso 4 (TelecomLatina) - ARP table overflow, múltiples MAC addresses
- **Tarjeta RISKIO:** "9 - Monitoreo de red" (monitorear eventos clave)
- **Justificación RISKIO:** El monitoreo de red permite detectar cambios en la tabla ARP, identificar direcciones MAC duplicadas, y monitorear eventos clave para detectar ataques de envenenamiento ARP en tiempo real.
- **Contramedidas Adicionales de Casos:**
  - ARP monitoring en switches (Caso 1)
  - VLANs para segmentar redes (Caso 1, Caso 4)
  - Port security en switches (Caso 1)
  - Aislamiento de redes críticas (Caso 4)

### Tarjeta 11: Port Scanning

**ESCENARIO:** Un sistema intenta conectarse a múltiples puertos de los servidores de la empresa.

**SÍNTOMAS:**
- Múltiples intentos de conexión
- Puertos específicos siendo probados
- Actividad sospechosa en logs de red

**ANÁLISIS:**
- **Capa OSI:** Capa 4 (Transporte)
- **Justificación:** El Port Scanning ataca la capa de transporte porque:
  - Los puertos TCP/UDP se manejan en esta capa
  - El atacante prueba conexiones a puertos específicos
  - Los servicios de red se identifican por sus puertos
  - Los firewalls filtran tráfico basándose en puertos
- **Ataque:** Escaneo de puertos abiertos
- **Ejemplo Real:** Escaneo de puertos en servidor web
- **Caso Similar:** Caso 1 (E-commerce) - Port scan detected on 192.168.1.100 y Caso 4 (TelecomLatina) - Port scan detected
- **Tarjeta RISKIO:** "2 - Asegurar portátiles/PC" (eliminar servicios no necesarios)
- **Justificación RISKIO:** Asegurar portátiles/PC eliminando todas las cuentas de usuario y servicios predeterminados no necesarios previene el escaneo de puertos al cerrar servicios innecesarios y reducir la superficie de ataque.
- **Contramedidas Adicionales de Casos:**
  - Firewalls para bloquear puertos innecesarios (Caso 1, Caso 4)
  - IDS/IPS para detectar escaneos (Caso 1, Caso 4)
  - Honeypots como trampas para atacantes
  - Monitoreo de actividad sospechosa (Caso 1, Caso 4)

### Tarjeta 12: Brute Force Attack

**ESCENARIO:** Un atacante intenta adivinar contraseñas probando miles de combinaciones diferentes.

**SÍNTOMAS:**
- Múltiples intentos de login fallidos
- Cuentas bloqueadas por seguridad
- Actividad inusual en servidores de autenticación

**ANÁLISIS:**
- **Capa OSI:** Capa 7 (Aplicación)
- **Justificación:** El Brute Force Attack ocurre en la capa de aplicación porque:
  - La autenticación de usuarios se maneja en el nivel de aplicación
  - Los formularios de login y sistemas de autenticación operan aquí
  - Los mecanismos de rate limiting y bloqueo de cuentas son funciones de aplicación
  - Los sistemas MFA y CAPTCHA se implementan en esta capa
- **Ataque:** Fuerza bruta en autenticación
- **Ejemplo Real:** Ataque a panel admin web
- **Caso Similar:** Caso 4 (TelecomLatina) - Intentos de fuerza bruta en routers principales
- **Tarjeta RISKIO:** "4 - Control de acceso" (solo quienes deben tener acceso)
- **Justificación RISKIO:** El control de acceso asegura que solo quienes deben tener acceso al sistema lo tengan, implementando autenticación multifactor, bloqueo de cuentas, y controles de acceso estrictos para prevenir ataques de fuerza bruta.
- **Contramedidas Adicionales de Casos:**
  - Rate limiting para limitar intentos (Caso 3, Caso 4)
  - MFA para autenticación multifactor
  - Account lockout después de intentos fallidos
  - CAPTCHA para verificar que es un humano

---

## 3. Aplicación a Casos Prácticos

### Caso 1: E-commerce (TechStore.cl)

**ESCENARIO ORIGINAL:** Empresa de comercio electrónico con sitio web de transacciones, base de datos de 50,000 clientes, red WiFi para empleados y sistema de pagos integrado.

**INCIDENTE:** El equipo de seguridad detectó actividad sospechosa en el sistema de pagos a las 02:30 AM.

**EVIDENCIA RECOLECTADA:**
- Logs de aplicación: SQL queries sospechosas, login attempt con SQL injection
- Logs de red: Nueva conexión WiFi "TechStore_Guest", port scan, múltiples SYN packets
- Logs de seguridad: WAF alert por SQL injection, IDS alert por acceso no autorizado

**Tarjetas Relacionadas:** 1, 2, 3, 5, 6

**Aplicación de Contramedidas:**

**TARJETA 1 (Interceptación WiFi):**
- Implementar WPA3 en red corporativa
- Monitoreo continuo de usuarios conectados
- WIDS/WIPS para detectar sniffing

**TARJETA 2 (Evil Twin):**
- Verificar SSID oficial "TechStore_Corp"
- VPN obligatorio para empleados
- Certificados SSL en todas las conexiones

**TARJETA 3 (SYN Flood):**
- SYN Cookies en servidores web
- Rate limiting por IP
- DDoS protection service

**TARJETA 5 (SQL Injection):**
- WAF para bloquear inyecciones
- Prepared statements en código
- Input validation en formularios

**TARJETA 6 (ARP Poisoning):**
- ARP monitoring en switches
- VLANs para segmentar redes
- Port security en switches

---

### Caso 2: Hospital (Hospital Regional San José)

**ESCENARIO ORIGINAL:** Hospital con red WiFi separada por departamentos, sistemas médicos críticos, base de datos de pacientes (HIPAA), dispositivos IoT médicos y acceso remoto para médicos.

**INCIDENTE:** Los sistemas de monitoreo de pacientes en la UCI comenzaron a fallar a las 11:15 AM.

**EVIDENCIA RECOLECTADA:**
- Logs de sistemas médicos: Todos los monitores de UCI perdieron conexión
- Logs de red WiFi: Deauthentication frames, múltiples dispositivos desconectados, nueva AP "Hospital_Guest"
- Logs de seguridad: WIDS alert por Rogue AP, acceso físico no autorizado

**Tarjetas Relacionadas:** 7, 2

**Aplicación de Contramedidas:**

**TARJETA 7 (WiFi Jamming):**
- CRÍTICO: Monitores de UCI desconectados
- SOLUCIÓN: Backup cableado para equipos médicos
- DETECCIÓN: Monitoreo RF continuo
- PLAN: Protocolos de emergencia médica

**TARJETA 2 (Evil Twin):**
- CRÍTICO: Datos de pacientes interceptados
- SOLUCIÓN: Red WiFi aislada para equipos médicos
- VERIFICACIÓN: SSID oficial "Hospital_Med"
- ENCRIPTACIÓN: VPN para acceso remoto

---

### Caso 3: Universidad (Universidad Tecnológica del Sur)

**ESCENARIO ORIGINAL:** Universidad con red WiFi pública para estudiantes, red WiFi privada para administración, laboratorios de computación, biblioteca digital y sistema de gestión académica.

**INCIDENTE:** Estudiantes reportan que no pueden acceder a la red WiFi y el sistema de gestión académica está caído a las 09:30 AM.

**EVIDENCIA RECOLECTADA:**
- Logs de red WiFi: Beacon flood detectado, múltiples SSIDs "UTS_WiFi_1,2", congestión de canales
- Logs de sistema académico: DDoS attack detectado, database connection pool exhausted
- Logs de seguridad: WIDS alert por beacon flooding, IDS alert por DDoS desde múltiples IPs

**Tarjetas Relacionadas:** 8, 3, 4

**Aplicación de Contramedidas:**

**TARJETA 8 (Beacon Flooding):**
- PROBLEMA: Múltiples SSIDs falsos
- SOLUCIÓN: WIDS/WIPS + Rate limiting
- BALANCE: Permitir redes legítimas
- EDUCACIÓN: Informar a estudiantes

**TARJETA 3 (DDoS):**
- PROBLEMA: Servidores académicos caídos
- SOLUCIÓN: DDoS protection + Rate limiting
- BALANCE: Mantener acceso para estudiantes
- MONITOREO: Detectar patrones anómalos

**TARJETA 4 (Auth Server):**
- PROBLEMA: Servidor de autenticación sobrecargado
- SOLUCIÓN: Rate limiting + Timeouts
- BALANCE: No bloquear usuarios legítimos
- ESCALABILIDAD: Múltiples servidores auth

---

### Caso 4: TelecomLatina (Infraestructura Crítica)

**ESCENARIO ORIGINAL:** ISP principal con red de fibra óptica nacional, centros de datos distribuidos, servicios para 2M+ usuarios, conexiones internacionales y servicios críticos para bancos, hospitales y gobierno.

**INCIDENTE:** Ataque coordinado de 3 días que afectó al 80% de usuarios, centros de datos offline y servicios críticos interrumpidos.

**EVIDENCIA RECOLECTADA:**
- Logs de red críticos: ARP table overflow, múltiples MAC addresses, routing table modified
- Logs de WiFi: Beacon flood, deauthentication frames, rogue AP, channel congestion
- Logs de firewall: SYN flood, port scan, DDoS attack in progress
- Reporte de inteligencia: APT-41 (China), técnicas de interferencia física

**Tarjetas Relacionadas:** 7, 6, 3

**Aplicación de Contramedidas:**

**TARJETA 7 (WiFi Jamming):**
- CRÍTICO: 80% usuarios sin Internet
- PRIORIDAD: Backup cableado inmediato
- DETECCIÓN: Monitoreo RF nacional
- COORDINACIÓN: Otros ISP afectados

**TARJETA 6 (ARP Poisoning):**
- CRÍTICO: Tráfico redirigido incorrectamente
- PRIORIDAD: ARP monitoring en routers principales
- SEGMENTACIÓN: VLANs críticas
- AISLAMIENTO: Redes de servicios críticos

**TARJETA 3 (DDoS):**
- CRÍTICO: Centros de datos offline
- PRIORIDAD: DDoS protection services
- ESCALABILIDAD: Múltiples proveedores
- COORDINACIÓN: CSIRT Chile

---

### Matriz de Conexión Tarjetas-Casos

```
┌─────────────────────────────────────────────────────────────┐
│                MATRIZ DE CONEXIÓN TARJETAS-CASOS             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  TARJETA │ CASO RELACIONADO │ ATAQUE ESPECÍFICO │ APLICACIÓN │
│  ┌───────┼─────────────────┼───────────────────┼───────────┐ │
│  │   1   │ Caso 1          │ Evil Twin Attack  │ WIDS/WIPS  │ │
│  │       │ E-commerce     │ "TechStore_Guest" │ Detección  │ │
│  │       │                 │                   │ automática │ │
│  ├───────┼─────────────────┼───────────────────┼───────────┤ │
│  │   2   │ Caso 1          │ Evil Twin Attack  │ Verificar  │ │
│  │       │ E-commerce     │ Punto de acceso   │ SSID + VPN │ │
│  │       │                 │ malicioso         │ obligatorio│ │
│  ├───────┼─────────────────┼───────────────────┼───────────┤ │
│  │   3   │ Caso 1          │ SYN Flood         │ SYN Cookies│ │
│  │       │ E-commerce     │ Múltiples SYN     │ + Rate     │ │
│  │       │                 │ desde 192.168.1.100│ Limiting   │ │
│  ├───────┼─────────────────┼───────────────────┼───────────┤ │
│  │   5   │ Caso 1          │ SQL Injection     │ WAF +      │ │
│  │       │ E-commerce     │ admin' OR '1'='1' │ Prepared   │ │
│  │       │                 │                   │ Statements │ │
│  ├───────┼─────────────────┼───────────────────┼───────────┤ │
│  │   6   │ Caso 1          │ ARP Poisoning     │ ARP        │ │
│  │       │ E-commerce     │ Modificación tabla│ Monitoring │ │
│  │       │                 │ ARP               │ + VLANs    │ │
│  ├───────┼─────────────────┼───────────────────┼───────────┤ │
│  │   7   │ Caso 2          │ WiFi Jamming      │ Backup     │ │
│  │       │ Hospital       │ Señales 2.4 GHz   │ cableado + │ │
│  │       │                 │                   │ Detección RF│ │
│  ├───────┼─────────────────┼───────────────────┼───────────┤ │
│  │   2   │ Caso 2          │ Rogue AP          │ WIDS/WIPS  │ │
│  │       │ Hospital       │ "Hospital_Guest"  │ + Verificar│ │
│  │       │                 │                   │ SSID       │ │
│  ├───────┼─────────────────┼───────────────────┼───────────┤ │
│  │   7   │ Caso 3          │ Beacon Flooding   │ WIDS/WIPS  │ │
│  │       │ Universidad     │ Múltiples SSIDs   │ + Rate     │ │
│  │       │                 │ "UTS_WiFi_1,2"    │ Limiting   │ │
│  ├───────┼─────────────────┼───────────────────┼───────────┤ │
│  │   3   │ Caso 3          │ DDoS Attack       │ DDoS       │ │
│  │       │ Universidad     │ Servidores        │ Protection │ │
│  │       │                 │ académicos        │ Services   │ │
│  ├───────┼─────────────────┼───────────────────┼───────────┤ │
│  │   4   │ Caso 3          │ Auth Server       │ Rate       │ │
│  │       │ Universidad     │ Overload          │ Limiting + │ │
│  │       │                 │                   │ Timeouts   │ │
│  ├───────┼─────────────────┼───────────────────┼───────────┤ │
│  │   7   │ Caso 4          │ WiFi Jamming      │ Redundancia│ │
│  │       │ TelecomLatina  │ Señales WiFi/radio│ + Backup   │ │
│  │       │                 │                   │ cableado   │ │
│  ├───────┼─────────────────┼───────────────────┼───────────┤ │
│  │   8   │ Caso 4          │ Malware Propagation│ Antivirus  │ │
│  │       │ TelecomLatina  │ Propagación auto. │ + Segment. │ │
│  │       │                 │ por múltiples capas│            │ │
│  ├───────┼─────────────────┼───────────────────┼───────────┤ │
│  │   6   │ Caso 4          │ ARP Poisoning     │ ARP        │ │
│  │       │ TelecomLatina  │ Masivo            │ Monitoring │ │
│  │       │                 │                   │ + VLANs    │ │
│  ├───────┼─────────────────┼───────────────────┼───────────┤ │
│  │   3   │ Caso 4          │ DDoS Distribuido  │ DDoS       │ │
│  │       │ TelecomLatina  │ Múltiples IPs     │ Protection │ │
│  │       │                 │                   │ + Firewalls│ │
│  └───────┴─────────────────┴───────────────────┴───────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 4. Criterios de Evaluación

### Excelente (90-100%):
- Identificación correcta de capa OSI para todas las tarjetas
- Contramedidas específicas y efectivas
- Comprensión profunda de los ataques
- Explicación clara de la relación entre capa y ataque
- Aplicación correcta de contramedidas a casos prácticos

### Bueno (80-89%):
- Identificación correcta de la mayoría de capas OSI
- Contramedidas apropiadas
- Comprensión básica de los ataques
- Algunas explicaciones de la relación capa-ataque
- Aplicación básica a casos prácticos

### Satisfactorio (70-79%):
- Identificación parcial de capas OSI
- Contramedidas básicas
- Comprensión superficial de ataques
- Pocas explicaciones de relaciones
- Aplicación limitada a casos prácticos

### Necesita Mejora (<70%):
- Múltiples errores en identificación de capas
- Contramedidas inadecuadas o ausentes
- Comprensión limitada de ataques
- Sin explicaciones de relaciones
- Sin aplicación a casos prácticos

---

## 5. Puntos de Discusión para el Debate

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

---

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
- Aplicación práctica a casos reales

### Adaptaciones Posibles:
- Modificar escenarios según el contexto local
- Agregar tarjetas específicas de la industria
- Incluir casos de estudio reales
- Personalizar según nivel de experiencia de los estudiantes
