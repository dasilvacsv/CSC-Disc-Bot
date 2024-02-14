import discord
from discord.ext import commands
from discord.ui import Button, View
from discord.commands import slash_command, Option
import uuid
import aiosqlite
import datetime
from discord.utils import basic_autocomplete
#Definicion de intents para Prefixed Commands
intents = discord.Intents.all()



# Consulta para la búsqueda de batches

async def autocomplete_batch_ids(ctx: discord.AutocompleteContext):
        user_id = str(ctx.interaction.user.id)
        batches = []

        async with aiosqlite.connect('main.db') as db:
            async with db.execute("SELECT BatchID FROM Batches WHERE UserID = ? AND Status = 'Open'", (user_id,)) as cursor:
                async for row in cursor:
                    batches.append(row[0])
        return [batch_id for batch_id in batches if ctx.value.lower() in batch_id.lower()]

async def autocomplete_cuentas(ctx: discord.AutocompleteContext):
    cuentas = []
    async with aiosqlite.connect('main.db') as db:
        async with db.execute("SELECT DISTINCT NombreCuenta FROM Cuentas") as cursor:
            async for row in cursor:
                cuentas.append(row[0])
    return [cuenta for cuenta in cuentas if ctx.value.lower() in cuenta.lower()]

# Transaction and Batch handling

class TransaccionesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Comando para iniciar un batch
    @slash_command(name="iniciar_ba", description="Inicia un nuevo batch de transacciones.")
    async def iniciar_ba(self, ctx):
        user_id = str(ctx.author.id)
        start_time = datetime.datetime.now().isoformat()
        batch_id = str(uuid.uuid1())

        async with aiosqlite.connect('main.db') as db:
            await db.execute('''INSERT INTO Batches (BatchID, UserID, StartTime, Status) 
                                VALUES (?, ?, ?, 'Open')''', 
                             (batch_id, user_id, start_time))
            await db.commit()

        await ctx.respond(f"Batch {batch_id} iniciado por {ctx.author.mention}")
   
   
    # Comando slash para cerrar un batch con opción
    @slash_command(name="cerrar_bach", description="Cierra un batch de transacciones.")
    async def cerrar_bach(self, ctx, batch_id: Option(str, "ID del batch a cerrar", autocomplete=basic_autocomplete(autocomplete_batch_ids),), valor_liquidacion: float):
        total_transacciones = 0
        transacciones_liquidar = []
        async with aiosqlite.connect('main.db') as db:
            async with db.execute("SELECT * FROM Transactions WHERE BatchID = ? AND Status = 'Completed'", (batch_id,)) as cursor:
                async for row in cursor:
                    total_transacciones += row['Amount']
                    transacciones_liquidar.append(row)

            factor_liquidacion = valor_liquidacion / total_transacciones
            for transaccion in transacciones_liquidar:
                monto_liquidado = transaccion['Amount'] * factor_liquidacion
                await db.execute("UPDATE Transactions SET LiquidatedAmount = ?, Status = 'Liquidated' WHERE TransactionID = ?", (monto_liquidado, transaccion['TransactionID']))
            await db.execute("UPDATE Batches SET Status = 'Closed' WHERE BatchID = ?", (batch_id,))
            await db.commit()

            await ctx.respond(f"Batch {batch_id} cerrado correctamente.")
        
    @slash_command(name="estado_batch", description="Muestra el estado del batch.")
    async def estado_batch(self, ctx, batch_id: Option(str, "ID del batch a cerrar", autocomplete=basic_autocomplete(autocomplete_batch_ids))):
        transacciones = {'Pending': [], 'Completed': [], 'Cancelled': []}
        async with aiosqlite.connect('main.db') as db:
                async with db.execute("SELECT * FROM Transactions WHERE BatchID = ?", (batch_id,)) as cursor:
                    async for row in cursor:
                        transacciones[row['Status']].append(row)
                print(transacciones)

    @slash_command(name="registrar", description="Registra una nueva transacción.")  
    async def registrar_transaccion(self, ctx, monto: Option(int, "Monto de la transacción"), tasa: Option(int, "Tasa de conversión"), cuenta_entrada: Option(str, "Cuenta de entrada", autocomplete=basic_autocomplete(autocomplete_cuentas)), cuenta_salida: Option(str, "Cuenta de salida", autocomplete=basic_autocomplete(autocomplete_cuentas))):
        user_id = ctx.author.id  # ID del usuario que ejecuta el comando
        total_salida = monto * tasa  # Cálculo del total en la cuenta de salida

    # Crear y configurar el embed con la información de la transacción
        embed = discord.Embed(title="Nueva Transacción", description="Detalles de la transacción pendiente")
        embed.add_field(name="Usuario", value=str(ctx.author), inline=True)
        embed.add_field(name="Monto", value=str(monto), inline=True)
        embed.add_field(name="Tasa", value=str(tasa), inline=True)
        embed.add_field(name="Total Salida", value=str(total_salida), inline=True)
        embed.add_field(name="Cuenta Entrada", value=cuenta_entrada, inline=True)
        embed.add_field(name="Cuenta Salida", value=cuenta_salida, inline=True)
        
        # Generar un ID único para la transacción
        transaction_id = str(uuid.uuid4())
        timestamp = datetime.datetime.now().isoformat()
        status = 'Pending'  # El estado inicial de la transacción

    # Insertar la transacción en la base de datos
        async with aiosqlite.connect('main.db') as db:
            await db.execute('''
            INSERT INTO Transactions (TransactionID, BatchID, SenderAccountID, ReceiverAccountID, Amount, Timestamp, Status)
            VALUES (?, 0, ?, ?, ?, ?, ?)
        ''', (transaction_id, cuenta_entrada, cuenta_salida, monto, timestamp, status))
            await db.commit()

    # Obtener el canal y el miembro Cajero
        transaction_queue_channel = self.bot.get_channel(1207153726239023175)  # Asegúrate de que el ID del canal es correcto
        cajero_member = ctx.guild.get_member(1176991779208319016)  # Asegúrate de que el ID del miembro es correcto

    # Enviar el embed al canal y al Cajero
        await transaction_queue_channel.send(embed=embed)
        await cajero_member.send(embed=embed)

    # Responder al usuario
        await ctx.respond(f"Transacción {transaction_id} registrada y enviada a la cola.")

# Función para añadir el cog al bot

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(TransaccionesCog(bot)) # add the cog to the bot
