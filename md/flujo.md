# Registro de usuario
El registro de usuario lleva el siguiente flujo
tengo mi base de datos de usuario que registra, un id autoincrement de usuario, el usuario, que será = al discord.username, el Discord uid que será = al discord.uid, lleva una cuenta o cuentas asociadas no sé como manejar esto en la base de datos pero tendría la siguiente estructura
if there is 1 cuenta it will have  the following fields, valor insertado, valor anterior, valor actual, entonces por cada cuenta que tenga asociada, se actualizarán esos 3 valores aunque creo que eso podría estar directamente relacionado en una tabla de cuentas en la base de datos, quiero ir modelando todo en base a mi base de datos, pero entonces al registrarse un usuario la información principal será:
id
username
discord.uid
timestampregistro
rol
El manejo de roles será a través de un embed donde selecciona un botón donde tendrá varias opciones, en este caso ya yo tengo una lógica desarrollada anteriormente con este código que más adelante te comentaré, al seleccionar el embed, se prouce un timestamp de registro y se envía una solicitud a un canal a un usuario superuser, que aceptará o rechazará la solicitud
cabe destacar que las solicitudes se guardarán en una tabla backlog solicitudes donde irá el registro de, todas las peticiones de rol, el manejo de las solicitudes aceptas y las rechazadas, luego de este el fin termina en un registro del usuario con el rol asignado en la base de datos, quiero que al aceptarse la request el id del rol sea asignado al usuario y así finalizaría el registro de usuario, cabe destacar que cada usuario tendrá tambien un registro de sus ganancias y una tabla donde se llevará todo el flow de ganancias y transacciones que afectan estas, por lo que creo que con este flujo puedes diagramarme algo mejor para construir un diagrama de esto, esto solo aborda el registro de usuario al entrar al servidor

