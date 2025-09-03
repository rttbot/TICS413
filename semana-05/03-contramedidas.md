# Contramedidas y Controles de Seguridad

## Introducción

Las contramedidas son acciones específicas diseñadas para prevenir, detectar o responder a amenazas de seguridad. En este documento, analizaremos los controles más efectivos organizados por capa del modelo OSI y tipo de amenaza.

## Clasificación de Controles

### Diagrama: Tipos de Controles de Seguridad

```
┌─────────────────────────────────────────────────────────────┐
│                CLASIFICACIÓN DE CONTROLES                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CONTROLES PREVENTIVOS:     CONTROLES DETECTIVOS:           │
│  ┌─────────────────┐      ┌─────────────────┐            │
│  │                 │      │                 │            │
│  │ • Firewalls     │      │ • IDS/IPS        │            │
│  │ • Encriptación  │      │ • SIEM          │            │
│  │ • Autenticación │      │ • Logs          │            │
│  │ • Segmentación  │      │ • Monitoreo     │            │
│  │ • Validación    │      │ • Alertas       │            │
│  │                 │      │                 │            │
│  └─────────────────┘      └─────────────────┘            │
│                                                             │
│  CONTROLES CORRECTIVOS:    CONTROLES DISUASIVOS:            │
│  ┌─────────────────┐      ┌─────────────────┐            │
│  │                 │      │                 │            │
│  │ • Respuesta     │      │ • Señales        │            │
│  │   automática    │      │ • Advertencias   │            │
│  │ • Recuperación  │      │ • Políticas      │            │
│  │ • Parches       │      │ • Educación      │            │
│  │ • Backup        │      │ • Consecuencias  │            │
│  │                 │      │                 │            │
│  └─────────────────┘      └─────────────────┘            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Controles por Capa OSI

### Capa 7: Controles de Aplicación

```
┌─────────────────────────────────────────────────────────────┐
│                CONTROLES CAPA 7: APLICACIÓN                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PREVENTIVOS:                    DETECTIVOS:                │
│  ┌─────────────────────────┐      ┌─────────────────────────┐ │
│  │                         │      │                         │ │
│  │ • WAF (Web Application │      │ • Análisis de logs     │ │
│  │   Firewall)            │      │ • Monitoreo de BD      │ │
│  │                         │      │ • Alertas de acceso    │ │
│  │ • Validación de entrada │      │ • Detección de         │ │
│  │                         │      │   anomalías            │ │
│  │ • Sanitización de      │      │                         │ │
│  │   datos                │      │ • Análisis de          │ │
│  │                         │      │   comportamiento       │ │
│  │ • Autenticación        │      │                         │ │
│  │   multifactor           │      │ • Auditoría de         │ │
│  │                         │      │   aplicaciones         │ │
│  └─────────────────────────┘      └─────────────────────────┘ │
│                                                             │
│  CORRECTIVOS:                     DISUASIVOS:               │
│  ┌─────────────────────────┐      ┌─────────────────────────┐ │
│  │                         │      │                         │ │
│  │ • Respuesta automática  │      │ • Mensajes de error     │ │
│  │ • Bloqueo de IPs        │      │ • Advertencias de       │ │
│  │                         │      │   seguridad             │ │
│  │ • Rate limiting         │      │ • Políticas de uso      │ │
│  │                         │      │                         │ │
│  │ • Parches de seguridad  │      │ • Educación de           │ │
│  │                         │      │   usuarios              │ │
│  │ • Recuperación de BD    │      │                         │ │
│  └─────────────────────────┘      └─────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Controles Específicos:**

1. **Web Application Firewall (WAF)**
   - Filtrado de tráfico malicioso
   - Protección contra OWASP Top 10
   - Reglas personalizadas por aplicación

2. **Validación de Entrada**
   - Verificación de tipos de datos
   - Validación de longitud y formato
   - Sanitización de caracteres especiales

3. **Autenticación Multifactor**
   - Contraseñas + tokens
   - Biometría + PIN
   - Certificados digitales

