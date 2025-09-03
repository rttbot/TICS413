
# **Respuestas de Alumnos - Actividad "Seguridad por Capas - Modelo OSI"**

---

## **Grupo 1: Capa 6 - Presentación**
**Integrantes:** Jose Fritz Martinez, Jose Miguel Puiggros, María Trinidad Wilson  
**Fecha:** 27 de agosto de 2025, 17:16

### **1. FUNCIÓN DE LA CAPA**

La función principal de la capa 6 del modelo OSI, llamada capa de presentación es traducir, transformar y preparar los datos para que puedan ser correctamente interpretados por el receptor. Esto incluye tareas como codificación, compresión y cifrado, asegurando que la información enviada por el emisor llegue en un formato comprensible, seguro y eficiente para el destinatario.

**Analogía:** Un ejemplo de la vida real sería una combinación entre un traductor y un repartidor de cartas, ya que la capa se encarga que el mensaje o el paquete llegue de forma entendible al destinatario (traductor) y lo encripta, para que durante el viaje no pueda ser interpretado y leído por 3ras partes.

2. SERVICIOS Y PROTOCOLOS

SSL/TLS (Secure Sockets Layer / Transport Layer Security)

Explicación Este sirve para proporcionar cifrados y seguridad en la comunicación entre dos dispositivos. Se usa comúnmente en páginas web seguras (HTTPS).

Ejemplo práctico: Cuando entras a tu banco en línea, TLS cifra tus datos para que nadie pueda leerlos mientras viajan por la red.

MIME (Multipurpose Internet Mail Extensions)

Explicación: Permite que los correos electrónicos incluyan archivos adjuntos, imágenes, audio, y otros tipos de contenido, no solo texto plano.

Ejemplo práctico: Cuando recibes un correo con una foto o un PDF adjunto, MIME se encarga de que ese archivo se pueda enviar y recibir correctamente.

ASCII / UTF-8 (Formatos de codificación de caracteres)

Explicación: Traducen los datos a un formato que las aplicaciones puedan entender, especialmente texto. UTF-8 es más moderno y soporta muchos idiomas.

Ejemplo práctico: Cuando escribes un mensaje en español con tildes o la letra "ñ", UTF-8 asegura que se vea correctamente en cualquier dispositivo.









### **3. VULNERABILIDADES Y ATAQUES TÍPICOS**

#### **3.1. Man in the Middle**
En este tipo de ataque, el atacante se encuentra entre el usuario y el servidor, haciéndose pasar por el servidor legítimo. Si logra engañar al sistema de certificados, puede establecer una conexión cifrada falsa y leer o modificar los datos sin que el usuario lo note.

#### **3.2. Explotación de Formatos de Archivo**
La capa de presentación al gestiona formatos de archivo como imágenes, audio, video o documentos. Algunos atacantes incrustan código malicioso dentro de estos archivos, que se ejecuta cuando el archivo se abre, siendo como un caballo de troya.

#### **3.3. Ataques por Cifrado Débil o Desactualizado**
También es importante utilizar cifrados buenos y actualizados ya que, cuando se usan algoritmos de cifrado antiguos como SSL 2.0 o 3.0, o incluso versiones tempranas de TLS, los atacantes pueden aprovechar vulnerabilidades conocidas para descifrar la información que debería estar protegida.



### **4. MEDIDAS DE MITIGACIÓN**

#### **4.1. Implementar Cifrado Fuerte y Actualizado**
Utilizar protocolos modernos como TLS 1.3 garantiza que los datos estén protegidos con algoritmos seguros y eficientes. Esto reduce el riesgo de que los atacantes puedan descifrar la información mediante técnicas como fuerza bruta o explotación de vulnerabilidades en versiones antiguas como SSL o TLS 1.0.

#### **4.2. Validar Rigurosamente los Certificados Digitales**
Es fundamental verificar que los certificados utilizados en las conexiones cifradas sean auténticos, vigentes y emitidos por autoridades certificadoras confiables. Esto previene ataques tipo man in the middle, donde un atacante podría interceptar la comunicación usando un certificado falso.