# Transacciones
SelfCreated Transaction
Entonces en nuestra aplicación tenemos distintos tipos de usuarios, y transacciones, tenemos a los usuarios que son los revendedores, la características de los revendedores es que pueden tener clientes registrados asociados a la base de datos y que les generan comisión al estar referidos por ellos, tenemos a los clientes normales que solo están registrados y generan puntos por cada transacción que realizan con nosotros, tenemos al super usuario que puede hacer de todo en la aplicacion mover cambiar otorgar permisos, y tenemos a los cajeros, que se encargan de recibir las transacciones que envian los revendedores o clientes y registrarlas como realizada o cancelada, esto tendrá un backlog donde se registran si la transaccion fue realizada o cancelada y esto a su vez llevará un registro de, por ejemplo El Revendeodr David, registrado en la base de datos como Revendedor, realiza el comando !t 100 p (p sería la tasa publicada) esto realizaría la lógica de lo que sería nuestra tabla de base de datos tenemos que ver como manejar estas operaciones de setRates para cada país, tenemos que crear una base de datos de país y las cuentas asociadas, etnocnes para empezar a trabajar con un usuario tenemos que crear batches que irán acumualndo las transacciones desde donde salen hasta donde entran por ejemplo, al david estar registrado, irá al canal #transacciones-david donde en la base de datos se registrará canal-uid, nombre-canal, y que almacenará la lógica de los batches, entonces  ya teniendo a david, antes de empezar tenemos que crear un batch que creará una base de datos en memoria que se puede manejar con una base de datos alterna que leugo afectará a las cuentas principales al realizar endbatch
un ejemplo es
en el canal de transacciones david tenemos a los actores david y el cajero1, o todos los que se puedan ir asociado, el batch irá asociando toda esa base de datos de la siguiente manera
!start batch
Datos iniciales
David-cuentas
Cuenta Receptora: Cuenta Soles Saldo: 0
Cuenta Emisora: Cuenta Venezuela Saldo Enviado: 0
!t 100 p, hará la multiplicación por la tasa publicada y daría 900Bs la moneda de Venezuela, cabe destacar que if transaction venezuela se le suma un 0.3%, y quiero dejar esta funcionalidad de % de comision por realizacion de transferencia si en otro país se aplica la misma lógica para transferir
esto enviará un mensaje al privado al cajero y un mensaje a un canal de transacciones-pending, si fue realizada, el cajero responde con el capture, y presiona en listo asi como la lógica de registro de usuarios y si fue cancelada, le da click en cancelar 
entonces luego de esta transaccion, si fue realizada se sumaría y quedaría así el batch, cabe destacar que el valor relativo en $ para que los bs se calculen en $ debe estar puesto en la base de datos tipo !setBsusdValue 38
entonces al terminarse la transaccion llegaría un embed con la información actualizada del batch
informacion del batch
Datos iniciales
David-cuentas
Cuenta Receptora: Cuenta Soles Saldo: 100S
Cuenta Emisora: Cuenta Venezuela Saldo Enviado: 902.7Bs
Cantidad enviada en $: 23.755$
y al cerrar el bache se coloca el monto equivalente a los Soles en USDT por ejemplo
david realizó otra transacción la cual es !t 100 9.2
entonces serían 920bs
la transacción sería realizada, y al ser realizada llegaría un embed al canal de david donde se actualizaría la información del batch
Datos iniciales
David-cuentas
Cuenta Receptora: Cuenta Soles Saldo: 200S
Cuenta Emisora: Cuenta Venezuela Saldo Enviado: 1825.46Bs
Cantidad enviada en $: 48.03$
entonces este seria mi bache ya con 2 transacciones, al DAvid comprar los usdt, me colocaría
!c (cantidad del bache comprada) (monto usdt)
entonces sería en este caso !c 200 52.63
esto arrojaría un 
Se ha realizado un cierre de bache, dando un valor promedio que será (cantidad comprada) / (cantidad de usdt) = valor del usdt comprado, esto me dará un vaalor que irá a un backlog después igual que todas las transacciones que se realizan en baches tendrán un Bachebacklog
Datos iniciales
David-cuentas
Cuenta Receptora: Cuenta Soles Saldo: 200S
Cantidad $ USD = 52.63$
Cuenta Emisora: Cuenta Venezuela Saldo Enviado: 1825.46Bs
Cantidad enviada en $: 48.03$
Ganancia generada en el bache = 4.6$
Cut del Reseller = (consulta la base de datos para consultar el % de este, ejemplo 40%) y multiplica por ganancia generando en le bache = 1.84$
entonces ahora el valor de gannacia david en usuario sería actualizado a 1.84$, y el resto que quedó sería sumado a Ganancia Cajero
ahi terminaría la lógica del bache, quiero tener backlog de todas las transacciones con timestamps de cuando una transaccion se realiza y cuando se aprueba o se cancela
tambine cabe destacar que en la base de datos de pais, debe haber una columna de monedas
y en la base de datos de cuentas debe haber un id asociado a un usuario


CashierCreated Transactions

# Manejo de las cuentas
El manejo de las cuentas tiene que tener un registro, donde el usuario pueda interactuar y crear cuentas, esta acción debería ser llevada a cabo en un registro previo, puede ser con un modal, y sea aprobado por un superusuario, al tener una cuenta asociado, esta tendrá el valor de saldo anterior, saldo insertado, y saldo actual que se actualizaría solo con las transacciones que son realizadas, no las canceladas, las cuentas estarán asociadas a países y cada cuenta tendrá su valor relativo en $ en algun momento para el cálculo de gannacia
# Consulta de saldos cuentas
Los usuarios podrán verificar las ganancias asociadas a ellos, la cantidad de transacciones, las transacciones que tengan en estado pendiente, las transacciones canceladas, todo con comandos, cada usuario tendrá una manera de retirar las ganancias con un comando request que debe ser aprobado por un super usuario que funcionará por ejemplo el usuario irá acumulando comisiones hasta llegar a cierta canitdad e ir al canal de !request-retiro
 netonces la solicitud llegará al superusuairo que verificará pagará, y reiniciará las gnancias del usuario, quiero poder manejar toda esta lógica, y la monetización es a través de los batches
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