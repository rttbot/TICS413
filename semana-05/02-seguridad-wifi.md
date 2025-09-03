# Seguridad en Redes Inalámbricas (WiFi)

## Introducción

Las redes inalámbricas presentan desafíos únicos de seguridad debido a su naturaleza de transmisión por radio. A diferencia de las redes cableadas, donde el acceso físico está limitado, las señales WiFi pueden ser interceptadas por cualquier dispositivo dentro del rango de transmisión.

## Características Únicas de las Redes WiFi

### Diagrama: Diferencias entre Redes Cableadas e Inalámbricas

```
┌─────────────────────────────────────────────────────────────┐
│              REDES CABLEADAS vs INALÁMBRICAS                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  REDES CABLEADAS:                    REDES INALÁMBRICAS:   │
│  ┌─────────────────┐                ┌─────────────────┐   │
│  │                 │                │                 │   │
│  │  Acceso físico  │                │  Acceso por      │   │
│  │  requerido      │                │  radio (sin      │   │
│  │                 │                │  barreras       │   │
│  │  Señal          │                │  físicas)        │   │
│  │  contenida      │                │                 │   │
│  │  en cable       │                │  Señal se        │   │
│  │                 │                │  propaga en      │   │
│  │  Control de     │                │  todas las       │   │
│  │  acceso         │                │  direcciones     │   │
│  │  físico         │                │                 │   │
│  │  Menor          │                │  Interceptación  │   │
│  │  vulnerabilidad │                │  fácil           │   │
│  └─────────────────┘                └─────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Amenazas Específicas a Redes WiFi

### 1. Evil Twin Attack

```
┌─────────────────────────────────────────────────────────────┐
│                    EVIL TWIN ATTACK                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  USUARIO              ATACANTE           PUNTO DE ACCESO    │
│     │                    │                    │           │
│     │ 1. Busca redes     │                    │           │
│     │    WiFi            │                    │           │
│     │                    │                    │           │
│     │ 2. Ve "Café_WiFi"  │                    │           │
│     │    (legítimo)      │                    │           │
│     │                    │                    │           │
│     │ 3. Atacante crea   │                    │           │
│     │    "Café_WiFi"     │                    │           │
│     │    (falso)         │                    │           │
│     │                    │                    │           │
│     │ 4. Usuario se      │                    │           │
│     │    conecta al      │                    │           │
│     │    falso           │                    │           │
│     │                    │                    │           │
│     │ 5. Atacante       │                    │           │
│     │    intercepta      │                    │           │
│     │    todo tráfico    │                    │           │
│     │                    │                    │           │
└─────────────────────────────────────────────────────────────┘
```

**Características del Ataque:**
- Punto de acceso falso con mismo SSID
- Señal más fuerte que la legítima
- Interceptación completa del tráfico
- Robo de credenciales y datos

**Contramedidas:**
- Verificar certificados SSL/TLS
- Usar VPNs (Virtual Private Network - Red Privada Virtual) para tráfico sensible
  - **Analogía:** Como un túnel privado y seguro que conecta tu dispositivo directamente con el servidor de destino, evitando que otros en la red WiFi puedan ver tu tráfico
- Configurar alertas para nuevas redes
- Educar a usuarios sobre riesgos

### 2. Deauthentication Attack

```
┌─────────────────────────────────────────────────────────────┐
│                DEAUTHENTICATION ATTACK                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  DISPOSITIVO           ATACANTE           PUNTO DE ACCESO   │
│     │                    │                    │          │
│     │ 1. Conectado        │                    │          │
│     │    normalmente      │                    │          │
│     │                    │                    │          │
│     │ 2. Atacante envía  │                    │          │
│     │    frames de        │                    │          │
│     │    desautenticación │                    │          │
│     │    falsos           │                    │          │
│     │                    │                    │          │
│     │ 3. Dispositivo     │                    │          │
│     │    se desconecta    │                    │          │
│     │    forzadamente     │                    │          │
│     │                    │                    │          │
│     │ 4. Interrupción    │                    │          │
│     │    de servicio      │                    │          │
│     │                    │                    │          │
│     │ 5. Ataque puede    │                    │          │
│     │    ser continuo     │                    │          │
│     │                    │                    │          │
└─────────────────────────────────────────────────────────────┘
```

**Características del Ataque:**
- Frames de desautenticación falsos
- Desconexión forzada de dispositivos
- Interrupción de servicios
- Ataque de denegación de servicio

**Contramedidas:**
- Detección de anomalías
- Autenticación robusta (WPA3)
- Monitoreo de patrones de desconexión
- Reconexión automática segura

### 3. KRACK (Key Reinstallation Attack)

```
┌─────────────────────────────────────────────────────────────┐
│                    KRACK ATTACK                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CLIENTE              ATACANTE           PUNTO DE ACCESO   │
│     │                    │                    │          │
│     │ 1. Inicia          │                    │          │
│     │    handshake       │                    │          │
│     │    WPA2            │                    │          │
│     │                    │                    │          │
│     │ 2. Atacante        │                    │          │
│     │    intercepta       │                    │          │
│     │    handshake       │                    │          │
│     │                    │                    │          │
│     │ 3. Manipula         │                    │          │
│     │    mensajes del     │                    │          │
│     │    handshake        │                    │          │
│     │                    │                    │          │
│     │ 4. Fuerza          │                    │          │
│     │    reinstalación    │                    │          │
│     │    de claves        │                    │          │
│     │                    │                    │          │
│     │ 5. Compromete      │                    │          │
│     │    encriptación     │                    │          │
│     │                    │                    │          │
└─────────────────────────────────────────────────────────────┘
```

**Características del Ataque:**
- Vulnerabilidad en WPA2
- Manipulación del handshake de 4 vías
- Reinstalación forzada de claves
- Compromiso de encriptación

**Contramedidas:**
- Actualizar dispositivos con parches
- Usar WPA3 cuando sea posible
- Implementar VPNs para tráfico crítico
- Monitoreo de conexiones sospechosas

## Estándares de Seguridad WiFi

### Comparación de Protocolos

```
┌─────────────────────────────────────────────────────────────┐
│              EVOLUCIÓN DE PROTOCOLOS WIFI                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  WEP (1997)           WPA (2003)        WPA2 (2004)        │
│  ┌─────────────┐      ┌─────────────┐    ┌─────────────┐    │
│  │             │      │             │    │             │    │
│  │ RC4 (40/104 │      │ TKIP        │    │ CCMP/AES    │    │
│  │ bits)       │      │             │    │             │    │
│  │             │      │             │    │             │    │
│  │ Vulnerable  │      │ Mejorado    │    │ Robusto     │    │
│  │ a ataques   │      │ sobre WEP   │    │ y seguro    │    │
│  │             │      │             │    │             │    │
│  │ NO USAR     │      │ Transición  │    │ Estándar    │    │
│  │             │      │             │    │ actual      │    │
│  └─────────────┘      └─────────────┘    └─────────────┘    │
│                                                             │
│  WPA3 (2018)                                                │
│  ┌─────────────┐                                            │
│  │             │                                            │
│  │ AES-256     │                                            │
│  │             │                                            │
│  │ Forward     │                                            │
│  │ Secrecy     │                                            │
│  │             │                                            │
│  │ Individual  │                                            │
│  │ Encryption  │                                            │
│  └─────────────┘                                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Explicación Detallada de Protocolos WiFi:**

