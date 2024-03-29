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

#Consulta para la busqueda de cuentas
async def autocomplete_cuentas(ctx: discord.AutocompleteContext):
    cuentas = []
    async with aiosqlite.connect('main.db') as db:
        async with db.execute("SELECT DISTINCT NombreCuenta FROM Cuentas") as cursor:
            async for row in cursor:
                cuentas.append(row[0])
    return [cuenta for cuenta in cuentas if ctx.value.lower() in cuenta.lower()]

#Función de autocompletar paises
async def autocomplete_paises(ctx: discord.AutocompleteContext):
    paises = []
    async with aiosqlite.connect('main.db') as db:
        async with db.execute("SELECT DISTINCT Nombre FROM Paises") as cursor:
            async for row in cursor:
                paises.append(row[0])
    return [paise for paise in paises if ctx.value.lower() in paise.lower()]

# Transaction and Batch handling

class TransaccionesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Comando para establecer presetsF
    @slash_command(name="pre", description="Establece los presets para un canal.")
    async def pre(self, ctx, paisreceptor: Option(str, "Elige país desde donde se envía", autocomplete=basic_autocomplete(autocomplete_paises)), paisemisor: Option(str, "Elige país al que se envía", autocomplete=basic_autocomplete(autocomplete_paises)), cuentareceptora: Option(str, "Elige cuenta que recibe", autocomplete=basic_autocomplete(autocomplete_cuentas)), cuentaemisora: Option(str, "Elige cuenta que envía", autocomplete=basic_autocomplete(autocomplete_cuentas))): #type: ignore 
        channel_id = str(ctx.channel.id)

        async with aiosqlite.connect('main.db') as db:
            # Store the presets for the channel in the database
            await db.execute('''INSERT OR REPLACE INTO Presets (ChannelID, PaisReceptor, PaisEmisor, CuentaReceptora, CuentaEmisora) 
                                VALUES (?, ?, ?, ?, ?)''', 
                             (channel_id, paisreceptor, paisemisor, cuentareceptora, cuentaemisora))
            await db.commit()

        await ctx.respond(f"Presets establecidos para este canal.")

    # Comando para registrar una transacción segun presetsF
    @slash_command(name="regp", description="Registra una nueva transacción utilizando los presets.")
    async def regp(self, ctx, monto: float, tasa: float):
        user_id = str(ctx.author.id)
        channel_id = str(ctx.channel.id)
        timestamp = datetime.datetime.now().isoformat()

        async with aiosqlite.connect('main.db') as db:
            # Retrieve the presets for the channel from the database
            cursor = await db.execute("SELECT PaisEmisor, PaisReceptor, CuentaEmisora, CuentaReceptora FROM Presets WHERE ChannelID = ?", (channel_id,))
            result = await cursor.fetchone()
            if result is None:
                await ctx.respond(f"No hay presets establecidos para este canal.")
                return
            pais_emisor, pais_receptor, cuenta_emisora, cuenta_receptora = result

            # Retrieve the active batch for the channel from the database
            cursor = await db.execute("SELECT BatchID FROM Batches WHERE ChannelID = ? AND Status = 'Open'", (channel_id,))
            result = await cursor.fetchone()
            if result is None:
                await ctx.respond(f"No hay un batch activo para este canal.")
                return
            batch_id = result[0]

            # Retrieve the last used number from the database
            cursor = await db.execute("SELECT value FROM Counters WHERE name = 'transaction_id'")
            result = await cursor.fetchone()
            if result is None:
                # If the counter does not exist, create it with a value of 1
                await db.execute("INSERT INTO Counters (name, value) VALUES ('transaction_id', 1)")
                transaction_id = "0000001"
            else:
                # If the counter exists, increment it and update the database
                new_value = result[0] + 1
                await db.execute("UPDATE Counters SET value = ? WHERE name = 'transaction_id'", (new_value,))
                transaction_id = f"{new_value:07d}"
            monto_total = monto * tasa #Logica para el calculo del monto total
                
            await db.execute('''INSERT INTO Transacciones (TransactionID, BatchID, UserID, Timestamp, Status, Monto, Tasa, MontoTotal, PaisEmisor, PaisReceptor, CuentaEmisora, CuentaReceptora) 
                                VALUES (?, ?, ?, ?, 'Pending', ?, ?, ?, ?, ?, ?, ?)''', 
                             (transaction_id, batch_id, user_id, timestamp, monto, tasa, monto_total, pais_emisor, pais_receptor, cuenta_emisora, cuenta_receptora))
            await db.commit()
        
            # Crear y configurar el embed con la información de la transacción
            embed = discord.Embed(title="Nueva Transacción", description="Detalles de la transacción pendiente")
            embed.add_field(name="Usuario", value=str(ctx.author), inline=True)
            embed.add_field(name="Monto", value=str(monto), inline=True)
            embed.add_field(name="Tasa", value=str(tasa), inline=True)
            embed.add_field(name="Monto Total", value=str(monto_total), inline=True)
            embed.add_field(name="Cuenta Receptora", value=cuenta_receptora, inline=True)
            embed.add_field(name="Cuenta Emisora", value=cuenta_emisora, inline=True)


    # Obtener el canal y el miembro Cajero
        transaction_queue_channel = self.bot.get_channel(1207153726239023175)  # Asegúrate de que el ID del canal es correcto
        cajero_member = ctx.guild.get_member(1176991779208319016)  # Asegúrate de que el ID del miembro es correcto

    # Enviar el embed al canal y al Cajero
        await transaction_queue_channel.send(embed=embed)
        await cajero_member.send(embed=embed)
        await ctx.respond(f"Transacción {transaction_id} registrada en el batch {batch_id} por {ctx.author.mention}")
    
    # Comando para iniciar un batchF
    @slash_command(name="inicia_ba", description="Inicia un nuevo batch de transacciones.")
    async def inicia_ba(self, ctx):
        user_id = str(ctx.author.id)
        channel_id = str(ctx.channel.id)
        start_time = datetime.datetime.now().isoformat()

        async with aiosqlite.connect('main.db') as db:
            # Check if a batch already exists for the channel
            cursor = await db.execute("SELECT * FROM Batches WHERE ChannelID = ?", (channel_id,))
            result = await cursor.fetchone()
            if result is not None:
                await ctx.respond(f"Ya existe un batch para este canal.")
                return

            # Retrieve the last used number from the database
            cursor = await db.execute("SELECT value FROM Counters WHERE name = 'batch_id'")
            result = await cursor.fetchone()
            if result is None:
                # If the counter does not exist, create it with a value of 1
                await db.execute("INSERT INTO Counters (name, value) VALUES ('batch_id', 1)")
                batch_id = "0000001"
            else:
                # If the counter exists, increment it and update the database
                new_value = result[0] + 1
                await db.execute("UPDATE Counters SET value = ? WHERE name = 'batch_id'", (new_value,))
                batch_id = f"{new_value:07d}"

            await db.execute('''INSERT INTO Batches (BatchID, UserID, ChannelID, StartTime, Status) 
                                VALUES (?, ?, ?, ?, 'Open')''', 
                             (batch_id, user_id, channel_id, start_time))
            await db.commit()

        await ctx.respond(f"Batch {batch_id} iniciado por {ctx.author.mention}")  

    # Comando slash para cerrar un batch con opción
    @slash_command(name="cerra_bach", description="Cierra un batch de transacciones.")
    async def cerra_bach(self, ctx, batch_id: Option(str, "ID del batch a cerrar", autocomplete=basic_autocomplete(autocomplete_batch_ids),), valor_liquidacion: float): #type: ignore
        total_transacciones = 0
        transacciones_liquidar = []
        async with aiosqlite.connect('main.db') as db:
            async with db.execute("SELECT * FROM Transacciones WHERE BatchID = ? AND Status = 'Completed'", (batch_id,)) as cursor:
                async for row in cursor:
                    total_transacciones += float(row[6])  # Access the 'Amount' column using the index 2
                    transacciones_liquidar.append(row)
                    print(total_transacciones)
                    print(transacciones_liquidar)
            if total_transacciones != 0:
                factor_liquidacion = int(valor_liquidacion) / int(total_transacciones)

                for transaccion in transacciones_liquidar:
                    monto_liquidado = int(transaccion[6]) * int(factor_liquidacion)  # Access the 'Amount' column using the index 2
                    await db.execute("UPDATE Transacciones SET LiquitatedAmount = ?, Status = 'Liquidated' WHERE TransactionID = ?", (monto_liquidado, transaccion[0]))  # Access the 'TransactionID' column using the index 0
                await db.execute("UPDATE Batches SET Status = 'Closed' WHERE BatchID = ?", (batch_id,))
                await db.commit()
                await ctx.respond(f"Batch {batch_id} cerrado correctamente.")
            else:
                await ctx.respond(f"Error: No se pueden realizar divisiones por cero.")
            

    #Estado del batch
    @slash_command(name="estdo_batch", description="Muestra el estado del batch.")
    async def estado_batch(self, ctx, batch_id: Option(str, "ID del batch a cerrar", autocomplete=basic_autocomplete(autocomplete_batch_ids))): #type: ignore
        transacciones = {'Pending': [], 'Completed': [], 'Cancelled': []}
        async with aiosqlite.connect('main.db') as db:
                async with db.execute("SELECT * FROM Transactions WHERE BatchID = ?", (batch_id,)) as cursor:
                    async for row in cursor:
                        transacciones[row['Status']].append(row)
                print(transacciones)

    
    
    
    
    
    
    
    
    
    @slash_command(name="regise", description="Registra una nueva transacción.")  
    async def registrar_transaccion(self, ctx, monto: Option(int, "Monto de la transacción"), tasa: Option(int, "Tasa de conversión"), cuenta_entrada: Option(str, "Cuenta de entrada", autocomplete=basic_autocomplete(autocomplete_cuentas)), cuenta_salida: Option(str, "Cuenta de salida", autocomplete=basic_autocomplete(autocomplete_cuentas))): #type: ignore
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
            INSERT INTO Transacciones (TransactionID, BatchID, SenderAccountID, ReceiverAccountID, Amount, Timestamp, Status)
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