### Capa 6: Controles de Presentación

```
┌─────────────────────────────────────────────────────────────┐
│              CONTROLES CAPA 6: PRESENTACIÓN                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PREVENTIVOS:                    DETECTIVOS:                │
│  ┌─────────────────────────┐      ┌─────────────────────────┐ │
│  │                         │      │                         │ │
│  │ • TLS 1.3               │      │ • Monitoreo de         │ │
│  │                         │      │   certificados         │ │
│  │ • Certificate Pinning   │      │ • Alertas de           │ │
│  │                         │      │   expiración           │ │
│  │ • Validación de         │      │                         │ │
│  │   certificados           │      │ • Detección de         │ │
│  │                         │      │   downgrade            │ │
│  │ • Encriptación fuerte   │      │                         │ │
│  │                         │      │ • Análisis de           │ │
│  │ • HSTS (HTTP Strict     │      │   protocolos            │ │
│  │   Transport Security)   │      │                         │ │
│  └─────────────────────────┘      └─────────────────────────┘ │
│                                                             │
│  CORRECTIVOS:                     DISUASIVOS:               │
│  ┌─────────────────────────┐      ┌─────────────────────────┐ │
│  │                         │      │                         │ │
│  │ • Renovación automática │      │ • Advertencias de       │ │
│  │   de certificados       │      │   seguridad             │ │
│  │                         │      │                         │ │
│  │ • Fallback seguro       │      │ • Indicadores de        │ │
│  │                         │      │   conexión segura       │ │
│  │ • Actualización de      │      │                         │ │
│  │   protocolos             │      │ • Educación sobre       │ │
│  │                         │      │   certificados         │ │
│  │ • Backup de claves      │      │                         │ │
│  └─────────────────────────┘      └─────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Capa 5: Controles de Sesión

```
┌─────────────────────────────────────────────────────────────┐
│                CONTROLES CAPA 5: SESIÓN                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PREVENTIVOS:                    DETECTIVOS:                │
│  ┌─────────────────────────┐      ┌─────────────────────────┐ │
│  │                         │      │                         │ │
│  │ • Tokens únicos         │      │ • Monitoreo de           │ │
│  │                         │      │   sesiones               │ │
│  │ • Timeouts automáticos  │      │ • Detección de           │ │
│  │                         │      │   sesiones              │ │
│  │ • Regeneración de IDs   │      │   concurrentes           │ │
│  │                         │      │                         │ │
│  │ • Encriptación de       │      │ • Alertas de            │ │
│  │   sesiones              │      │   desconexión           │ │
│  │                         │      │                         │ │
│  │ • Límites de sesión     │      │ • Análisis de            │ │
│  │                         │      │   comportamiento        │ │
│  └─────────────────────────┘      └─────────────────────────┘ │
│                                                             │
│  CORRECTIVOS:                     DISUASIVOS:               │
│  ┌─────────────────────────┐      ┌─────────────────────────┐ │
│  │                         │      │                         │ │
│  │ • Terminación de        │      │ • Notificaciones de      │ │
│  │   sesiones              │      │   sesión                │ │
│  │                         │      │                         │ │
│  │ • Bloqueo de usuarios   │      │ • Indicadores de        │ │
│  │                         │      │   actividad             │ │
│  │ • Logout forzado        │      │                         │ │
│  │                         │      │ • Advertencias de        │ │
│  │ • Limpieza de           │      │   timeout               │ │
│  │   sesiones              │      │                         │ │
│  └─────────────────────────┘      └─────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Capa 4: Controles de Transporte

