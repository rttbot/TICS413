## Guía de Respuestas Esperadas

Esta sección proporciona las respuestas correctas que los estudiantes deberían identificar durante el ejercicio. Sirve como referencia para el instructor y como herramienta de verificación para los grupos.

### Capas OSI:
- **Capa 1 (Física)**: Señales WiFi, cables, hardware físico de red
- **Capa 2 (Enlace)**: Direcciones MAC, switches, protocolos WiFi (WPA/WPA2)
- **Capa 3 (Red)**: Direcciones IP, routers, protocolos de enrutamiento
- **Capa 4 (Transporte)**: Puertos TCP/UDP, conexiones y sesiones de transporte
- **Capa 5 (Sesión)**: Sesiones de usuario, autenticación, protocolos como RPC
- **Capa 6 (Presentación)**: Encriptación, certificados SSL/TLS, formato de datos
- **Capa 7 (Aplicación)**: Aplicaciones web, bases de datos, protocolos HTTP/HTTPS

### Tipos de Ataques:
- **Interceptación**: Capturar y leer comunicaciones privadas
- **Suplantación**: Falsificar identidad de usuarios, dispositivos o servicios
- **Denegación de Servicio**: Interrumpir o bloquear servicios legítimos
- **Inyección**: Insertar código malicioso en aplicaciones o sistemas
- **Fuerza Bruta**: Probar múltiples combinaciones para romper autenticación
- **Propagación**: Extender malware automáticamente a través de la red

### Contramedidas Básicas:
- **Firewalls**: Bloquear tráfico no autorizado entre segmentos de red
- **Encriptación**: Proteger datos en tránsito y en reposo
- **Autenticación**: Verificar identidades antes de otorgar acceso
- **Monitoreo**: Detectar actividad sospechosa y comportamientos anómalos
- **Segmentación**: Aislar redes y sistemas críticos del resto de la red
- **Parches**: Corregir vulnerabilidades conocidas en software y sistemas

### Notas para el Instructor:
- Utilizar las preguntas de discusión para profundizar en cada tema
- Enfatizar la importancia de la defensa en profundidad
- Conectar las amenazas específicas de WiFi con los casos prácticos
- Relacionar los criterios de evaluación con los objetivos de aprendizaje

## Preguntas de Discusión

### 1. Análisis de Amenazas
- ¿Qué amenazas son más críticas para una empresa?
- ¿Cómo priorizarías las contramedidas?
- ¿Qué amenazas requieren respuesta inmediata?

### 2. Defensa en Profundidad
- ¿Cómo implementarías múltiples capas de protección?
- ¿Qué contramedidas son más efectivas por capa?
- ¿Cómo coordinar las defensas entre capas?

### 3. Redes Inalámbricas
- ¿Qué amenazas son específicas de WiFi?
- ¿Cómo proteger redes WiFi corporativas?
- ¿Qué diferencias hay con redes cableadas?

### 4. Detección y Respuesta
- ¿Cómo detectarías estas amenazas en tiempo real?
- ¿Qué herramientas necesitarías para monitoreo?
- ¿Cómo responderías a un incidente de seguridad?

## Criterios de Evaluación

### Análisis Técnico (40%)
- Identificación correcta de capas OSI
- Clasificación apropiada de tipos de ataque
- Propuesta de contramedidas relevantes

### Pensamiento Crítico (30%)
- Análisis de impacto y priorización
- Consideración de múltiples perspectivas
- Evaluación de efectividad de contramedidas

### Trabajo en Equipo (20%)
- Participación activa en discusiones
- Colaboración efectiva con el grupo
- Resolución de conflictos de opinión

### Presentación (10%)
- Claridad en la exposición de ideas
- Organización lógica de la información
- Respuestas a preguntas del instructor

## Escenarios de Aplicación

### Escenario 1: Pequeña Empresa
- 20 empleados
- Red WiFi para invitados
- Servidor web básico
- **Pregunta**: ¿Qué amenazas son más críticas?

### Escenario 2: Hospital
- Sistemas médicos críticos
- Datos de pacientes confidenciales
- Redes separadas por departamento
- **Pregunta**: ¿Cómo proteger cada sistema?

### Escenario 3: Universidad
- Red WiFi pública
- Estudiantes con dispositivos personales
- Investigación académica
- **Pregunta**: ¿Qué controles implementarías?

## Conclusiones del Ejercicio

Este ejercicio demuestra que:

1. **La seguridad en redes requiere comprensión de múltiples capas**
2. **Las amenazas pueden operar en diferentes niveles simultáneamente**
3. **La defensa en profundidad es esencial para protección efectiva**
4. **El monitoreo continuo es crucial para detectar amenazas**
5. **La respuesta rápida puede minimizar el impacto de ataques**