```
┌─────────────────────────────────────────────────────────────┐
│                EXPLICACIÓN DE PROTOCOLOS WIFI               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  WEP (Wired Equivalent Privacy - 1997):                    │
│  • RC4 (40/104 bits): Algoritmo de encriptación débil      │
│  • Vulnerable a ataques: Fácil de romper en minutos        │
│  • NO USAR: Completamente inseguro, obsoleto               │
│  • Problemas: Claves estáticas, IVs débiles, sin autenticación │
│                                                             │
│  WPA (WiFi Protected Access - 2003):                       │
│  • TKIP (Temporal Key Integrity Protocol): Mejora sobre WEP │
│  • Mejorado sobre WEP: Claves dinámicas, MIC para integridad │
│  • Transición: Protocolo temporal hasta WPA2               │
│  • Limitaciones: Aún vulnerable a algunos ataques         │
│                                                             │
│  WPA2 (WiFi Protected Access 2 - 2004):                    │
│  • CCMP/AES: Encriptación fuerte con AES-128               │
│  • Robusto y seguro: Estándar actual de facto             │
│  • Estándar actual: Ampliamente implementado              │
│  • Vulnerabilidades: KRACK (2017), pero sigue siendo seguro │
│                                                             │
│  WPA3 (WiFi Protected Access 3 - 2018):                    │
│  • AES-256: Encriptación más fuerte                        │
│  • Forward Secrecy: Claves únicas por sesión               │
│  • Individual Encryption: Cada dispositivo tiene su propia │
│    encriptación, incluso en redes abiertas                 │
│  • Más seguro: Protección contra ataques offline           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Comparación de Seguridad:**

```
┌─────────────────────────────────────────────────────────────┐
│                COMPARACIÓN DE SEGURIDAD                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  NIVEL DE SEGURIDAD:                                        │
│  WEP:    ❌❌❌❌❌ (0/5) - Completamente inseguro           │
│  WPA:    ⚠️⚠️⚠️❌❌ (3/5) - Mejor que WEP, pero débil      │
│  WPA2:   ✅✅✅✅⚠️ (4/5) - Seguro, con algunas vulnerabilidades │
│  WPA3:   ✅✅✅✅✅ (5/5) - Máxima seguridad disponible     │
│                                                             │
│  VULNERABILIDADES CONOCIDAS:                                │
│  WEP:    • Ataques de fuerza bruta                          │
│          • Análisis estadístico de tráfico                 │
│          • Inyección de paquetes                            │
│                                                             │
│  WPA:    • Ataques de diccionario                           │
│          • Vulnerabilidades en TKIP                         │
│          • Algunos ataques de fuerza bruta                 │
│                                                             │
│  WPA2:   • KRACK (Key Reinstallation Attack)                │
│          • Ataques de diccionario (contraseñas débiles)    │
│          • Evil Twin attacks                                │
│                                                             │
│  WPA3:   • Pocas vulnerabilidades conocidas                │
│          • Resistente a ataques offline                     │
│          • Protección contra ataques de diccionario        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Recomendaciones de Uso:**