#### **4.3. Analizar y Verificar Archivos Antes de Abrirlos**
Los archivos descargados de internet pueden contener código malicioso oculto. Es recomendable escanearlos con herramientas de seguridad antes de abrirlos, especialmente si provienen de lugares poco confiables.









---

#### **Notas Importantes:**
- **PD1:** El error de la presentación se encuentra al mostrar la inyección de código como vulnerabilidad, siendo que eso corresponde a la capa de aplicación 7
- **PD2:** Nos hacemos responsables de que usamos de manera responsable la Inteligencia Artificial Copilot

---

## **Grupo 2: Capa 7 - Aplicación**
**Integrantes:** Francisco Araya - Bastián de la Fuente  
**Fecha:** 27 de agosto de 2025, 17:18

**Introducción:** El modelo OSI divide la comunicación en redes en siete capas, cada una con funciones específicas. La Capa de Aplicación (Capa 7) es la más cercana al usuario final, ya que permite que programas como navegadores, correos electrónicos o aplicaciones móviles interactúen con la red sin necesidad de comprender los detalles técnicos de las capas inferiores.

### **1. FUNCIÓN DE LA CAPA**

La capa de aplicación proporciona la interfaz entre los usuarios y los servicios de red. Su rol es facilitar la comunicación entre software y red, ofreciendo servicios como navegación web, correo electrónico o transferencia de archivos. Se encarga de hacer la traducción final de los protocolos a algo usable para el usuario.

**Analogía:** Si la red fuera un gran edificio, la capa de aplicación sería la recepción, el lugar donde los visitantes (usuarios) solicitan servicios (correo, web, archivos) sin preocuparse por cómo funcionan los pasillos, ascensores o electricidad del edificio.

### **2. SERVICIOS Y PROTOCOLOS**

Algunos de los principales protocolos de la capa de aplicación son:

- **HTTP/HTTPS:** Protocolos que permiten la navegación web, siendo HTTPS la versión segura mediante cifrado.
- **SMTP, IMAP, POP3:** Protocolos de correo electrónico para enviar, recibir y almacenar mensajes.
- **FTP/SFTP:** Permiten la transferencia de archivos entre computadoras, siendo SFTP la versión segura.


### **3. VULNERABILIDADES Y ATAQUES TÍPICOS**

La capa de aplicación es la más atacada, ya que es la que interactúa directamente con el usuario y maneja datos sensibles. Entre los ataques más comunes están:

- **Phishing:** Suplantación de identidad para engañar al usuario y obtener información confidencial.
- **SQL Injection:** Inserción de código malicioso en formularios web para acceder o manipular bases de datos.
- **Cross-Site Scripting (XSS):** Inyección de scripts en páginas web para robar información de los usuarios.

### **4. MEDIDAS DE MITIGACIÓN**

Para proteger la capa de aplicación se utilizan diversas técnicas y buenas prácticas, como:

- **Certificados digitales y HTTPS:** Cifran la comunicación entre usuarios y servidores.
- **Firewalls de Aplicación Web (WAF):** Detectan y bloquean ataques como SQL Injection o XSS.
- **Buenas prácticas del usuario:** Verificar remitentes de correos, no hacer clic en enlaces sospechosos, y usar contraseñas seguras.
- **Autenticación multifactor (MFA):** Agrega una capa extra de seguridad ante contraseñas comprometidas.


Ejemplos:

- **Google y la mayoría de servicios modernos utilizan HTTPS obligatorio.**
- **Empresas implementan WAFs como Cloudflare para proteger aplicaciones web.**
- **La MFA es usada en bancos y servicios de correo para reducir riesgos de acceso no autorizado.**


#### **Conclusión:**
La capa de aplicación es la puerta de entrada del usuario a la red y, por tanto, el objetivo más frecuente de los atacantes. Entender sus funciones, vulnerabilidades y medidas de mitigación es esencial para proteger la información.

En términos simples: así como en un edificio la recepción debe estar bien controlada para evitar fraudes y accesos indebidos, en la red la capa de aplicación necesita tanto tecnología de protección como usuarios conscientes y preparados.




PD 1: En nuestra capa no encontramos errores en el documento subido. 

PD 2: Se usó copilot para una investigación inicial y saber qué conceptos buscar manualmente. 
  capa “Aplicación”.pdf