```
┌─────────────────────────────────────────────────────────────┐
│              CONTROLES CAPA 4: TRANSPORTE                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PREVENTIVOS:                    DETECTIVOS:                │
│  ┌─────────────────────────┐      ┌─────────────────────────┐ │
│  │                         │      │                         │ │
│  │ • Firewalls de estado   │      │ • Monitoreo de          │ │
│  │                         │      │   conexiones            │ │
│  │ • SYN cookies           │      │ • Detección de          │ │
│  │                         │      │   SYN floods            │ │
│  │ • Rate limiting         │      │                         │ │
│  │                         │      │ • Análisis de           │ │
│  │ • Filtrado de puertos   │      │   patrones TCP          │ │
│  │                         │      │                         │ │
│  │ • IPS/IDS               │      │ • Alertas de            │ │
│  │                         │      │   conexiones            │ │
│  │ • Honeypots             │      │   sospechosas           │ │
│  └─────────────────────────┘      └─────────────────────────┘ │
│                                                             │
│  CORRECTIVOS:                     DISUASIVOS:               │
│  ┌─────────────────────────┐      ┌─────────────────────────┐ │
│  │                         │      │                         │ │
│  │ • Bloqueo automático    │      │ • Mensajes de           │ │
│  │                         │      │   conexión              │ │
│  │ • Rate limiting         │      │   rechazada             │ │
│  │   dinámico              │      │                         │ │
│  │                         │      │ • Indicadores de        │ │
│  │ • Terminación de        │      │   estado de             │ │
│  │   conexiones            │      │   conexión              │ │
│  │                         │      │                         │ │
│  │ • Recuperación de       │      │ • Advertencias de        │ │
│  │   servicios             │      │   límites               │ │
│  └─────────────────────────┘      └─────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Capa 3: Controles de Red

```
┌─────────────────────────────────────────────────────────────┐
│                CONTROLES CAPA 3: RED                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PREVENTIVOS:                    DETECTIVOS:                │
│  ┌─────────────────────────┐      ┌─────────────────────────┐ │
│  │                         │      │                         │ │
│  │ • Firewalls de red      │      │ • Monitoreo de          │ │
│  │                         │      │   tráfico               │ │
│  │ • Filtrado de paquetes  │      │ • Detección de          │ │
│  │                         │      │   anomalías             │ │
│  │ • BCP38 (RFC 2827)     │      │                         │ │
│  │                         │      │ • Análisis de          │ │
│  │ • Rate limiting         │      │   patrones IP           │ │
│  │                         │      │                         │ │
│  │ • DDoS protection       │      │ • Alertas de           │ │
│  │                         │      │   ataques              │ │
│  │ • VPNs                  │      │   distribuidos          │ │
│  └─────────────────────────┘      └─────────────────────────┘ │
│                                                             │
│  CORRECTIVOS:                     DISUASIVOS:               │
│  ┌─────────────────────────┐      ┌─────────────────────────┐ │
│  │                         │      │                         │ │
│  │ • Mitigación DDoS       │      │ • Mensajes de           │ │
│  │                         │      │   bloqueo               │ │
│  │ • Reenrutamiento        │      │                         │ │
│  │   automático            │      │ • Indicadores de        │ │
│  │                         │      │   estado de red         │ │
│  │ • Filtrado dinámico     │      │                         │ │
│  │                         │      │ • Advertencias de       │ │
│  │ • Recuperación de       │      │   límites de             │ │
│  │   servicios             │      │   ancho de banda        │ │
│  └─────────────────────────┘      └─────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Capa 2: Controles de Enlace de Datos

