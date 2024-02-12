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