Imagen de Simón Alfredo Valenzuela Bassi
En respuesta a Romina Debora Torres Torres
Re: Actividad 27.08
de Simón Alfredo Valenzuela Bassi - miércoles, 27 de agosto de 2025, 17:19
Nombres: Eduardo Rojas, José Llanos, Simón Valenzuela.

### **1. FUNCIÓN DE LA CAPA**
La Capa Física es la base de toda comunicación digital. La función que tiene es mover bits (0 y 1) de un punto A a un punto B usando señales eléctricas, de luz o de radio.
No entiende “mensajes”, “direcciones IP” ni “usuarios”. Solo se preocupa de que los bits lleguen físicamente por el medio (cable de cobre, fibra óptica, aire/ondas).
Analogía:
Podemos suponer que internet es una ciudad y los datos son autos. La Capa Física es la carretera por donde los autos se mueven. No decide a qué barrio van; solo asegura que haya pavimento y que los autos puedan avanzar.
### **2. SERVICIOS Y PROTOCOLOS**

#### **Servicios:**
- Transmisión y recepción de bits.
- Codificación de señales (digital a analógica y viceversa).
- Control de voltaje, frecuencia, modulación.
- Establecimiento y desconexión del enlace físico.

#### **Protocolos:**
- **Ethernet (IEEE 802.3):** Sirve para enviar bits por cable entre equipos de forma confiable
- **Wi‑Fi (IEEE 802.11):** Define cómo viajan los bits de forma inalámbrica
- **RS‑232/RS‑485 (serial):** Comunicaciones punto a punto simples entre equipos (sensores, PLC, consolas)
- **Otros ejemplos válidos:** Fibra óptica, DOCSIS (coaxial), Bluetooth – PHY
### **3. VULNERABILIDADES Y ATAQUES TÍPICOS**
Afectan directamente el medio (cable/aire/infraestructura) y, por lo tanto, pueden tumbar servicios antes de que actúen firewalls o contraseñas.
Jamming (especialmente en Wi‑Fi)
Bloquea las señales inalámbricas, haciendo que los equipos no logren conectarse.
Pinchado de cable (tapping) en cobre o fibra
Colocar un dispositivo que copia la señal del cable (en fibra, a veces con una leve curvatura controlada que “filtra” luz)
Conexión física no autorizada (rogue device)

Que alguien accede físicamente a un rack/oficina y conecta un equipo (mini‑switch, laptop, Raspberry Pi) a un puerto libre.
Sabotaje Físico
Cortar los cables o desconectar equipos.
### **4. MEDIDAS DE MITIGACIÓN**

Para proteger la capa física, se pueden aplicar:

- **Control de acceso físico:** Cerraduras, cámaras, seguridad en salas de servidores.
- **Uso de cableado blindado:** Para evitar interferencias y escuchas.
- **Monitoreo de infraestructura:** Sensores, alarmas, detección de desconexiones.
- **Separación de redes sensibles:** Evitar que redes críticas compartan infraestructura.
- **Protección contra jamming:** Uso de frecuencias seguras, detección de interferencias.

---

#### **Notas Importantes:**
- **PD1:** En el material correspondiente de capa 1 en vulnerabilidad no corresponde el término keylogging.
- **PD2:** Uso de IA Copilot UAI para contrastar la información de las diapositivas.

---

## **Grupo 4: Capa 2 - Enlace de Datos**
**Integrantes:** Javier Anderson y Giovanni Beretta  
**Fecha:** 27 de agosto de 2025, 17:19

1. FUNCIÓN DE LA CAPA
La capa de enlace de datos se encarga de establecer una conexión directa entre dos dispositivos en la misma red. Su función principal es organizar los bits en tramas, detectar y corregir errores de transmisión, y controlar el acceso al medio físico (quién puede hablar y cuándo).

La capa de enlace de datos es como el portero de un edificio.
Imagina que los datos son personas que quieren entrar al edificio (la red). El portero verifica quién entra, si tienen permiso, y se asegura de que no haya conflictos entre quienes entran al mismo tiempo. También revisa que nadie entre con errores (como una tarjeta mal escaneada) y que todo esté en orden.