```
┌─────────────────────────────────────────────────────────────┐
│            CONTROLES CAPA 2: ENLACE DE DATOS                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PREVENTIVOS:                    DETECTIVOS:                │
│  ┌─────────────────────────┐      ┌─────────────────────────┐ │
│  │                         │      │                         │ │
│  │ • Port Security         │      │ • Monitoreo de          │ │
│  │                         │      │   dispositivos         │ │
│  │ • VLANs                 │      │ • Detección de          │ │
│  │                         │      │   dispositivos          │ │
│  │ • 802.1X                │      │   no autorizados        │ │
│  │                         │      │                         │ │
│  │ • ARP monitoring         │      │ • Análisis de           │ │
│  │                         │      │   tabla ARP             │ │
│  │ • DHCP Snooping         │      │                         │ │
│  │                         │      │ • Alertas de            │ │
│  │ • Encriptación WiFi     │      │   cambios MAC            │ │
│  └─────────────────────────┘      └─────────────────────────┘ │
│                                                             │
│  CORRECTIVOS:                     DISUASIVOS:               │
│  ┌─────────────────────────┐      ┌─────────────────────────┐ │
│  │                         │      │                         │ │
│  │ • Bloqueo de puertos    │      │ • Mensajes de           │ │
│  │                         │      │   acceso                │ │
│  │ • Aislamiento de        │      │   denegado              │ │
│  │   dispositivos          │      │                         │ │
│  │                         │      │ • Indicadores de        │ │
│  │ • Limpieza de tabla     │      │   estado de             │ │
│  │   ARP                   │      │   conexión              │ │
│  │                         │      │                         │ │
│  │ • Recuperación de       │      │ • Advertencias de       │ │
│  │   VLANs                 │      │   políticas             │ │
│  └─────────────────────────┘      └─────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Capa 1: Controles Físicos

```
┌─────────────────────────────────────────────────────────────┐
│                CONTROLES CAPA 1: FÍSICA                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PREVENTIVOS:                    DETECTIVOS:                │
│  ┌─────────────────────────┐      ┌─────────────────────────┐ │
│  │                         │      │                         │ │
│  │ • Control de acceso     │      │ • Cámaras de            │ │
│  │   físico                │      │   seguridad             │ │
│  │                         │      │                         │ │
│  │ • Cerraduras            │      │ • Sensores de           │ │
│  │   electromagnéticas     │      │   movimiento            │ │
│  │                         │      │                         │ │
│  │ • Cableado blindado     │      │ • Detección de          │ │
│  │                         │      │   desconexiones         │ │
│  │ • Jaulas de Faraday     │      │                         │ │
│  │                         │      │ • Monitoreo de          │ │
│  │ • Separación de redes   │      │   temperatura           │ │
│  │                         │      │                         │ │
│  │ • UPS y generadores     │      │ • Alertas de            │ │
│  │                         │      │   intrusión             │ │
│  └─────────────────────────┘      └─────────────────────────┘ │
│                                                             │
│  CORRECTIVOS:                     DISUASIVOS:               │
│  ┌─────────────────────────┐      ┌─────────────────────────┐ │
│  │                         │      │                         │ │
│  │ • Respuesta de          │      │ • Señales de             │ │
│  │   seguridad              │      │   advertencia           │ │
│  │                         │      │                         │ │
│  │ • Bloqueo automático    │      │ • Carteles de           │ │
│  │                         │      │   seguridad             │ │
│  │ • Recuperación de       │      │                         │ │
│  │   energía               │      │ • Indicadores de        │ │
│  │                         │      │   acceso                │ │
│  │ • Reparación de         │      │                         │ │
│  │   infraestructura       │      │ • Advertencias de       │ │
│  │                         │      │   consecuencias         │ │
│  └─────────────────────────┘      └─────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Estrategia de Defensa en Profundidad

### Diagrama: Capas de Defensa

