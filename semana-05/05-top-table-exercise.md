# Top Table Exercise: Simulación de Seguridad en Redes

## Objetivo del Ejercicio

Este ejercicio simula un escenario real de seguridad en redes donde los estudiantes deben identificar amenazas, clasificarlas por capas OSI y proponer contramedidas efectivas. El ejercicio fomenta el pensamiento crítico y la aplicación práctica de los conceptos aprendidos.

## Materiales Necesarios

- Tarjetas de amenazas (12 tarjetas)
- Tabla de clasificación (1 por grupo)


## Estructura del Ejercicio

### Fase 1: Preparación (10 minutos)
- Formación de grupos de 4-5 estudiantes

- Explicación de reglas y objetivos

### Fase 2: Análisis Individual (15 minutos)
- Cada estudiante analiza 2-3 tarjetas de amenazas
- Identifica capa OSI, tipo de ataque y contramedidas básicas

### Fase 3: Discusión Grupal (20 minutos)
- Compartir análisis con el grupo
- Llenar tabla de clasificación grupal
- Discutir diferencias y llegar a consenso

### Fase 4: Presentación y Debate (15 minutos)
- Cada grupo presenta sus hallazgos
- Debate sobre contramedidas más efectivas
- Discusión sobre defensa en profundidad

## Tarjetas de Amenazas

### Tarjeta 1: Ataque de Interceptación WiFi

```
┌─────────────────────────────────────────────────────────────┐
│                    TARJETA 1                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ESCENARIO:                                                 │
│  Un atacante se conecta a la red WiFi de una empresa        │
│  y comienza a capturar todo el tráfico de red.             │
│                                                             │
│  SÍNTOMAS:                                                  │
│  • Usuario desconocido conectado a la red                    │
│  • Tráfico de red inusualmente alto                        │
│  • Dispositivos experimentan lentitud                       │
│                                                             │
│  PREGUNTA: ¿Qué capa OSI está siendo atacada?               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Tarjeta 2: Suplantación de Punto de Acceso

```
┌─────────────────────────────────────────────────────────────┐
│                    TARJETA 2                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ESCENARIO:                                                 │
│  Los empleados ven una red WiFi llamada "Empresa_Gratis"   │
│  junto a la red oficial de la empresa.                     │
│                                                             │
│  SÍNTOMAS:                                                  │
│  • Nueva red WiFi con nombre similar                        │
│  • Usuarios se conectan accidentalmente                    │
│  • Datos sensibles aparecen en lugares extraños            │
│                                                             │
│  PREGUNTA: ¿Qué tipo de ataque es este?                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Tarjeta 3: Sobreflujo de Conexiones

```
┌─────────────────────────────────────────────────────────────┐
│                    TARJETA 3                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ESCENARIO:                                                 │
│  El servidor web de la empresa deja de responder            │
│  porque recibe miles de solicitudes de conexión.           │
│                                                             │
│  SÍNTOMAS:                                                  │
│  • Servidor no responde a usuarios legítimos                │
│  • Conexiones quedan "colgadas"                             │
│  • Recursos del servidor agotados                           │
│                                                             │
│  PREGUNTA: ¿En qué capa OSI ocurre este ataque?             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Tarjeta 4: Robo de Sesiones

```
┌─────────────────────────────────────────────────────────────┐
│                    TARJETA 4                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ESCENARIO:                                                 │
│  Un usuario reporta que alguien accedió a su cuenta         │
│  bancaria sin su autorización.                             │
│                                                             │
│  SÍNTOMAS:                                                  │
│  • Actividad sospechosa en la cuenta                       │
│  • Sesión activa desde ubicación desconocida                │
│  • Usuario no cerró sesión en computadora pública          │
│                                                             │
│  PREGUNTA: ¿Qué capa OSI maneja las sesiones?               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Tarjeta 5: Inyección de Código Web

```
┌─────────────────────────────────────────────────────────────┐
│                    TARJETA 5                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ESCENARIO:                                                 │
│  Un formulario web acepta código malicioso que             │
│  permite acceder a la base de datos.                       │
│                                                             │
│  SÍNTOMAS:                                                  │
│  • Mensajes de error extraños en la web                    │
│  • Datos de usuarios aparecen donde no deberían            │
│  • Comportamiento inesperado del sitio web                  │
│                                                             │
│  PREGUNTA: ¿En qué capa OSI ocurren los ataques web?       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Tarjeta 6: Falsificación de Direcciones

```
┌─────────────────────────────────────────────────────────────┐
│                    TARJETA 6                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ESCENARIO:                                                 │
│  Los logs de red muestran paquetes que parecen             │
│  venir de direcciones IP internas pero no existen.         │
│                                                             │
│  SÍNTOMAS:                                                  │
│  • Paquetes con IPs internas falsas                        │
│  • Tráfico sospechoso desde "dentro" de la red             │
│  • Firewall confundido sobre origen del tráfico            │
│                                                             │
│  PREGUNTA: ¿Qué capa OSI maneja las direcciones IP?         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Tarjeta 7: Bloqueo de Señales WiFi