Relación con las capas adyacentes:
La capa física (1) sería como el cableado del timbre y la puerta - La capa física le da al portero la capacidad de "escuchar" y "hablar". Sin ella, no hay comunicación.

La capa (3) de red sería como el GPS del visitante que quiere llegar al edificio - La capa de red guía los datos hasta el portero. Sin ella, los datos no sabrían a qué edificio ir.


2. SERVICIOS Y PROTOCOLOS

Ethernet
¿Qué es?
Idioma utilizado para que los dispositivos conectados por cable a una red local (LAN) puedan hablar entre ellos. Les dice cómo enviar y recibir datos de forma ordenada.
¿Para qué sirve?
Ethernet establece un marco confiable y eficiente para el intercambio de tramas de datos entre dispositivos dentro de una misma red física.

MAC (Media Access Control)
¿Qué es?
Es una parte del protocolo de Ethernet. Cada dispositivo posee una dirección MAC única que los distingue entre cada uno de ellos.
¿Para qué sirve?
Permite identificar quién envía y quién recibe los datos dentro de la red local.


LLC (Logical Link Control)
¿Qué es?
Subcapa que gestiona los errores y el control de flujo de los datos.
¿Para qué sirve?
Asegura que los datos lleguen en orden y sin errores.

3. VULNERABILIDADES Y ATAQUES TÍPICOS

Desconexión física / Corte de cable:
Un ataque muy simple: desconectar o cortar el cable de red para interrumpir la comunicación.
¿Cómo funciona?
Literalmente, alguien puede desenchufar un cable Ethernet o cortar una fibra óptica. Esto detiene completamente la transmisión de datos, afectando la disponibilidad del servicio.

b) Intercepción de cables (Wiretapping):
Es cuando alguien conecta un dispositivo físico (como un sniffer o analizador de red) a un cable de red para escuchar o capturar datos.

¿Cómo funciona?
Es como poner un micrófono oculto en una conversación telefónica. El atacante no interfiere, solo escucha. En redes, puede capturar contraseñas, correos, o cualquier dato que pase por ese cable.

c) Interferencia electromagnética (EMI) / Jamming

Es cuando una señal externa (como la de un motor, microondas o incluso otro transmisor) interfiere con la señal de red, causando pérdida de datos o desconexiones.

¿Cómo funciona?
Imagina que estás hablando por walkie-talkie y alguien enciende una radio muy fuerte cerca. Tu señal se mezcla con ruido, y ya no puedes entender lo que te dicen. En redes, esto puede hacer que los bits lleguen corruptos o no lleguen.



4. MEDIDAS DE MITIGACIÓN

1. Control de acceso a la red
Permite decidir qué dispositivos pueden conectarse a una red local, y bajo qué condiciones.

Herramientas que lo implementan:
Microsoft NPS (Network Policy Server)
FreeRADIUS (en entornos Linux)
Switches gestionables de fabricantes (ej: Cisco, HP y Aruba)

Buenas prácticas:
Validar a los usuarios con Active Directory.
Usar certificados digitales o credenciales seguras.
Desactivar puertos no utilizados en switches.






2. Segmentación de red con VLANs
Divide la red física en subredes, para limitar el alcance del tráfico, reduciendo probabilidad de ataques internos

Herramientas que lo implementan:
Switches gestionables (Cisco, MikroTik, Ubiquiti)
Firewalls con soporte de VLAN (pfSense, Fortinet, SonicWall)

Buenas prácticas:
Separar usuarios, servidores y dispositivos IoT en VLANs distintas.
Configurar reglas estrictas de comunicación entre VLANs.
Usar VLANs de gestión para administración de red.

3. Protección contra ARP Spoofing
Evita la suplantación de direcciones MAC/IP, reduciendo el riesgo de interceptación de tráfico en la red local.

Herramientas que lo implementan:
Dynamic ARP Inspection (DAI) en switches Cisco
ARPwatch para monitorear cambios sospechosos en la red
Ettercap (se usa en pruebas de seguridad)

Buenas prácticas:
Activar DAI y configurar listas de direcciones MAC/IP válidas.
Monitorear constantemente la tabla ARP.
Usar IP estáticas en dispositivos críticos.






