```
┌─────────────────────────────────────────────────────────────┐
│                DEFENSA EN PROFUNDIDAD                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CAPA 7: APLICACIÓN                                        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ WAF • Validación • Autenticación • Sanitización     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CAPA 6: PRESENTACIÓN                                      │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ TLS 1.3 • Certificados • Encriptación • HSTS        │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CAPA 5: SESIÓN                                            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Tokens • Timeouts • Regeneración • Encriptación     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CAPA 4: TRANSPORTE                                        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Firewalls • SYN Cookies • Rate Limiting • IPS/IDS   │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CAPA 3: RED                                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Firewalls • Filtrado • DDoS Protection • VPNs      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CAPA 2: ENLACE                                            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Port Security • VLANs • 802.1X • ARP Monitoring   │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CAPA 1: FÍSICA                                            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Control de Acceso • Cableado • Separación • UPS     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Implementación de Controles

### Matriz de Priorización

```
┌─────────────────────────────────────────────────────────────┐
│                MATRIZ DE PRIORIZACIÓN                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ALTA PRIORIDAD:                    BAJA PRIORIDAD:        │
│  ┌─────────────────────────┐        ┌─────────────────────┐ │
│  │                         │        │                     │ │
│  │ • Firewalls             │        │ • Honeypots          │ │
│  │ • Encriptación          │        │ • Análisis forense  │ │
│  │ • Autenticación         │        │ • Auditoría          │ │
│  │ • Validación de        │        │ • Documentación      │ │
│  │   entrada               │        │                     │ │
│  │ • Monitoreo básico     │        │ • Reportes          │ │
│  │                         │        │                     │ │
│  └─────────────────────────┘        └─────────────────────┘ │
│                                                             │
│  MEDIA PRIORIDAD:                                           │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Segmentación de red                              │   │
│  │ • IDS/IPS                                          │   │
│  │ • Backup y recuperación                             │   │
│  │ • Educación de usuarios                            │   │
│  │ • Políticas de seguridad                           │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Monitoreo y Respuesta

### Sistema SIEM (Security Information and Event Management)

```
┌─────────────────────────────────────────────────────────────┐
│                    SISTEMA SIEM                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  FUENTES DE DATOS:                                         │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Firewalls         • Servidores                   │   │
│  │ • IDS/IPS          • Aplicaciones                  │   │
│  │ • Antivirus        • Bases de datos               │   │
│  │ • Endpoint         • Dispositivos de red          │   │
│  │   protection       • Sistemas de autenticación    │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  PROCESAMIENTO:                                            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Normalización de datos                           │   │
│  │ • Correlación de eventos                           │   │
│  │ • Análisis de patrones                             │   │
│  │ • Detección de anomalías                           │   │
│  │ • Generación de alertas                            │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  RESPUESTA:                                                │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Alertas automáticas                               │   │
│  │ • Respuesta automática                              │   │
│  │ • Escalamiento manual                               │   │
│  │ • Reportes y dashboards                             │   │
│  │ • Análisis forense                                  │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Mejores Prácticas

### Checklist de Implementación

```
┌─────────────────────────────────────────────────────────────┐
│            CHECKLIST DE IMPLEMENTACIÓN                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  FASE 1: FUNDAMENTOS                                        │
│  ☐ Inventario de activos                                  │
│  ☐ Evaluación de riesgos                                   │
│  ☐ Políticas de seguridad                                  │
│  ☐ Controles básicos (firewalls, encriptación)            │
│                                                             │
│  FASE 2: FORTALECIMIENTO                                   │
│  ☐ Segmentación de red                                    │
│  ☐ Autenticación multifactor                              │
│  ☐ Monitoreo básico                                       │
│  ☐ Backup y recuperación                                  │
│                                                             │
│  FASE 3: AVANZADO                                          │
│  ☐ IDS/IPS                                                │
│  ☐ SIEM                                                   │
│  ☐ Análisis de comportamiento                             │
│  ☐ Respuesta automática                                   │
│                                                             │
│  FASE 4: OPTIMIZACIÓN                                      │
│  ☐ Análisis forense                                       │
│  ☐ Threat hunting                                         │
│  ☐ Automatización avanzada                                │
│  ☐ Mejora continua                                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Conclusiones

La implementación efectiva de controles de seguridad requiere:

1. **Enfoque holístico**: Controles en todas las capas
2. **Priorización**: Implementar por impacto y facilidad
3. **Monitoreo continuo**: Detección en tiempo real
4. **Respuesta rápida**: Mitigación inmediata
5. **Mejora continua**: Evaluación y actualización regular

Los controles deben ser:
- **Proporcionados**: Adecuados al riesgo
- **Efectivos**: Logran el objetivo deseado
- **Eficientes**: No impactan negativamente el negocio
- **Sostenibles**: Mantenibles a largo plazo