```
┌─────────────────────────────────────────────────────────────┐
│                RECOMENDACIONES DE USO                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PARA USUARIOS DOMÉSTICOS:                                  │
│  • Usar WPA3 si está disponible                            │
│  • WPA2 como mínimo aceptable                              │
│  • NUNCA usar WEP o WPA                                    │
│  • Contraseñas fuertes (mínimo 12 caracteres)              │
│                                                             │
│  PARA EMPRESAS:                                            │
│  • Implementar WPA3-Enterprise                             │
│  • Usar autenticación 802.1X                               │
│  • Certificados digitales para autenticación               │
│  • Segmentación de redes por departamentos                │
│                                                             │
│  PARA DISPOSITIVOS ANTIGUOS:                               │
│  • Actualizar firmware si es posible                       │
│  • Considerar reemplazo si no soporta WPA2+                │
│  • Usar redes separadas para dispositivos IoT             │
│  • Monitoreo adicional de seguridad                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Autenticación 802.1X

```
┌─────────────────────────────────────────────────────────────┐
│                    AUTENTICACIÓN 802.1X                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  SUPPLICANTE         AUTENTICADOR      SERVIDOR DE          │
│  (Cliente)          (AP)              AUTENTICACIÓN        │
│     │                    │              │                  │
│     │ 1. Solicita         │              │                  │
│     │    acceso           │              │                  │
│     │                    │              │                  │
│     │ 2. Envía           │              │                  │
│     │    credenciales     │              │                  │
│     │                    │              │                  │
│     │ 3. Reenvía         │              │                  │
│     │    credenciales     │              │                  │
│     │                    │              │                  │
│     │ 4. Verifica        │              │                  │
│     │    credenciales     │              │                  │
│     │                    │              │                  │
│     │ 5. Respuesta       │              │                  │
│     │    de éxito        │              │                  │
│     │                    │              │                  │
│     │ 6. Permite         │              │                  │
│     │    acceso           │              │                  │
│     │                    │              │                  │
└─────────────────────────────────────────────────────────────┘
```

## Medidas de Seguridad WiFi

### 1. Ocultación de Señales

```
┌─────────────────────────────────────────────────────────────┐
│                TÉCNICAS DE OCULTACIÓN                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  TÉCNICA                    DESCRIPCIÓN                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ Desactivar broadcast SSID                          │   │
│  │ • Oculta nombre de red                             │   │
│  │ • No aparece en lista de redes                     │   │
│  │                                                     │   │
│  │ Nombres crípticos                                  │   │
│  │ • Evita nombres descriptivos                      │   │
│  │ • No revela organización                          │   │
│  │                                                     │   │
│  │ Reducir potencia                                   │   │
│  │ • Limita alcance de señal                          │   │
│  │ • Reduce superficie de ataque                      │   │
│  │                                                     │   │
│  │ Ubicación estratégica                              │   │
│  │ • APs (Access Points - Puntos de Acceso) en interior    │   │
│  │ • Alejados de ventanas                             │   │
│  │                                                     │   │
│  │ Antenas direccionales                              │   │
│  │ • Enfoca señal en dirección específica             │   │
│  │ • Reduce exposición                                │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**¿Qué es un AP (Access Point)?**