Bibliografía
Microsoft Copilot. (2025). Asistencia técnica sobre seguridad en la Capa 2 del modelo OSI. https://copilot.microsoft.com
PD.1: “Finaliza la comunicación entre los nodos de red” (ppt profesora)
En el modelo OSI, la capa 2 no finaliza la comunicación, sino que se garantiza el enlace confiable entre nodos vecinos. El que finaliza la comunicación se asocia más bien a capas superiores.


PD.2: Durante nuestra investigación sobre redes y el modelo OSI, utilizamos IA generativa para obtener explicaciones claras y rápidas sobre conceptos técnicos como la capa física, la capa de red, y los ataques comunes en estas capas. En particular, usamos Copilot de Microsoft, una IA basada en el modelo GPT-4, que nos ayudó a:

Comprender cómo se relacionan las capas del modelo OSI.
Identificar vulnerabilidades y ataques típicos en la capa física.
Redactar textos explicativos de forma clara y en lenguaje sencillo.
Gracias a esta herramienta, podemos mejorar la calidad de nuestras respuestas y presentaciones, optimizando el tiempo de investigación y redacción.
Imagen de Benjamín Heraldo López Pachel
En respuesta a Romina Debora Torres Torres
Re: Actividad 27.08
de Benjamín Heraldo López Pachel - miércoles, 27 de agosto de 2025, 17:20
CAPA 4
Integrantes: Eduardo Diaz y benjamín Lopez

Capa 4: Capa de transporte

1. FUNCIÓN DE LA CAPA (2 minutos)

Permite la comunicación fiable y organizada entre aplicaciones en diferentes sistemas gestionando la segmentación de datos, el cual es proceso de dividir grandes flujos de datos de la capa de aplicación en unidades más pequeñas llamadas segmentos para su transmisión eficiente a través de la red, el reensamblaje de los mismos y el control errores y flujo de la red.

Pedí por temu una mesa y en vez de llegar armada en una caja grande que es muy difícil de transportar las diferentes partes de la mesa llegan en cajas más pequeñas, para luego que yo las arme en mi casa

2. SERVICIOS Y PROTOCOLOS (1 minuto)
Mencionar 2-3 servicios/protocolos principales de la capa
Explicar para qué sirve cada uno
Protocolos principales
TCP (Transmission Control Protocol):
El protocolo TCP está orientado a la conexión y garantiza que la información enviada llegue de manera completa, en el mismo orden en que fue transmitida y sin errores. Esto lo hace muy confiable para aplicaciones donde no se puede perder ningún dato, como la navegación web, el correo electrónico o la transferencia de archivos.


UDP (User Datagram Protocol):
UDP es un protocolo sin conexión que no asegura la entrega ni el orden de los datos, pero ofrece mucha mayor velocidad y menor consumo de recursos. Por eso, se utiliza en aplicaciones en tiempo real donde la rapidez es más importante que la confiabilidad, como en transmisiones de video en streaming, videojuegos en línea o llamadas por voz sobre internet (VoIP).
TLS/SSL (Transport Layer Security / Secure Sockets Layer):
TLS y su predecesor SSL son protocolos que añaden seguridad al transporte de datos, usando cifrado y autenticación. Aunque funciona sobre TCP, se encargan de que la información viaje de forma privada y protegida contra ataques. Son la base de la seguridad en servicios como HTTPS, que protege la comunicación en la web.




3. VULNERABILIDADES Y ATAQUES TÍPICOS (1 minuto)

SYN Flood (TCP): Este ataque consiste en enviar muchas solicitudes de conexión TCP con paquetes SYN, El servidor queda esperando respuestas que nunca llegan, lo que consume memoria y recursos hasta saturar, impidiendo que atienda a usuarios legítimos.

UDP Flood: En este caso, el atacante envía una gran cantidad de paquetes UDP a distintos puertos de la víctima. Como respuesta, la máquina debe contestar con mensajes de error indicando que esos puertos están cerrados, lo que genera sobrecarga en la red y termina produciendo una denegación de servicio.

TCP Reset Attack: el atacante falsifica un paquete RST haciéndose pasar por una de las partes de la conexión. Al recibirlo, el otro computador cree que su compañero quiere cortar la comunicación y cierra la sesión aunque en realidad nadie lo pidió.


