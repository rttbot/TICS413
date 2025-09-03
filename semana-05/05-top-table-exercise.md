# Top Table Exercise: Simulación de Seguridad en Redes

## Objetivo del Ejercicio

Este ejercicio simula un escenario real de seguridad en redes donde los estudiantes deben identificar amenazas, clasificarlas por capas OSI y proponer contramedidas efectivas. El ejercicio fomenta el pensamiento crítico y la aplicación práctica de los conceptos aprendidos.

## Materiales Necesarios

- Tarjetas de amenazas (12 tarjetas)
- Tabla de clasificación (1 por grupo)
- Marcadores y post-its
- Cronómetro
- Pizarra o papelógrafo para discusión

## Estructura del Ejercicio

### Fase 1: Preparación (10 minutos)
- Formación de grupos de 4-5 estudiantes
- Distribución de materiales
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

## Guía de Respuestas Esperadas

### Capas OSI:
- **Capa 1 (Física)**: Señales WiFi, cables, hardware
- **Capa 2 (Enlace)**: Direcciones MAC, switches, WiFi
- **Capa 3 (Red)**: Direcciones IP, routers, enrutamiento
- **Capa 4 (Transporte)**: Puertos, conexiones TCP/UDP
- **Capa 5 (Sesión)**: Sesiones de usuario, autenticación
- **Capa 6 (Presentación)**: Encriptación, certificados SSL
- **Capa 7 (Aplicación)**: Aplicaciones web, bases de datos

### Tipos de Ataques:
- **Interceptación**: Capturar comunicaciones
- **Suplantación**: Falsificar identidad o servicios
- **Denegación de Servicio**: Interrumpir servicios
- **Inyección**: Insertar código malicioso
- **Fuerza Bruta**: Probar múltiples combinaciones
- **Propagación**: Extender malware automáticamente

### Contramedidas Básicas:
- **Firewalls**: Bloquear tráfico no autorizado
- **Encriptación**: Proteger datos en tránsito
- **Autenticación**: Verificar identidades
- **Monitoreo**: Detectar actividad sospechosa
- **Segmentación**: Aislar redes y sistemas
- **Parches**: Corregir vulnerabilidades

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