```
┌─────────────────────────────────────────────────────────────┐
│                ACCESS POINT (AP) - EXPLICACIÓN              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  DEFINICIÓN:                                                │
│  • AP = Access Point (Punto de Acceso)                     │
│  • Dispositivo que permite conexiones WiFi                 │
│  • Conecta dispositivos inalámbricos a la red cableada     │
│  • Actúa como "puente" entre WiFi y Ethernet               │
│                                                             │
│  FUNCIONES PRINCIPALES:                                     │
│  • Transmite señal WiFi en un área específica             │
│  • Autentica dispositivos que se conectan                  │
│  • Encripta el tráfico de datos                            │
│  • Gestiona la distribución de direcciones IP              │
│  • Controla el acceso a la red                             │
│                                                             │
│  TIPOS DE AP:                                               │
│  • AP Independiente: Un solo dispositivo                   │
│  • AP Controller: Múltiples APs gestionados centralmente    │
│  • AP Mesh: Red de APs interconectados                     │
│  • AP Empresarial: Con funciones avanzadas de seguridad    │
│                                                             │
│  COMPONENTES TÍPICOS:                                       │
│  • Antenas WiFi (2.4GHz y/o 5GHz)                          │
│  • Puerto Ethernet para conexión a red                     │
│  • Procesador para gestión de conexiones                   │
│  • Memoria para configuración y logs                        │
│  • Firmware con protocolos de seguridad                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Analogía del AP:**

```
┌─────────────────────────────────────────────────────────────┐
│                    ANALOGÍA DEL AP                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  IMAGINA QUE EL AP ES COMO UN "PORTERO INTELIGENTE":       │
│                                                             │
│  • RECIBE VISITANTES: Dispositivos que quieren conectarse   │
│  • VERIFICA IDENTIDAD: Autentica credenciales WiFi         │
│  • ASIGNA HABITACIÓN: Da dirección IP al dispositivo       │
│  • CONTROLA ACCESO: Permite/deniega acceso a la red        │
│  • MONITOREA ACTIVIDAD: Registra quién entra y sale         │
│  • PROPORCIONA SERVICIOS: Conecta a Internet y recursos    │
│                                                             │
│  SIN AP: Como una casa sin portero - cualquiera puede      │
│          entrar y salir sin control                        │
│                                                             │
│  CON AP: Como un edificio con portero - control de        │
│          acceso, registro de visitantes, seguridad         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 2. Segmentación de Red