4. MEDIDAS DE MITIGACIÓN (1 minuto)

Para proteger esta capa se pueden aplicar varios controles. Uno muy común es el uso de firewalls de capa 4, que permiten filtrar tráfico según puertos y protocolos (por ejemplo, bloquear puertos innecesarios o limitar conexiones). Herramientas como iptables en Linux o firewalld son ejemplos de software que permiten implementar estas reglas.

Otra medida es el uso de sistemas de detección y prevención de intrusos (IDS/IPS), como Snort o Suricata, que ayudan a identificar patrones de ataques como SYN Flood o escaneos de puertos y detenerlos en tiempo real.

Finalmente, una buena práctica es configurar limitación de conexiones y rate limiting en servidores, de manera que un atacante no pueda abrir miles de sesiones simultáneamente. Por ejemplo, en servidores web se usa Fail2ban o mod_evasive para bloquear automáticamente IPs que abusan de las conexiones.


PD1: No encontramos errores significativos si no en algunas partes falta de tecnicismo e información
PD2 utilizamos copilot para un análisis exploratorio inicial
Imagen de Ignacio Javier Soto Saniter
En respuesta a Romina Debora Torres Torres
Re: Actividad 27.08
de Ignacio Javier Soto Saniter - miércoles, 27 de agosto de 2025, 17:22
-- Capa 5 - Ignacio Soto y Pablo Cabezas  --


Funciones


La capa de sesión permite a los usuarios en distintas máquinas establecer sesiones entre ellos. 


Las sesiones ofrecen varios servicios: 

control del diálogo (llevar el control de quién va a transmitir)

manejo de tokens (evitar que dos partes intenten la misma operación crítica al mismo tiempo)

sincronización (usar puntos de referencia en las transmisiones extensas para reanudar desde el último punto de referencia en caso de una interrupción).


Ej análogo: En una partida de ajedrez entre dos personas:


Control del diálogo: juegan por turnos, uno mueve y el otro espera.

Manejo de tokens: solo una persona puede tener la pieza en la mano a la vez

Sincronización: si se corta la luz, al volver continúan desde la última jugada, no desde el inicio.


Servicios y protocolos


RPC (Remote Procedure Call): permite que un programa ejecute funciones en otro equipo de forma remota.


NetBIOS: Protocolo usado en redes Windows para establecer sesiones entre dispositivos. Aunque hoy se usa sobre TCP/IP, originalmente operaba en la capa de sesión.


– Se uso Copilot para este ítem –


Vulnerabilidades


Secuestro de sesión (Session Hijacking): un atacante roba la sesión activa de un usuario (ej: tu cuenta en un banco o en Facebook) y actúa como si fueras tú.


Fugas de información: la información sensible almacenada en variables de sesion puede ser expuesta a través de errores de programación o ataques dirigido


– Se uso Copilot para este ítem –

Medidas de mitigación


Controles de seguridad específicos:

Autenticación mutua de sesión

Verifica la identidad de ambos extremos antes de establecer la sesión.

Previene ataques de suplantación (spoofing) y accesos no autorizados.

Gestión segura de tokens y credenciales

Protege los identificadores de sesión (como cookies o tokens JWT) contra robo o manipulación.

Evita secuestro de sesión (session hijacking).

Control de tiempo de sesión y cierre automático

Limita la duración de sesiones inactivas para reducir la superficie de ataque.

Previene accesos persistentes no deseados.

– Se uso Copilot para este ítem –

Herramientas que ayudan a implementarlos:

Kerberos: Protocolo de autenticación que opera en la capa de sesión, ideal para entornos corporativos. Usa tickets temporales para validar identidades.

OAuth 2.0 / OpenID Connect: Aunque se implementan en capas superiores, gestionan tokens de sesión de forma segura.

Firewalls de aplicación (WAF): Pueden detectar y bloquear intentos de secuestro de sesión o manipulación de tokens

– Se uso Copilot para este ítem –

Ejemplos de buenas prácticas:

Usar TLS para cifrar toda la comunicación de sesión.

Implementar expiración de tokens y rotación periódica.

