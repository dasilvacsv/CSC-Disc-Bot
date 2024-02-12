
Modelo de Datos Preliminar
Tabla Usuarios:
ID de Usuario (autogenerado)
Username (Discord Username)
Discord UID
Timestamp de Registro
Rol (Cliente, Revendedor, Cajero, Super Usuario)

Tabla Cuentas Asociadas:
ID de Cuenta (asociado al Usuario)
Saldo Anterior
Saldo Insertado
Saldo Actual
Transacciones (relacionadas con el Batch)

Tabla Batches:
ID de Batch
ID del Canal de Transacciones
ID del Usuario Revendedor
Saldos Iniciales y Actuales
Transacciones Acumuladas
Estado (Abierto/Cerrado)

Tabla Transacciones:
ID de Transacción
ID de Batch
Monto
Tasa Aplicada
Comisión
Estado (Pendiente, Realizada, Cancelada)
Timestamps de Creación y Resolución

Tabla País:
ID de País
Nombre del País
Monedas Disponibles
Tasa de Cambio

Tabla Backlog de Transacciones y Batches:
ID de Registro
Detalles de la Transacción/Batch
Timestamps
Ganancias y Comisiones