```
┌─────────────────────────────────────────────────────────────┐
│                    SEGMENTACIÓN DE RED                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  RED CORPORATIVA                                           │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │  VLAN EMPLEADOS     VLAN INVITADOS    VLAN IoT      │   │
│  │  ┌─────────────┐    ┌─────────────┐   ┌─────────┐   │   │
│  │  │             │    │             │   │         │   │   │
│  │  │ Acceso       │    │ Internet    │   │         │   │   │
│  │  │ completo     │    │ limitado    │   │ Aislado │   │   │
│  │  │             │    │             │   │         │   │   │
│  │  │ WPA3 +       │    │ Portal      │   │         │   │   │
│  │  │ 802.1X       │    │ cautivo     │   │         │   │   │
│  │  │             │    │             │   │         │   │   │
│  │  │ Monitoreo    │    │ Sin acceso  │   │         │   │   │
│  │  │ completo     │    │ interno     │   │         │   │   │
│  │  └─────────────┘    └─────────────┘   └─────────┘   │   │
│  │                                                     │   │
│  │  FIREWALLS INTERNOS                                 │   │
│  │  ┌─────────────────────────────────────────────┐   │   │
│  │  │ Control de tráfico entre segmentos          │   │   │
│  │  │ Políticas específicas por VLAN               │   │   │
│  │  │ Monitoreo de comunicaciones                  │   │   │
│  │  └─────────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Monitoreo y Detección

### Sistema WIDS/WIPS

**¿Qué son WIDS/WIPS?**

```
┌─────────────────────────────────────────────────────────────┐
│                WIDS/WIPS - EXPLICACIÓN                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  WIDS = Wireless Intrusion Detection System                 │
│  (Sistema de Detección de Intrusión Inalámbrica)           │
│                                                             │
│  WIPS = Wireless Intrusion Prevention System                │
│  (Sistema de Prevención de Intrusión Inalámbrica)           │
│                                                             │
│  DIFERENCIA CLAVE:                                          │
│  • WIDS: SOLO DETECTA amenazas (como un sistema de alarmas) │
│  • WIPS: DETECTA Y BLOQUEA amenazas (como un guardia activo) │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**¿Cómo Funciona WIDS/WIPS?**

```
┌─────────────────────────────────────────────────────────────┐
│                FUNCIONAMIENTO WIDS/WIPS                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PASO 1: MONITOREO CONTINUO                                │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Los sensores WiFi escanean constantemente:        │   │
│  │ • Nuevos dispositivos que aparecen                 │   │
│  │ • APs no autorizados (Rogue APs)                   │   │
│  │ • Intentos de conexión sospechosos                 │   │
│  │ • Ataques conocidos (KRACK, Evil Twin, etc.)       │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  PASO 2: ANÁLISIS DE AMENAZAS                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ El servidor central analiza:                        │   │
│  │ • Patrones de tráfico anómalos                      │   │
│  │ • Dispositivos no reconocidos                       │   │
│  │ • Intentos de ataques conocidos                     │   │
│  │ • Comportamiento sospechoso                          │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  PASO 3: RESPUESTA AUTOMÁTICA                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ WIDS: Envía alertas al administrador               │   │
│  │ WIPS: Bloquea automáticamente la amenaza           │   │
│  │ • Desconecta dispositivos maliciosos                │   │
│  │ • Bloquea APs no autorizados                        │   │
│  │ • Aísla tráfico sospechoso                          │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Tipos de Amenazas que Detecta:**

```
┌─────────────────────────────────────────────────────────────┐
│                AMENAZAS DETECTADAS POR WIDS/WIPS            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ROGUE APs (Puntos de Acceso Maliciosos):                  │
│  • APs instalados por atacantes                           │
│  • APs configurados incorrectamente                       │
│  • APs con configuraciones débiles                         │
│  • APs que imitan redes legítimas                          │
│                                                             │
│  CLIENTES MALICIOSOS:                                      │
│  • Dispositivos no autorizados                             │
│  • Dispositivos con malware                                │
│  • Dispositivos realizando ataques                         │
│  • Dispositivos con configuraciones débiles                │
│                                                             │
│  ATAQUES CONOCIDOS:                                        │
│  • KRACK (Key Reinstallation Attack)                       │
│  • Evil Twin (Punto de acceso falso)                      │
│  • Deauthentication attacks                                │
│  • Jamming (Interferencia de señal)                        │
│  • Man-in-the-Middle attacks                               │
│                                                             │
│  COMPORTAMIENTO ANÓMALO:                                   │
│  • Múltiples intentos de conexión fallidos                 │
│  • Tráfico inusual o excesivo                              │
│  • Conexiones desde ubicaciones no esperadas               │
│  • Patrones de tráfico sospechosos                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Ejemplo Práctico de WIDS/WIPS:**