doble autenticador de sesión

– Se uso Copilot para este ítem –









PD1: En la capa 5, se menciona que SSL/TLS es parte de la capa 5, sin embargo esto es inexacto, en realidad es de capa 6.

PD2: Se utilizó copilot en ciertas partes 



  Capa 5 contenido con formato.pdf
Imagen de Nathan Denuit
En respuesta a Romina Debora Torres Torres
Re: Actividad 27.08
de Nathan Denuit - miércoles, 27 de agosto de 2025, 17:26
hecho por Nathan Denuit and Lara Heuberger

Capa 3 - Red

1. FUNCIÓN DE LA CAPA
La capa 3 del modelo OSI, conocida como capa de red, tiene como función principal permitir que los datos viajen desde un dispositivo de origen hasta uno de destino, incluso si están en redes distintas o ubicaciones geográficas lejanas. Esta capa hace posible la comunicación entre dispositivos conectados a diferentes redes, como si enviáramos una carta que debe atravesar múltiples oficinas postales antes de llegar a su destino.

Para lograr esto, la capa 3 utiliza direcciones IP (IPv4 e IPv6) que identifican de forma única cada dispositivo en la red. Estas direcciones permiten que los paquetes tengan un origen y un destino claramente definidos. Además, se encarga del encaminamiento, es decir, de determinar la mejor ruta disponible para que los paquetes lleguen a su destino. Los routers evalúan tablas de enrutamiento y métricas como distancia, costo o latencia para seleccionar el camino más eficiente.

Otras funciones importantes incluyen la fragmentación y reensamblaje de paquetes grandes, el control de tráfico y la priorización de ciertos paquetes mediante mecanismos como QoS, la gestión de errores con protocolos como ICMP que informan sobre problemas de conectividad, y la interconexión de redes LAN, WAN o WiFi mediante un direccionamiento común basado en IP.

2. SERVICIOS Y PROTOCOLOS
Entre los protocolos más relevantes de esta capa se encuentra IP, que asigna direcciones lógicas y transporta los paquetes. ICMP también es esencial, ya que gestiona mensajes de control y error, como los que se usan en herramientas como ping o traceroute. IGMP permite la gestión de grupos multicast, facilitando la transmisión eficiente de datos a múltiples destinatarios. Los protocolos de enrutamiento como OSPF y BGP permiten que los routers compartan información para calcular rutas óptimas, y IPsec protege la integridad y confidencialidad de los datos mediante cifrado y autenticación.

3. VULNERABILIDADES Y ATAQUES TÍPICOS
Sin embargo, esta capa también presenta vulnerabilidades. Una de ellas es la suplantación de IP (IP Spoofing), donde un atacante falsifica una dirección IP para hacerse pasar por otro dispositivo. También existe la manipulación de rutas (Route Hijacking), que redirige el tráfico hacia destinos maliciosos, y la falta de filtrado, que permite el paso de tráfico no deseado por firewalls mal configurados. Los ataques de intermediario (Man-in-the-Middle) interceptan la comunicación entre dos dispositivos sin ser detectados, y los ataques DDoS saturan la red con tráfico excesivo. Además, el flooding de paquetes ICMP o IGMP puede sobrecargar los recursos de red.

4. MEDIDAS DE MITIGACIÓN
Para mitigar estos riesgos, se aplican varias medidas. Contra la suplantación de IP, se recomienda el filtrado de paquetes, la autenticación fuerte con IPsec y el monitoreo de tráfico. Para evitar el secuestro de rutas, se deben usar protocolos seguros como BGP con validación RPKI, segmentar la red y realizar auditorías periódicas. Los ataques DDoS pueden enfrentarse con servicios especializados de mitigación, balanceo de carga y limitación de tasa. Para protegerse de ataques de intermediario, se recomienda cifrado de extremo a extremo, autenticación mutua y supervisión de red. Contra la falta de filtrado, es clave configurar adecuadamente los firewalls, usar listas de control de acceso (ACLs) y mantener los dispositivos actualizados. Finalmente, para prevenir el flooding ICMP/IGMP, se debe minimizar su uso y aplicar sistemas IDS/IPS que detecten y bloqueen tráfico anómalo.
