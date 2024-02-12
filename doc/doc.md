# Nombre del Proyecto|

## Índice

- [Introducción](#introducción)
- [Visión General del Proyecto](#visión-general-del-proyecto)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Flujo de Información](#flujo-de-información)
- [Actores y Casos de Uso](#actores-y-casos-de-uso)
- [Arquitectura del Sistema](#arquitectura-del-sistema)
- [Modelado de la Base de Datos](#modelado-de-la-base-de-datos)
- [Planificación del Proyecto](#planificación-del-proyecto)
  - [Metodología Ágil](#metodología-ágil)
  - [Sprints y Tareas](#sprints-y-tareas)
- [Gestión de Repositorios](#gestión-de-repositorios)
- [Pruebas y Calidad del Código](#pruebas-y-calidad-del-código)
- [Despliegue y Mantenimiento](#despliegue-y-mantenimiento)
- [Conclusiones y Próximos Pasos](#conclusiones-y-próximos-pasos)

## Introducción

Bienvenidos al proyecto CSC Discord Bot, una iniciativa enfocada en desarrollar un bot de Discord altamente interactivo y funcional que servirá como la piedra angular para una aplicación más amplia en el futuro. En un mundo donde la comunicación digital y las comunidades en línea juegan un papel crucial, nuestro proyecto busca utilizar esta herramienta para integrar la comunicación y la gestión de nuestra empresa utilizando las herramientas opensource que nos otorga discord para el desarrollo de nuestras aplicaciones

Este proyecto surge de la necesidad de resolver problemas tales como, la gestión de las transferencias, mejorar la velocidad ya que se busca crear una comunicación efectiva e inmediata de las transacciones, el manejo y las consultas a la base de datos integrando desde discord, y tiene como objetivo principal unificar todas las operaciones de la empresa a través de discord. Con el uso de tecnologías punteras como SQLite3 para la gestión de bases de datos, aiosqlite para la programación asíncrona, y Nextcord para la integración con Discord, este proyecto promete ser una solución robusta y escalable.

Adoptaremos un enfoque ágil para el desarrollo, utilizando SCRUM y Kanban para garantizar una entrega eficiente y flexible, permitiendo iteraciones rápidas basadas en el feedback de los usuarios y las necesidades emergentes del proyecto. La documentación detallará cada fase del desarrollo, desde la planificación inicial hasta el despliegue final, asegurando que todas las partes interesadas estén bien informadas y comprometidas a lo largo del proceso.

Con un enfoque claro en la calidad, la usabilidad y la innovación, este proyecto no solo busca satisfacer las necesidades actuales sino también anticiparse a las futuras demandas de la comunidad de Discord y del ámbito digital en general.

### Visión a Largo Plazo

El proyecto CSC Discord Bot es solo el comienzo de una ambiciosa visión a largo plazo para revolucionar la gestión empresarial y el manejo de relaciones con los clientes dentro de nuestra organización. Nuestro objetivo es no solo simplificar y mejorar la comunicación interna y la gestión de tareas a través de Discord, sino también sentar las bases para un sistema integral que abarque todas las facetas de la gestión empresarial, desde las operaciones diarias hasta las interacciones con los clientes y el análisis de métricas clave del negocio.

### Integración y Escalabilidad

A medida que el CSC Discord Bot madure y se estabilice, planeamos expandir su funcionalidad para integrarse con un ecosistema más amplio de aplicaciones empresariales. Esta expansión contempla el desarrollo de una aplicación con un frontend robusto construido en React, permitiendo una experiencia de usuario rica e interactiva, y un backend potente en NodeJS, garantizando escalabilidad, rendimiento y la capacidad de manejar un volumen creciente de transacciones y datos de manera eficiente.

### Enfoque en Métricas y Relaciones con los Clientes

Un componente clave de nuestra visión a largo plazo es la implementación de herramientas avanzadas para el análisis de métricas del negocio y la gestión de relaciones con los clientes (CRM). Esto nos permitirá no solo monitorear el rendimiento del negocio en tiempo real, sino también entender mejor las necesidades y preferencias de nuestros clientes, personalizando nuestras interacciones y servicios para mejorar la satisfacción y la lealtad del cliente.

### Plan de Desarrollo Futuro

Reconocemos que este es un proyecto ambicioso que requerirá una planificación cuidadosa, recursos dedicados y una ejecución meticulosa. Nuestro plan incluye:

- **Fase de Investigación y Desarrollo:** Continuar explorando las últimas tecnologías y mejores prácticas en desarrollo de software para asegurar que nuestra solución sea a la vez innovadora y sostenible.
- **Iteraciones Incrementales:** Adoptar un enfoque iterativo para el desarrollo, permitiéndonos lanzar funcionalidades de manera gradual y ajustar nuestros planes basados en el feedback de los usuarios y las tendencias del mercado.
- **Enfoque en la Experiencia del Usuario:** Asegurar que todas las interfaces y puntos de interacción sean intuitivos, eficientes y satisfactorios para los usuarios, tanto internos como externos.

Con esta visión, estamos comprometidos no solo con el éxito a corto plazo del CSC Discord Bot, sino con el establecimiento de una plataforma que pueda crecer y evolucionar para satisfacer las necesidades cambiantes de nuestra empresa y nuestros clientes en los años venideros.

## Visión General del Proyecto

El proyecto CSC Discord Bot se concibe como una solución innovadora diseñada para optimizar la comunicación interna y la gestión de tareas dentro de nuestra empresa, utilizando la plataforma Discord. Al integrar funcionalidades avanzadas directamente en Discord, buscamos mejorar la eficiencia operativa, facilitar el acceso rápido a la información y centralizar las operaciones empresariales en un único ecosistema digital.

### Objetivos Clave

- **Mejora de la Comunicación Interna:** Facilitar una comunicación fluida y eficaz entre los miembros del equipo, mejorando la colaboración y la rapidez en la toma de decisiones.
- **Automatización de Tareas:** Implementar funciones automatizadas para gestionar tareas rutinarias, reduciendo la carga de trabajo manual y minimizando errores.
- **Acceso a Información en Tiempo Real:** Proporcionar a los empleados una manera rápida y sencilla de consultar y gestionar datos empresariales importantes directamente desde Discord.
- **Integración de Sistemas:** Conectar el bot con otros sistemas y herramientas empresariales para un flujo de trabajo unificado y eficiente.

### Componentes del Proyecto

- **Bot de Discord:** Desarrollo del bot utilizando Nextcord para integrarse perfectamente con Discord, ofreciendo una variedad de comandos y funcionalidades.
- **Base de Datos:** Utilización de SQLite3 y aiosqlite para una gestión de datos eficiente, segura y escalable.
- **Interfaz de Usuario:** (Planificado para fases futuras) Desarrollo de un frontend en React para proporcionar una experiencia de usuario rica y un backend en NodeJS para manejar la lógica empresarial y la gestión de datos.

### Metodología de Desarrollo

Adoptaremos un enfoque ágil para el desarrollo del proyecto, utilizando prácticas de SCRUM y Kanban para permitir una planificación flexible, una entrega iterativa y una adaptación continua a los cambios y nuevos requisitos. Este enfoque nos permitirá lanzar rápidamente las funcionalidades más críticas y recopilar comentarios de los usuarios para iteraciones futuras.

### Alcance y Limitaciones

El proyecto se centrará inicialmente en el desarrollo del bot de Discord, con la intención de expandir y escalar la solución para incluir interfaces de usuario más avanzadas y una integración más profunda con otros sistemas empresariales en fases posteriores. Estamos conscientes de las limitaciones técnicas y de recursos en esta etapa inicial, pero estamos comprometidos a superar estos desafíos mediante una planificación cuidadosa y la adopción de tecnologías escalables.

### Beneficios Esperados

Con el CSC Discord Bot, esperamos lograr una transformación digital interna que no solo mejore la eficiencia operativa sino que también fomente una cultura de innovación y colaboración dentro de la empresa. Este proyecto sienta las bases para una gestión empresarial más integrada y automatizada, preparando el camino para futuras mejoras y expansiones.

Con esta visión general, proporcionamos un marco claro para el proyecto, estableciendo expectativas y delineando el camino hacia el éxito. Estamos emocionados de embarcarnos en este viaje y de ver cómo el CSC Discord Bot contribuirá al crecimiento y la innovación de nuestra empresa.


## Tecnologías Utilizadas
El desarrollo del proyecto CSC Discord Bot involucra una variedad de tecnologías, cada una seleccionada por su eficacia, fiabilidad y compatibilidad con los objetivos del proyecto. Cada vez que implementemos una tecnología nueva debemos implementarla en el área de Tecnologías utilizadas, una breve descripción y cómo nos ayudará esa herramienta para el desarrollo, y especificar la versión donde se añadió esa tecnología inicialmete empezaremos con las siguientes tecnologías_

### Python

Python es el lenguaje de programación principal para el desarrollo del bot de Discord. Fue elegido por su simplicidad, legibilidad y la vasta biblioteca de paquetes disponibles que facilitan el desarrollo rápido y eficiente de aplicaciones complejas.

### SQLite3 y aiSQLite

SQLite3 es el sistema de gestión de bases de datos elegido por su ligereza, independencia y configuración sin servidor, lo que lo hace ideal para proyectos con necesidades moderadas de almacenamiento de datos. aiSQLite, una interfaz asíncrona para SQLite, permite operaciones de base de datos no bloqueantes, lo que es crucial para mantener la eficiencia y la escalabilidad del bot en entornos asíncronos de Python.

### Nextcord

Nextcord es una biblioteca de Python que facilita la interacción con la API de Discord, permitiendo la creación de bots ricos en características. Se seleccionó Nextcord por su amplia documentación, su comunidad activa y su compatibilidad con las últimas funcionalidades de Discord.

### Azure DevOps / GitHub

Para la gestión de versiones y el control de código fuente, estamos considerando Azure DevOps y GitHub. Ambos ofrecen robustas herramientas de CI/CD (Integración Continua/Entrega Continua), gestión de proyectos y colaboración en equipo. La elección final se basará en factores como la integración con el entorno de desarrollo existente, la preferencia del equipo y la experiencia previa.

### Visual Studio Code (VSCode)

VSCode es el editor de código seleccionado para el desarrollo, debido a su amplia gama de extensiones, soporte para múltiples lenguajes de programación y herramientas integradas de depuración y control de versiones. Su personalización y eficiencia lo hacen ideal para el desarrollo ágil de software.

### Notion
Herramienta que utilizarEntendiendo que ya tienes experiencia en desarrollo y que la comunicación entre componentes se manejará a través de los mensajes en Discord, podemos simplificar y reestructurar los microservicios de la siguiente manera, enfocándonos en la funcionalidad central y minimizando la complejidad:

Microservicios Reestructurados
Microservicio de Gestión de Usuarios y Roles

Responsabilidades: Maneja el registro de usuarios, la asignación y gestión de roles dentro de Discord y la base de datos.
Casos de Uso Principales: Registro de usuarios, selección y asignación de roles.
Tecnologías Sugeridas: Python, SQLite3/aiSQLite para la gestión de datos de usuarios y roles.
Microservicio de Gestión de Cuentas y Transacciones

Responsabilidades: Administra las cuentas de los usuarios y procesa las transacciones, incluyendo la creación de cuentas, actualización de saldos, y manejo de transacciones y batches.
Casos de Uso Principales: Creación y actualización de cuentas, manejo de transacciones, inicio y cierre de batches.
Tecnologías Sugeridas: Python, SQLite3/aiSQLite, con lógica para manejar transacciones basadas en los mensajes de Discord.
Microservicio de Bot de Discord

Responsabilidades: Interactúa con los usuarios a través de Discord, manejando comandos y eventos, y sirve como el punto de integración para otros microservicios.
Casos de Uso Principales: Procesamiento de comandos de Discord, interacción directa con los usuarios.
Tecnologías Sugeridas: Python con la biblioteca Nextcord.
Microservicio de Reportes y Monitoreo

Responsabilidades: Genera reportes sobre el estado de cuentas, transacciones y ofrece herramientas de monitoreo para la actividad del sistema.
Casos de Uso Principales: Reportes de estado de cuentas y transacciones, monitoreo del sistema.
Tecnologías Sugeridas: ELK Stack para logging y análisis, Prometheus y Grafana para monitoreo.
Simplificaciones y Consideraciones
Comunicación Interna: Dado que se utilizarán los mensajes de Discord para la comunicación, cada microservicio puede escuchar y responder a comandos específicos directamente a través del bot de Discord, eliminando la necesidad de un sistema de colas de mensajes separado.

Autenticación y Autorización: La autenticación se manejará a través de Discord, y la autorización basada en roles de Discord puede ser suficiente para controlar el acceso a funciones específicas dentro de los microservicios.

Base de Datos Unificada: Considera la posibilidad de mantener una base de datos centralizada si la carga de trabajo y la complejidad de los datos lo permiten, simplificando la gestión de datos y reduciendo la sobrecarga de sincronización entre servicios.

Escalabilidad y Despliegue: Cada microservicio puede ser contenedorizado y desplegado a través de Kubernetes para facilitar la escalabilidad y el manejo de la infraestructura, pero la arquitectura debe diseñarse de tal manera que los componentes puedan escalarse de forma independiente según sea necesario.

Esta estructura simplificada se centra en la funcionalidad esencial y aprovecha las capacidades de comunicación de Discord, lo que puede reducir la complejidad y acelerar el desarrollo. Asegúrate de documentar claramente las interfaces y responsabilidades de cada microservicio y mantener buenas prácticas de desarrollo para garantizar la mantenibilidad y escalabilidad del sistema.emos para realizar la gestión de proyectos y tareas al igual que el manejo de la gestión colaborativa

### Herramientas Adicionales

Además de las tecnologías principales, se utilizarán otras herramientas y bibliotecas auxiliares según sea necesario para pruebas, depuración, documentación y otras tareas de desarrollo. Estas pueden incluir Postman para pruebas de API, PyTest para pruebas unitarias, y Sphinx para generación de documentación.

Confirmar la pila tecnológica, incluyendo Python, SQLite3, aiSQLite, Nextcord, Azure DevOps/GitHub, VSCode, Notion, Kubernetes, RabbitMQ/Kafka, ELK Stack, Prometheus, Grafana, etc.

Con esta pila tecnológica, el proyecto CSC Discord Bot está bien equipado para abordar los desafíos de desarrollo actuales y futuros, garantizando una solución final robusta, escalable y mantenible.



## Flujo de Información
### Registro de usuarios
Actores
Usuario Discord: Persona que interactúa con el bot para registrarse en el sistema.
Superuser: Usuario con permisos para aceptar o rechazar solicitudes de roles.

#### Casos de Uso
- Registro de Usuario:
    - El usuario interactúa con el bot para iniciar el proceso de registro.
    - El bot recopila la información del usuario de Discord (username y UID).
    - El bot registra la información en la base de datos con un timestamp de registro.

- Asignación de Cuenta:
    - Se verifica si el usuario tiene cuentas asociadas.
    - Se actualizan o crean registros de cuentas con el valor insertado valor anterior y valor actual.

- Selección de Rol:
    - El usuario selecciona un rol a través de un embed con botones.
    - El bot registra la solicitud de rol con un timestamp.

- Gestión de Solicitudes:
    - El superuser revisa las solicitudes de rol en un canal específico.
    - El superuser acepta o rechaza la solicitud.
    - La solicitud se guarda en una tabla de backlog con el estado de la solicitud.

- Asignación de Rol:
    - Si la solicitud es aceptada, el bot asigna el rol al usuario en Discord.
    - El bot actualiza la base de datos con el rol asignado al usuario.

- Gestión de Ganancias y Transacciones:
    - Cada usuario tiene un registro de ganancias y transacciones.
    - Se lleva un flujo detallado de las ganancias y transacciones en la base de datos.

#### Registro de Usuario - Diagramas de Flujo
Para el proceso de registro de usuarios y asignación de roles, el diagrama de flujo incluirá los siguientes pasos:

- Usuario inicia el registro.
- Usuario proporciona información a través del bot.
- Bot registra la información en la base de datos.
- Usuario selecciona un rol.
- Bot envía solicitud al superuser.
- Superuser acepta o rechaza la solicitud.
- Bot actualiza el registro del usuario con el rol asignado.

Para la gestión de cuentas y transacciones, el flujo sería:
- Usuario realiza una operación que afecta su cuenta.
- Bot actualiza los valores de la cuenta en la base de datos.
- Se mantiene un registro de todas las transacciones y cambios de valor.

### Transacciones
Actores
- Revendedor (Reseller): Usuario que puede tener clientes asociados y recibir comisiones.
- Cliente Normal: Usuario registrado que acumula puntos por transacciones.
- Super Usuario: Tiene permisos completos para gestionar la aplicación.
- Cajero: Responsable de manejar las transacciones enviadas por los revendedores o clientes y registrarlas como realizadas o canceladas.
- Sistema (Bot de Discord): Ejecuta comandos y automatiza procesos en la aplicación.

Proceso de Transacción y Casos de Uso

Inicio de Batch (Lote):
- Un revendedor o cajero inicia un batch para acumular transacciones.
- Un revendedor inicia un batch para acumular transacciones.
- Se crea una base de datos en memoria o se utiliza una base de datos alterna para manejar el batch.

Registro de Cuentas y Saldos Iniciales:
- Se registra la o las cuentas receptoras y emisoras con los saldos iniciales.

Realización de Transacciones:
- El revendedor realiza una transacción con el comando !t.
- Se calcula el monto en moneda receptora aplicando la tasa de cambio.
- Se añade la comisión si aplica.
- El bot notifica al cajero y registra la transacción en un canal de transacciones pendientes.

Gestión de Transacciones por el Cajero:
- El cajero recibe la notificación de la transacción.
- El cajero completa o cancela la transacción.
- El bot actualiza el batch y la base de datos con el resultado de la transacción.

Cierre de Batch:
- Al finalizar las transacciones, el revendedor cierra el batch.
- El bot calcula la ganancia generada y la comisión del revendedor.
- El bot actualiza la base de datos con las ganancias y las comisiones.

Backlog de Transacciones:
- Todas las transacciones se registran con timestamps.
- Hay un registro de todas las transacciones realizadas, aprobadas o canceladas.

Gestión de Tasas de Cambio:
- Se establecen tasas de cambio para cada país y moneda.
- Se utiliza una base de datos de países y cuentas asociadas para gestionar las tasas.

### Manejo de las Cuentas con Backlogs
Solicitud de Creación de Cuenta:
- El usuario inicia una solicitud para crear una cuenta.
- Un backlog de solicitudes de cuenta se actualiza con la nueva solicitud.

Aprobación de la Cuenta:
- El superusuario revisa la solicitud de la cuenta en el backlog.
- Una vez aprobada o rechazada, el backlog se actualiza con el resultado.

Creación y Actualización de Cuentas:
- La cuenta se crea en la base de datos si es aprobada.
- Cualquier transacción que actualice el saldo de la cuenta también actualiza el backlog de transacciones de la cuenta.

Backlog de Transacciones:
- Todas las transacciones realizadas o canceladas se registran en un backlog, incluyendo la información sobre saldos anteriores, insertados y actuales.
- Consulta de Saldos de Cuentas con Backlogs

### Consulta de Transacciones y Saldos:
- Los usuarios utilizan comandos para consultar sus saldos y el historial de transacciones, así como sus ganancias asociadas
- Un backlog de consultas se actualiza con cada comando realizado por el usuario.

### Retiro de Ganancias:
- Los usuarios solicitan retirar sus ganancias acumuladas.
- Las solicitudes de retiro se añaden a un backlog de retiros.
- El superusuario procesa las solicitudes de retiro del backlog y actualiza el estado de cada solicitud.

### Cierre de Batch y Backlog de Batches:
- Al cierre de cada batch, se calcula la ganancia total y las comisiones.
- Los detalles del cierre del batch se registran en un backlog de batches.

## Arquitectura del Sistema
### Servicios de la arquitectura
####  Servicio de Bot de Discord:
- Este servicio se encargará de la interacción en tiempo real con los usuarios de Discord.
- Manejará comandos, modales y eventos (como presionar un botón en un embed).
- Gestión de interacciones como selección de roles y solicitudes de transacción.
#### Servicio de Aplicaciones
- Ejecutará la lógica del negocio, procesando las solicitudes del bot y gestionando la lógica de los batches, transacciones, solicitudes y roles.
- Se comunicará con la base de datos y otros servicios según sea necesario.
#### Base de Datos
- Almacenará todos los datos relacionados con usuarios, roles, transacciones, batches, cuentas y tasas de cambio.
- Mantiene backlogs para auditoría, seguimiento y recuperación de datos.
#### Sistema de Gestión de Roles
- Un módulo dedicado para gestionar la asignación y administración de roles de usuario dentro de Discord y en la base de datos.
- Permite la asignación dinámica de roles y gestiona permisos de usuarios.
#### Sistema de Gestión de cuentas
- Manejará la creación de cuentas, asociación con usuarios y actualización de saldos.
- Integrará un mecanismo para la aprobación de cuentas por superusuarios.
#### Motor de Reglas de Negocio
- Definirá y ejecutará las reglas de negocio, como cálculos de comisiones, tasas de cambio y bonificaciones.
- Se adaptará para aplicar diferentes reglas para diferentes países y tipos de usuario.
#### Interfaz de Administración
- Monitoreo de la actividad del sistema y gestión de backlogs.
- Permitirá a los superusuarios gestionar el sistema, aprobar solicitudes, configurar tasas y monedas.
#### Sistema de Backlogs
- Registrará cada acción relevante en la aplicación para propósitos de auditoría y seguimiento.
- Incluirá backlogs de transacciones, solicitudes de cuenta, solicitudes de retiro, y detalles de cierre de batch.
### Componentes de la Arquitectura
#### Interfaz de Usuario (UI)
- Interfaces de Discord para interacción con el bot (modales, mensajes, embeds con botones).
- Panel de control para el superusuario para gestionar solicitudes y supervisar el sistema.
#### Bot de Discord
- Un conjunto de comandos para interacción del usuario (registro, transacciones, consultas, retiros).
- Lógica de negocio para procesar solicitudes y ejecutar acciones en el sistema.
#### Sistema de Gestión de Base de Datos
- Base de datos principal para almacenar usuarios, roles, transacciones, cuentas, y tasas de cambio.
- Base de datos en memoria o temporal para manejar el estado de los batches.
- Backlogs como registros de auditoría para todas las acciones y transacciones.
#### Servicios Backend
- Servicios de Transacción: Encargados de calcular montos, tasas de cambio y comisiones.
- Servicios de Batch: Controlan el inicio, actualización y cierre de batches, así como el cálculo de ganancias y comisiones.
- Servicios de cálculo de transacciones y conversión de divisas.
- Servicios de notificación y mensajería para interactuar con el cajero y los usuarios.
- Servicios de autorización y autenticación para diferentes tipos de usuarios.
#### Sistema de Reportes y Monitoreo
- Herramientas de generación de reportes para estado de cuentas, transacciones, y backlogs.
- Sistema de monitoreo y alertas para la actividad del sistema y la auditoría.
#### Integración con Sistemas Externos
- Herramientas de terceros para la gestión de proyectos y tareas (por ejemplo, Notion).
### Herramientas para la escalabilidad
#### Escalabilidad:
- Arquitectura diseñada para escalar, posiblemente utilizando servicios en la nube que puedan manejar aumentos en la carga de trabajo.
- Uso de microservicios o contenedores para manejar diferentes partes del sistema de forma independiente.
#### Microservicios:
- Considerar una arquitectura basada en microservicios para manejar diferentes aspectos del sistema de forma modular y escalable.
- Orquestación de Microservicios: Utiliza herramientas como Kubernetes para gestionar los microservicios, lo que te permitirá escalar y desplegar servicios de manera más eficiente.
- Balanceo de Carga: Implementa balanceadores de carga para distribuir el tráfico entre instancias de servicios y mejorar la disponibilidad y tiempo de respuesta.
#### Bases de Datos
- Replicación de Base de Datos: Configura la replicación de bases de datos para mejorar la disponibilidad y el rendimiento en lecturas.
- Particionamiento de Datos: Considera la posibilidad de particionar tus bases de datos para manejar grandes volúmenes de datos y mejorar el rendimiento de las consultas.
#### Sistema de Backlogs
- Sistema de Colas de Mensajes: Implementa colas de mensajes (como RabbitMQ o Kafka) para manejar tareas asíncronas y asegurar la entrega de mensajes entre diferentes componentes del sistema.
#### Sistemas de Seguridad
- Firewalls de Aplicaciones Web (WAF): Protege tus servicios de aplicaciones con WAF para detectar y bloquear ataques maliciosos.
- Gestión de Identidades y Accesos: Utiliza proveedores de identidades como Auth0 o Keycloak para una gestión centralizada de usuarios y permisos.
#### Interfaz y Experiencia de  Usuario
- Diseño de Interfaz de Usuario Consistente: Asegúrate de que todas las interfaces de usuario sigan un diseño coherente y sean accesibles.
- Pruebas de Usabilidad: Realiza pruebas de usabilidad para garantizar que la experiencia del usuario sea intuitiva y eficiente.
Mejoras en la Internacionalización
#### Monitoreo y Registro
- Plataformas de Monitoreo: Emplea plataformas como Prometheus y Grafana para monitorear el rendimiento y la salud de tu infraestructura.
- Registro Centralizado: Utiliza soluciones de registro centralizado como ELK Stack para recopilar y analizar logs de todos tus servicios.

## Modelado de la Base de Datos
### Entidades Principales:
#### Usuarios:
- Atributos: ID de Usuario, Nombre de Usuario, UID de Discord, Timestamp de Registro, Timestamp AprobacionRegistro, Rol (con referencia a la entidad Roles).
- Relaciones: Relacionado con Transacciones, Cuentas, Solicitudes de Rol.
#### Roles:
- Atributos: ID de Rol, Nombre del Rol, Permisos.
- Relaciones: Asignados a Usuarios.
#### Cuentas:
- Atributos: ID de Cuenta, ID de Usuario asociado, Tipo de Cuenta, Saldo Anterior, Saldo Insertado, Saldo Actual, País, Valor Relativo en $.
- Relaciones: Pertenece a un Usuario, Asociada con Transacciones.
#### Transacciones:
- Atributos: ID de Transacción, ID de Usuario, Tipo (Revendedor/Cliente), ID de Cuenta Emisora, ID de Cuenta Receptora, Monto, Tasa de Cambio, Comisión, Estado (Realizada/Cancelada), TimestampEnvio, TimestampAprobado
- Relaciones: Relacionadas con Usuarios, Cuentas.
#### Batches:
- Atributos: ID de Batch, ID de Usuario (Revendedor), Estado (Abierto/Cerrado), Timestamp de Inicio, Timestamp de Cierre.
- Relaciones: Agrupa Transacciones.
#### Tasas de Cambio:
- Atributos: ID de Tasa, País, Moneda, Valor.
- Relaciones: Utilizadas en Transacciones.
#### Backlogs:
- Atributos: ID de Backlog, Tipo (Transacción, Solicitud de Cuenta, Solicitud de Retiro, Detalle de Batch), ID de Registro Asociado, TimestampInicio, TimestampFin, Estado (Pendiente/Aprobado/Rechazado).
- Relaciones: Referencia a Transacciones, Cuentas, Batches según el tipo.
#### Solicitudes:
- Atributos: ID de Solicitud, Tipo (Rol, Cuenta, Retiro), ID de Usuario, Timestamp, Estado (Pendiente/Aprobado/Rechazado).
- Relaciones: Relacionadas con Usuarios.
### Relaciones:
- Usuarios a Roles: Relación de uno a muchos, donde un usuario puede tener múltiples roles.
- Usuarios a Cuentas: Relación de uno a muchos, donde un usuario puede tener múltiples cuentas.
- Cuentas a Transacciones: Relación de uno a muchos, donde una cuenta puede estar involucrada en múltiples transacciones.
- Usuarios a Transacciones: Relación de uno a muchos, donde un usuario puede iniciar múltiples transacciones.
- Batches a Transacciones: Relación de uno a muchos, donde un batch agrupa múltiples transacciones.
- Backlogs a Registros: Relación polimórfica, donde un backlog puede referenciar a diferentes tipos de registros (Transacciones, Cuentas, Batches).

### Consideraciones:
- Índices: Utilizar índices en los campos que se consultan frecuentemente para mejorar el rendimiento de las consultas.
- Seguridad: Implementa medidas de seguridad adecuadas, como cifrado para datos sensibles y control de acceso basado en roles.


## Planificación del Proyecto
### Microservicio de Gestión de Usuarios y Roles
- Responsabilidades: Maneja el registro de usuarios, la asignación y gestión de roles dentro de Discord y la base de datos.
- Casos de Uso Principales: Registro de usuarios, selección y asignación de roles.
- Tecnologías Sugeridas: Python, SQLite3/aiSQLite para la gestión de datos de usuarios y roles.
### Microservicio de Gestión de Cuentas y Transacciones
- Responsabilidades: Administra las cuentas de los usuarios y procesa las transacciones, incluyendo la creación de cuentas, actualización de saldos, y manejo de transacciones y batches.
- Casos de Uso Principales: Creación y actualización de cuentas, manejo de transacciones, inicio y cierre de batches.
- Tecnologías Sugeridas: Python, SQLite3/aiSQLite, con lógica para manejar transacciones basadas en los mensajes de Discord.
### Microservicio de Bot de Discord
- Responsabilidades: Interactúa con los usuarios a través de Discord, manejando comandos y eventos, y sirve como el punto de integración para otros microservicios.
- Casos de Uso Principales: Procesamiento de comandos de Discord, interacción directa con los usuarios.
- Tecnologías Sugeridas: Python con la biblioteca Nextcord.
### Microservicio de Reportes y Monitoreo
- Responsabilidades: Genera reportes sobre el estado de cuentas, transacciones y ofrece herramientas de monitoreo para la actividad del sistema.
- Casos de Uso Principales: Reportes de estado de cuentas y transacciones, monitoreo del sistema.
- Tecnologías Sugeridas: ELK Stack para logging y análisis, Prometheus y Grafana para monitoreo.

### Metodología Ágil

### Sprints y Tareas

## Gestión de Repositorios

## Pruebas y Calidad del Código

## Despliegue y Mantenimiento

## Conclusiones y Próximos Pasos