```
┌─────────────────────────────────────────────────────────────┐
│                EJEMPLO: DETECCIÓN DE ROGUE AP               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ESCENARIO: Atacante instala AP malicioso en la oficina     │
│                                                             │
│  1. SENSOR WIDS DETECTA:                                   │
│     • Nuevo AP con SSID "Oficina_Libre"                    │
│     • No está en la lista de APs autorizados               │
│     • Señal fuerte en área de trabajo                      │
│                                                             │
│  2. SERVIDOR ANALIZA:                                      │
│     • Compara con base de datos de APs legítimos          │   │
│     • Verifica políticas de red                           │
│     • Determina que es una amenaza                         │
│                                                             │
│  3. RESPUESTA AUTOMÁTICA:                                  │
│     • WIDS: Envía alerta al administrador                 │
│     • WIPS: Bloquea automáticamente el AP malicioso       │
│     • Desconecta dispositivos que se conectaron           │
│     • Registra el incidente para análisis                 │
│                                                             │
│  4. ADMINISTRADOR RECIBE:                                  │
│     • Notificación en tiempo real                          │
│     • Ubicación del AP malicioso                           │
│     • Dispositivos afectados                               │
│     • Acciones recomendadas                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Mejores Prácticas de Seguridad WiFi

### Checklist de Configuración

```
┌─────────────────────────────────────────────────────────────┐
│                CHECKLIST DE SEGURIDAD WIFI                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CONFIGURACIÓN BÁSICA:                                     │
│  ☐ Cambiar credenciales por defecto                       │
│  ☐ Desactivar administración remota                       │
│  ☐ Mantener firmware actualizado                          │
│  ☐ Configurar filtrado MAC                                │
│  ☐ Reducir potencia de transmisión                         │
│                                                             │
│  ENCRIPTACIÓN:                                             │
│  ☐ Usar WPA3 cuando sea posible                           │
│  ☐ Implementar 802.1X para autenticación                  │
│  ☐ Configurar certificados digitales                      │
│  ☐ Rotar claves regularmente                              │
│                                                             │
│  SEGMENTACIÓN:                                             │
│  ☐ Crear VLANs separadas                                   │
│  ☐ Implementar firewalls internos                         │
│  ☐ Aislar redes críticas                                   │
│  ☐ Configurar políticas de acceso                          │
│                                                             │
│  MONITOREO:                                                │
│  ☐ Implementar WIDS/WIPS                                   │
│  ☐ Configurar alertas de seguridad                        │
│  ☐ Mantener logs de auditoría                             │
│  ☐ Análisis de tráfico regular                            │
│                                                             │
│  EDUCACIÓN:                                                │
│  ☐ Capacitar usuarios sobre riesgos                       │
│  ☐ Establecer políticas de uso                            │
│  ☐ Realizar pruebas de penetración                        │
│  ☐ Actualizar procedimientos regularmente                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Vulnerabilidades Emergentes

### Ataques Avanzados

```
┌─────────────────────────────────────────────────────────────┐
│                AMENAZAS EMERGENTES WIFI                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ATAQUE                    DESCRIPCIÓN                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ Dragonblood         • Vulnerabilidad en WPA3      │   │
│  │                     • Ataque de diccionario        │   │
│  │                     • Compromete autenticación     │   │
│  │                                                     │   │
│  │ FragAttacks         • Fragmentación de frames      │   │
│  │                     • Inyección de tráfico         │   │
│  │                     • Afecta múltiples protocolos  │   │
│  │                                                     │   │
│  │ PMKID Attack        • Captura de PMKID              │   │
│  │                     • Ataque offline               │   │
│  │                     • Vulnerable WPA/WPA2         │   │
│  │                                                     │   │
│  │ Beacon Flooding      • Sobreflujo de beacons        │   │
│  │                     • Interferencia de red          │   │
│  │                     • Denegación de servicio       │   │
│  │                                                     │   │
│  │ Rogue AP Detection  • Puntos de acceso falsos      │   │
│  │                     • Interceptación de tráfico    │   │
│  │                     • Robo de credenciales        │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Conclusiones

La seguridad en redes inalámbricas requiere un enfoque holístico que combine:

1. **Configuración robusta** de puntos de acceso
2. **Encriptación fuerte** con protocolos actualizados
3. **Autenticación multifactor** con 802.1X
4. **Segmentación de red** con VLANs
5. **Monitoreo continuo** con WIDS/WIPS
6. **Educación de usuarios** sobre riesgos
7. **Actualización regular** de firmware y políticas

La evolución constante de las amenazas requiere que los profesionales de seguridad mantengan un conocimiento actualizado y implementen defensas en múltiples capas para proteger efectivamente las redes inalámbricas.