```
┌─────────────────────────────────────────────────────────────┐
│                    TARJETA 7                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ESCENARIO:                                                 │
│  Todos los dispositivos WiFi de la oficina pierden          │
│  conexión simultáneamente sin razón aparente.              │
│                                                             │
│  SÍNTOMAS:                                                  │
│  • Conexiones WiFi se cortan de repente                    │
│  • Dispositivos no pueden reconectarse                     │
│  • Interferencia en la banda de frecuencia WiFi            │
│                                                             │
│  PREGUNTA: ¿Qué capa OSI maneja las señales físicas?       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Tarjeta 8: Propagación de Malware

```
┌─────────────────────────────────────────────────────────────┐
│                    TARJETA 8                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ESCENARIO:                                                 │
│  Un virus se propaga automáticamente entre computadoras     │
│  de la red sin que los usuarios hagan nada.                │
│                                                             │
│  SÍNTOMAS:                                                  │
│  • Múltiples computadoras infectadas                       │
│  │ • Propagación automática por la red                    │
│  │ • Uso excesivo de ancho de banda                        │
│  │ • Comportamiento extraño en dispositivos                │
│  │                                                         │
│  │ PREGUNTA: ¿Qué capas OSI puede usar el malware?         │
│  │                                                         │
│  └─────────────────────────────────────────────────────────┘
```

### Tarjeta 9: Interceptación de Comunicaciones

```
┌─────────────────────────────────────────────────────────────┐
│                    TARJETA 9                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ESCENARIO:                                                 │
│  Un atacante se posiciona entre dos dispositivos            │
│  que se comunican y puede ver todos los mensajes.          │
│                                                             │
│  SÍNTOMAS:                                                  │
│  • Comunicaciones interceptadas                            │
│  • Datos sensibles comprometidos                           │
│  • Certificados SSL inválidos                              │
│                                                             │
│  PREGUNTA: ¿Qué capa OSI maneja la encriptación?           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Tarjeta 10: Envenenamiento de Tabla ARP

```
┌─────────────────────────────────────────────────────────────┐
│                    TARJETA 10                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ESCENARIO:                                                 │
│  Los dispositivos de la red local envían todo su tráfico   │
│  a una computadora que no es el gateway real.             │
│                                                             │
│  SÍNTOMAS:                                                  │
│  • Tráfico redirigido incorrectamente                     │
│  • Lentitud en la red local                                │
│  • Comunicaciones interceptadas                            │
│                                                             │
│  PREGUNTA: ¿Qué capa OSI maneja las direcciones MAC?       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Tarjeta 11: Escaneo de Puertos

```
┌─────────────────────────────────────────────────────────────┐
│                    TARJETA 11                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ESCENARIO:                                                 │
│  Un sistema intenta conectarse a múltiples puertos          │
│  de los servidores de la empresa.                          │
│                                                             │
│  SÍNTOMAS:                                                  │
│  • Múltiples intentos de conexión                          │
│  • Puertos específicos siendo probados                     │
│  • Actividad sospechosa en logs de red                     │
│                                                             │
│  PREGUNTA: ¿Qué capa OSI maneja los puertos?               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Tarjeta 12: Ataque de Fuerza Bruta

```
┌─────────────────────────────────────────────────────────────┐
│                    TARJETA 12                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ESCENARIO:                                                 │
│  Un atacante intenta adivinar contraseñas probando          │
│  miles de combinaciones diferentes.                       │
│                                                             │
│  SÍNTOMAS:                                                  │
│  • Múltiples intentos de login fallidos                     │
│  • Cuentas bloqueadas por seguridad                        │
│  • Actividad inusual en servidores de autenticación        │
│                                                             │
│  PREGUNTA: ¿En qué capa OSI ocurre la autenticación?        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Tabla de Clasificación Grupal

```
┌─────────────────────────────────────────────────────────────┐
│                TABLA DE CLASIFICACIÓN GRUPAL                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  TARJETA │ CAPA OSI │ TIPO DE ATAQUE │ CONTRAMEDIDAS        │
│  ┌───────┼─────────┼───────────────┼─────────────────────┐ │
│  │   1   │         │               │                      │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┤ │
│  │   2   │         │               │                      │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┤ │
│  │   3   │         │               │                      │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┤ │
│  │   4   │         │               │                      │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┤ │
│  │   5   │         │               │                      │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┤ │
│  │   6   │         │               │                      │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┤ │
│  │   7   │         │               │                      │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┤ │
│  │   8   │         │               │                      │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┤ │
│  │   9   │         │               │                      │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┤ │
│  │  10   │         │               │                      │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┤ │
│  │  11   │         │               │                      │ │
│  ├───────┼─────────┼───────────────┼─────────────────────┤ │
│  │  12   │         │               │                      │ │
│  └───────┴─────────┴───────────────┴─────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Fase 5: Conexión con Casos Prácticos

### Objetivo de la Fase 5

Esta fase permite a los estudiantes aplicar los conocimientos adquiridos en las tarjetas a situaciones reales y complejas, desarrollando habilidades de análisis crítico y pensamiento estratégico.

### Instrucciones para la Fase 5

1. **Asignación de Casos:** Cada grupo recibe uno de los casos prácticos de `04-casos-practicos.md`
2. **Análisis de Conexión:** Identificar qué tarjetas se relacionan con los ataques del caso asignado
3. **Aplicación de Contramedidas:** Proponer cómo aplicar las contramedidas de las tarjetas al caso real
4. **Presentación Integrada:** Explicar la relación entre teoría (tarjetas) y práctica (casos)

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