**Nota**: Este ejercicio se centra en conceptos básicos de seguridad en redes. Los temas avanzados como análisis forense, malware sofisticado y APTs se cubrirán en unidades posteriores del curso.

El ejercicio fomenta el aprendizaje activo y la comprensión profunda de los conceptos de seguridad de redes.


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
│  │   8   │ Caso 3          │ Beacon Flooding   │ WIDS/WIPS  │ │
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

### Ejercicios de Conexión por Caso

#### Caso 1: E-commerce (TechStore.cl)

**Tarjetas Relacionadas:** 1, 2, 3, 5, 6

**Ejercicio de Aplicación:**
```
┌─────────────────────────────────────────────────────────────┐
│                EJERCICIO CASO 1: E-COMMERCE                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PREGUNTA: ¿Cómo aplicarías las contramedidas de las       │
│  tarjetas 1, 2, 3, 5 y 6 para proteger TechStore.cl?       │
│                                                             │
│  ANÁLISIS REQUERIDO:                                        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ 1. TARJETA 1 (Interceptación WiFi):                │   │
│  │    • Implementar WPA3 en red corporativa           │   │
│  │    • Monitoreo continuo de usuarios conectados      │   │
│  │    • WIDS/WIPS para detectar sniffing              │   │
│  │                                                     │   │
│  │ 2. TARJETA 2 (Evil Twin):                          │   │
│  │    • Verificar SSID oficial "TechStore_Corp"       │   │
│  │    • VPN obligatorio para empleados                │   │
│  │    • Certificados SSL en todas las conexiones      │   │
│  │                                                     │   │
│  │ 3. TARJETA 3 (SYN Flood):                          │   │
│  │    • SYN Cookies en servidores web                 │   │
│  │    • Rate limiting por IP                           │   │
│  │    • DDoS protection service                        │   │
│  │                                                     │   │
│  │ 4. TARJETA 5 (SQL Injection):                      │   │
│  │    • WAF para bloquear inyecciones                 │   │
│  │    • Prepared statements en código                 │   │
│  │    • Input validation en formularios               │   │
│  │                                                     │   │
│  │ 5. TARJETA 6 (ARP Poisoning):                      │   │
│  │    • ARP monitoring en switches                    │   │
│  │    • VLANs para segmentar redes                    │   │
│  │    • Port security en switches                     │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### Caso 2: Hospital (Hospital Regional San José)

**Tarjetas Relacionadas:** 7, 2

**Ejercicio de Aplicación:**
```
┌─────────────────────────────────────────────────────────────┐
│                EJERCICIO CASO 2: HOSPITAL                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PREGUNTA: ¿Por qué son críticos los ataques de las        │
│  tarjetas 7 y 2 en un entorno hospitalario?                │
│                                                             │
│  ANÁLISIS REQUERIDO:                                        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ 1. TARJETA 7 (WiFi Jamming):                        │   │
│  │    • CRÍTICO: Monitores de UCI desconectados        │   │
│  │    • SOLUCIÓN: Backup cableado para equipos médicos │   │
│  │    • DETECCIÓN: Monitoreo RF continuo               │   │
│  │    • PLAN: Protocolos de emergencia médica          │   │
│  │                                                     │   │
│  │ 2. TARJETA 2 (Evil Twin):                          │   │
│  │    • CRÍTICO: Datos de pacientes interceptados      │   │
│  │    • SOLUCIÓN: Red WiFi aislada para equipos médicos│   │
│  │    • VERIFICACIÓN: SSID oficial "Hospital_Med"     │   │
│  │    • ENCRIPTACIÓN: VPN para acceso remoto           │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### Caso 3: Universidad (Universidad Tecnológica del Sur)

**Tarjetas Relacionadas:** 8, 3, 4

