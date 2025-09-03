# Slides: Semana 5 - Tipos de Ataques en Redes y Seguridad Inalámbrica

## Slide 1: Título

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  TICS413: Seguridad TI                                      │
│                                                             │
│  SEMANA 5                                                   │
│                                                             │
│  Tipos de Ataques en Redes y                                │
│  Seguridad Inalámbrica                                      │
│                                                             │
│  Prof. Romina Torres                                        │
│  Segundo Semestre 2025                                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Slide 2: Objetivos de Aprendizaje

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  OBJETIVOS DE APRENDIZAJE                                   │
│                                                             │
│  Al finalizar esta sesión, serás capaz de:                 │
│                                                             │
│  ✓ Identificar y clasificar ataques por capa OSI           │
│  ✓ Analizar vulnerabilidades en redes inalámbricas         │
│  ✓ Aplicar contramedidas apropiadas                        │
│  ✓ Evaluar riesgos de seguridad                            │
│  ✓ Desarrollar estrategias de defensa en profundidad      │
│                                                             │
│  Metodología: Análisis práctico y ejercicios colaborativos │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Slide 3: Agenda de la Sesión

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  AGENDA DE LA SESIÓN                                        │
│                                                             │
│  1. Introducción a ataques por capa OSI (20 min)           │
│     • Modelo OSI y vulnerabilidades                        │
│     • Ataques más comunes por capa                         │
│                                                             │
│  2. Seguridad en redes inalámbricas (25 min)               │
│     • Características únicas de WiFi                       │
│     • Amenazas específicas (Evil Twin, KRACK, etc.)       │
│     • Estándares de seguridad (WPA2/WPA3)                   │
│                                                             │
│  3. Contramedidas y controles (20 min)                     │
│     • Clasificación de controles                           │
│     • Defensa en profundidad                               │
│     • Implementación práctica                              │
│                                                             │
│  4. Top Table Exercise (45 min)                             │
│     • Clasificación de ataques                             │
│     • Análisis de contramedidas                            │
│     • Discusión grupal                                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Slide 4: Modelo OSI y Seguridad de Redes

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  MODELO OSI Y SEGURIDAD DE REDES                           │
│                                                             │
│  CAPA 7: APLICACIÓN (Protocolos de Red)                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ DNS Poisoning • HTTP/HTTPS Interception •          │   │
│  │ Email Spoofing • FTP/SFTP Attacks • SSH Attacks     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CAPA 6: PRESENTACIÓN (Codificación de Red)               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ SSL/TLS Downgrade • Certificate Stealers •         │   │
│  │ Encoding Attacks • Format String Attacks           │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CAPA 5: SESIÓN (Protocolos de Sesión)                     │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Session Hijacking • RPC Hijacking • NetBIOS         │   │
│  │ Attacks • Session Fixation • Session Replay        │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CAPA 4: TRANSPORTE (Conexiones de Red)                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ SYN Flood • Port Scanning • TCP Hijacking •        │   │
│  │ UDP Flooding • Amplification Attacks               │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CAPA 3: RED (Enrutamiento)                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ IP Spoofing • DDoS/DoS • Route Poisoning •         │   │
│  │ ICMP Flooding • Smurf Attacks                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CAPA 2: ENLACE (Red Local)                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ ARP Poisoning • MAC Spoofing • VLAN Hopping •      │   │
│  │ DHCP Spoofing • Rogue Access Points                │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CAPA 1: FÍSICA (Infraestructura)                        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ WiFi Jamming • Cable Tapping • Physical Access •   │
│  │ Signal Interception • Sabotage                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Slide 5: Ataques por Capa - Ejemplos de Red

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ATAQUES POR CAPA - EJEMPLOS DE RED                        │
│                                                             │
│  CAPA 7: DNS Poisoning                                     │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ Input: www.banco.com → 192.168.1.100 (falso)       │   │
│  │                                                     │   │
│  │ Result: Usuario va a sitio falso                   │   │
│  │                                                     │   │
│  │ Contramedida: DNSSEC + Monitoreo DNS               │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CAPA 4: SYN Flood                                         │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ Attack: Múltiples paquetes SYN                      │   │
│  │                                                     │   │
│  │ Result: Agotamiento de recursos del servidor        │   │
│  │                                                     │   │
│  │ Contramedida: SYN Cookies + Rate Limiting          │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CAPA 2: ARP Poisoning                                     │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ Attack: Respuestas ARP falsas                       │   │
│  │                                                     │   │
│  │ Result: Interceptación de tráfico                   │   │
│  │                                                     │   │
│  │ Contramedida: Port Security + ARP Monitoring       │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Slide 6: Redes Inalámbricas - Vulnerabilidades Específicas

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  REDES INALÁMBRICAS - VULNERABILIDADES ESPECÍFICAS          │
│                                                             │
│  CARACTERÍSTICAS INHERENTES:                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Transmisión por radio (sin barreras físicas)     │   │
│  │ • Acceso por cualquier dispositivo en rango        │   │
│  │ • Interceptación fácil de señales                  │   │
│  │ • Movilidad de dispositivos                        │   │
│  │ • Recursos limitados en dispositivos IoT           │   │
│  │ • Propagación de señales más allá del control      │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  AMENAZAS ESPECÍFICAS DE RED:                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Evil Twin Attacks (Capa 2)                       │   │
│  │ • Deauthentication Attacks (Capa 2)                │   │
│  │ • KRACK (Key Reinstallation Attack)                │   │
│  │ • WiFi Jamming (Capa 1)                             │   │
│  │ • Rogue Access Points (Capa 2)                      │   │
│  │ • WiFi Malware (Capa 7)                             │   │
│  │ • Botnets Inalámbricas (Multi-capa)                │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Slide 7: Evil Twin Attack

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  EVIL TWIN ATTACK                                           │
│                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│  │             │    │             │    │             │     │
│  │   USUARIO   │    │  ATACANTE   │    │ PUNTO DE    │     │
│  │             │    │  ACCESO     │    │ LEGÍTIMO    │     │
│  │             │    │             │    │             │     │
│  └─────────────┘    └─────────────┘    └─────────────┘     │
│        │                   │                   │            │
│        │ 1. Busca redes     │                   │            │
│        │    WiFi            │                   │            │
│        │                   │                   │            │
│        │ 2. Ve "Café_WiFi" │                   │            │
│        │    (legítimo)      │                   │            │
│        │                   │                   │            │
│        │ 3. Atacante crea  │                   │            │
│        │    "Café_WiFi"    │                   │            │
│        │    (falso)         │                   │            │
│        │                   │                   │            │
│        │ 4. Usuario se      │                   │            │
│        │    conecta al      │                   │            │
│        │    falso           │                   │            │
│        │                   │                   │            │
│        │ 5. Interceptación │                   │            │
│        │    completa        │                   │            │
│                                                             │
│  CONTRAMEDIDAS:                                             │
│  • Verificar certificados SSL/TLS                          │
│  • Usar VPNs para tráfico sensible                          │
│  • Configurar alertas para nuevas redes                     │
│  • Educar usuarios sobre riesgos                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Slide 8: Estándares de Seguridad WiFi

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  EVOLUCIÓN DE ESTÁNDARES DE SEGURIDAD WIFI                 │
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │             │  │             │  │             │         │
│  │    WEP      │  │    WPA      │  │    WPA2     │         │
│  │   (1997)    │  │   (2003)    │  │   (2004)    │         │
│  │             │  │             │  │             │         │
│  │ RC4 (40/104 │  │ TKIP        │  │ CCMP/AES    │         │
│  │ bits)       │  │             │  │             │         │
│  │             │  │             │  │             │         │
│  │ Vulnerable  │  │ Mejorado    │  │ Robusto     │         │
│  │ a ataques   │  │ sobre WEP   │  │ y seguro    │         │
│  │             │  │             │  │             │         │
│  │ NO USAR     │  │ Transición  │  │ Estándar    │         │
│  │             │  │             │  │ actual      │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │                    WPA3 (2018)                      │   │
│  │                                                     │   │
│  │ • AES-256                                           │   │
│  │ • Forward Secrecy                                   │   │
│  │ • Individual Encryption                             │   │
│  │ • Protection against dictionary attacks             │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Slide 9: Contramedidas de Red por Capa

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  CONTRAMEDIDAS DE RED POR CAPA                             │
│                                                             │
│  CAPA 7: PROTOCOLOS DE RED                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ • DNSSEC (DNS Security Extensions)                  │   │
│  │ • WAF para tráfico HTTP/HTTPS                       │   │
│  │ • Email filtering y SPF/DKIM                        │   │
│  │ • Protocol inspection en firewalls                  │   │
│  │ • Monitoreo de servicios SSH                       │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CAPA 6: PRESENTACIÓN DE RED                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ • TLS 1.3                                            │   │
│  │ • Certificate Pinning                                │   │
│  │ • Validación de certificados                         │   │
│  │ • Monitoreo de protocolos seguros                    │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CAPA 5: PROTOCOLOS DE SESIÓN                            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ • SSL/TLS para encriptación de sesiones             │   │
│  │ • Tokens de sesión únicos                            │   │
│  │ • Timeouts automáticos                               │   │
│  │ • Regeneración de IDs de sesión                      │   │
│  │ • Firewalls de aplicación para protocolos            │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CAPA 4: CONEXIONES DE RED                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ • Firewalls de estado                                │   │
│  │ • SYN Cookies                                         │   │
│  │ • Rate Limiting                                       │   │
│  │ • IPS/IDS                                             │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CAPA 3: ENRUTAMIENTO                                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ • Firewalls de red                                    │   │
│  │ • Filtrado de paquetes                               │   │
│  │ • Implementación de BCP38                             │   │
│  │ • Monitoreo de tráfico                               │   │
│  │ • Servicios de mitigación DDoS                       │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CAPA 2: RED LOCAL                                        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ • Port Security                                       │   │
│  │ • VLANs                                               │   │
│  │ • 802.1X                                              │   │
│  │ • ARP Monitoring                                      │   │
│  │ • DHCP Snooping                                       │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CAPA 1: INFRAESTRUCTURA                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ • Control de acceso físico                           │   │
│  │ • Cableado blindado                                  │   │
│  │ • Monitoreo de infraestructura                       │   │
│  │ • Separación de redes sensibles                      │   │
│  │ • Análisis de espectro                               │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Slide 10: Defensa en Profundidad

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  DEFENSA EN PROFUNDIDAD                                     │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │  CAPA 7: APLICACIÓN                                 │   │
│  │  ┌─────────────────────────────────────────────┐   │   │
│  │  │ WAF • Validación • Autenticación •         │   │   │
│  │  │ Sanitización                               │   │   │
│  │  └─────────────────────────────────────────────┘   │   │
│  │                                                     │   │
│  │  CAPA 6: PRESENTACIÓN                               │   │
│  │  ┌─────────────────────────────────────────────┐   │   │
│  │  │ TLS 1.3 • Certificados • Encriptación •    │   │   │
│  │  │ HSTS                                      │   │   │
│  │  └─────────────────────────────────────────────┘   │   │
│  │                                                     │   │
│  │  CAPA 5: SESIÓN                                     │   │
│  │  ┌─────────────────────────────────────────────┐   │   │
│  │  │ Tokens • Timeouts • Regeneración •          │   │   │
│  │  │ Encriptación                               │   │   │
│  │  └─────────────────────────────────────────────┘   │   │
│  │                                                     │   │
│  │  CAPA 4: TRANSPORTE                                 │   │
│  │  ┌─────────────────────────────────────────────┐   │   │
│  │  │ Firewalls • SYN Cookies • Rate Limiting •   │   │   │
│  │  │ IPS/IDS                                   │   │   │
│  │  └─────────────────────────────────────────────┘   │   │
│  │                                                     │   │
│  │  CAPA 3: RED                                        │   │
│  │  ┌─────────────────────────────────────────────┐   │   │
│  │  │ Firewalls • Filtrado • DDoS Protection •    │   │   │
│  │  │ VPNs                                      │   │   │
│  │  └─────────────────────────────────────────────┘   │   │
│  │                                                     │   │
│  │  CAPA 2: ENLACE                                     │   │
│  │  ┌─────────────────────────────────────────────┐   │   │
│  │  │ Port Security • VLANs • 802.1X • ARP        │   │   │
│  │  │ Monitoring                                 │   │   │
│  │  └─────────────────────────────────────────────┘   │   │
│  │                                                     │   │
│  │  CAPA 1: FÍSICA                                     │   │
│  │  ┌─────────────────────────────────────────────┐   │   │
│  │  │ Control de Acceso • Cableado • Separación • │   │   │
│  │  │ UPS                                        │   │   │
│  │  └─────────────────────────────────────────────┘   │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Slide 11: Top Table Exercise

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  TOP TABLE EXERCISE                                         │
│                                                             │
│  OBJETIVO: Clasificar ataques y contramedidas              │
│                                                             │
│  MATERIALES:                                                │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Tarjetas de ataques (8 tipos diferentes)         │   │
│  │ • Tabla de clasificación                            │   │
│  │ • Marcadores y post-its                            │   │
│  │                                                     │   │
│  │ ACTIVIDADES:                                        │   │
│  │ • Clasificar por capa OSI                          │   │
│  │ • Identificar contramedidas                        │   │
│  │ • Priorizar implementación                         │   │
│  │ • Discutir en grupo                                 │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  TIEMPO: 45 minutos                                        │
│  EVALUACIÓN: Participación y precisión de clasificación    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Slide 12: Casos de Estudio

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  CASOS DE ESTUDIO                                           │
│                                                             │
│  CASO 1: Empresa de E-commerce                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Sitio web con transacciones                       │   │
│  │ • Base de datos de clientes                        │   │
│  │ • Red WiFi para empleados                           │   │
│  │                                                     │   │
│  │ PREGUNTA: ¿Qué ataques son más críticos?            │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CASO 2: Hospital                                          │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Sistemas médicos críticos                         │   │
│  │ • Datos de pacientes confidenciales                │   │
│  │ • Redes separadas por departamento                  │   │
│  │                                                     │   │
│  │ PREGUNTA: ¿Cómo protegerías cada sistema?           │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CASO 3: Universidad                                        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Red WiFi pública                                  │   │
│  │ • Estudiantes con dispositivos personales           │   │
│  │ • Investigación académica                           │   │
│  │                                                     │   │
│  │ PREGUNTA: ¿Qué controles implementarías?           │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Slide 13: Mejores Prácticas

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  MEJORES PRÁCTICAS DE SEGURIDAD                            │
│                                                             │
│  CONFIGURACIÓN BÁSICA:                                     │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ ☐ Cambiar credenciales por defecto                  │   │
│  │ ☐ Desactivar administración remota                  │   │
│  │ ☐ Mantener firmware actualizado                     │   │
│  │ ☐ Configurar filtrado MAC                           │   │
│  │ ☐ Reducir potencia de transmisión                   │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ENCRIPTACIÓN:                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ ☐ Usar WPA3 cuando sea posible                     │   │
│  │ ☐ Implementar 802.1X para autenticación             │   │
│  │ ☐ Configurar certificados digitales                │   │
│  │ ☐ Rotar claves regularmente                         │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  MONITOREO:                                                │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ ☐ Implementar WIDS/WIPS                             │   │
│  │ ☐ Configurar alertas de seguridad                   │   │
│  │ ☐ Mantener logs de auditoría                        │   │
│  │ ☐ Análisis de tráfico regular                       │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Slide 14: Evaluación y Próximos Pasos

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  EVALUACIÓN Y PRÓXIMOS PASOS                               │
│                                                             │
│  EVALUACIÓN DE LA SESIÓN:                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Participación en Top Table Exercise (30%)        │   │
│  │ • Análisis de casos presentado (40%)               │   │
│  │ • Clasificación de ataques (30%)                   │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  PRÓXIMOS PASOS:                                           │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Revisar material adicional en Canvas            │   │
│  │ • Completar ejercicios prácticos                   │   │
│  │ • Investigar casos reales de ataques              │   │
│  │ • Preparar para próxima sesión                     │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  RECURSOS ADICIONALES:                                     │
│  • Documentos de la semana 5                            │
│  • Herramientas de análisis de red                      │
│  • Casos de estudio adicionales                         │
│  • Enlaces de referencia                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Slide 15: Preguntas y Discusión

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  PREGUNTAS Y DISCUSIÓN                                     │
│                                                             │
│  PREGUNTAS CLAVE:                                          │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ 1. ¿Qué capa OSI es más vulnerable y por qué?      │   │
│  │                                                     │   │
│  │ 2. ¿Cómo se relacionan los ataques entre capas?    │   │
│  │                                                     │   │
│  │ 3. ¿Qué contramedidas son más efectivas?            │   │
│  │                                                     │   │
│  │ 4. ¿Cómo implementarías defensa en profundidad?    │   │
│  │                                                     │   │
│  │ 5. ¿Qué ataques requieren respuesta inmediata?      │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CONTACTO:                                                 │
│  • Email: romina.torres.t@uai.cl                          │
│  • Twitter: @rominabot                                     │
│  • Office Hours: Martes 14:00-16:00                       │
│                                                             │
│  ¡GRACIAS POR SU PARTICIPACIÓN!                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Notas para el Instructor

### Tiempo Sugerido por Slide:
- Slides 1-3: 10 minutos (introducción)
- Slides 4-5: 15 minutos (ataques por capa)
- Slides 6-8: 20 minutos (WiFi)
- Slides 9-10: 15 minutos (contramedidas)
- Slides 11-12: 10 minutos (ejercicio y casos)
- Slides 13-15: 10 minutos (cierre)

### Puntos Clave a Enfatizar:
1. **Defensa en profundidad** es fundamental
2. **Cada capa** tiene vulnerabilidades específicas
3. **WiFi** requiere consideraciones especiales
4. **Contramedidas** deben ser apropiadas al riesgo
5. **Práctica** es esencial para comprensión

### Materiales Necesarios:
- Proyector y computadora
- Tarjetas de ataques (imprimir)
- Tabla de clasificación (imprimir)
- Marcadores y post-its
- Cronómetro para el ejercicio

