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