**Ejercicio de Aplicación:**
```
┌─────────────────────────────────────────────────────────────┐
│                EJERCICIO CASO 3: UNIVERSIDAD               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PREGUNTA: ¿Cómo balancearías seguridad y accesibilidad   │
│  aplicando las contramedidas de las tarjetas 8, 3 y 4?     │
│                                                             │
│  ANÁLISIS REQUERIDO:                                        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ 1. TARJETA 8 (Beacon Flooding):                     │   │
│  │    • PROBLEMA: Múltiples SSIDs falsos              │   │
│  │    • SOLUCIÓN: WIDS/WIPS + Rate limiting              │   │
│  │    • BALANCE: Permitir redes legítimas                 │   │
│  │    • EDUCACIÓN: Informar a estudiantes                 │   │
│  │                                                     │   │
│  │ 2. TARJETA 3 (DDoS):                               │   │
│  │    • PROBLEMA: Servidores académicos caídos        │   │
│  │    • SOLUCIÓN: DDoS protection + Rate limiting        │   │
│  │    • BALANCE: Mantener acceso para estudiantes        │   │
│  │    • MONITOREO: Detectar patrones anómalos            │   │
│  │                                                     │   │
│  │ 3. TARJETA 4 (Auth Server):                        │   │
│  │    • PROBLEMA: Servidor de autenticación sobrecargado│   │
│  │    • SOLUCIÓN: Rate limiting + Timeouts               │   │
│  │    • BALANCE: No bloquear usuarios legítimos           │   │
│  │    • ESCALABILIDAD: Múltiples servidores auth         │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### Caso 4: TelecomLatina (Infraestructura Crítica)

**Tarjetas Relacionadas:** 7, 6, 3

**Ejercicio de Aplicación:**
```
┌─────────────────────────────────────────────────────────────┐
│                EJERCICIO CASO 4: TELECOMLATINA             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PREGUNTA: ¿Qué contramedidas de las tarjetas 7, 6 y 3     │
│  son más críticas para infraestructura nacional?           │
│                                                             │
│  ANÁLISIS REQUERIDO:                                        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ 1. TARJETA 7 (WiFi Jamming):                        │   │
│  │    • CRÍTICO: 80% usuarios sin Internet             │   │
│  │    • PRIORIDAD: Backup cableado inmediato              │   │
│  │    • DETECCIÓN: Monitoreo RF nacional                   │   │
│  │    • COORDINACIÓN: Otros ISP afectados                 │   │
│  │                                                     │   │
│  │ 2. TARJETA 6 (ARP Poisoning):                       │   │
│  │    • CRÍTICO: Tráfico redirigido incorrectamente   │   │
│  │    • PRIORIDAD: ARP monitoring en routers principales │   │
│  │    • SEGMENTACIÓN: VLANs críticas                      │   │
│  │    • AISLAMIENTO: Redes de servicios críticos          │   │
│  │                                                     │   │
│  │ 3. TARJETA 3 (DDoS):                               │   │
│  │    • CRÍTICO: Centros de datos offline              │   │
│  │    • PRIORIDAD: DDoS protection services               │   │
│  │    • ESCALABILIDAD: Múltiples proveedores             │   │
│  │    • COORDINACIÓN: CSIRT Chile                         │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Evaluación de la Fase 5

#### Criterios de Evaluación:

| Criterio | Puntuación | Descripción |
|----------|------------|-------------|
| **Identificación de Conexiones** | 30% | Correcta relación entre tarjetas y casos |
| **Aplicación de Contramedidas** | 30% | Propuesta realista de implementación |
| **Análisis de Contexto** | 20% | Comprensión de especificidades del caso |
| **Pensamiento Estratégico** | 20% | Consideración de prioridades y recursos |

#### Rúbrica de Evaluación:

```
┌─────────────────────────────────────────────────────────────┐
│                RÚBRICA FASE 5                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  EXCELENTE (90-100%):                                      │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Identifica todas las conexiones relevantes       │   │
│  │ • Propone contramedidas específicas y realistas     │   │
│  │ • Considera el contexto específico del caso        │   │
│  │ • Demuestra pensamiento estratégico                 │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  BUENO (80-89%):                                           │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Identifica la mayoría de conexiones              │   │
│  │ • Propone contramedidas apropiadas                  │   │
│  │ • Considera algunos aspectos del contexto          │   │
│  │ • Muestra pensamiento básico                        │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  SATISFACTORIO (70-79%):                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ • Identifica algunas conexiones                    │   │
│  │ • Propone contramedidas básicas                     │   │
│  │ • Considera limitadamente el contexto              │   │
│  │ • Pensamiento superficial                           │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Beneficios de la Fase 5

1. **Aplicación Práctica:** Los estudiantes ven cómo la teoría se aplica a situaciones reales
2. **Pensamiento Crítico:** Desarrollan habilidades de análisis y síntesis
3. **Comprensión Profunda:** Entienden la complejidad de los ataques reales
4. **Preparación Profesional:** Se preparan para situaciones laborales reales
5. **Integración de Conocimientos:** Conectan diferentes conceptos aprendidos

### Notas para Docentes

- **Flexibilidad:** Los estudiantes pueden identificar conexiones adicionales válidas
- **Contexto:** Considerar el nivel de experiencia de los estudiantes
- **Tiempo:** Ajustar el tiempo según la complejidad del grupo
- **Recursos:** Proporcionar acceso a los casos prácticos durante el ejercicio
