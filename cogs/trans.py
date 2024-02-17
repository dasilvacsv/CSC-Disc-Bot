import discord
from discord.ext import commands
from discord.ui import Button, View
import datetime
import aiosqlite
import asyncio
from discord.utils import basic_autocomplete
from discord.commands import slash_command, Option

# Definicion de intents para Prefixed Commands
intents = discord.Intents.all()

class ApproveButton(Button):
    def __init__(self, transaction_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.transaction_id = transaction_id
    async def callback(self, interaction: discord.Interaction):
        # Format the current timestamp
        current_timestamp = datetime.datetime.now().isoformat()
        await interaction.response.defer()
        async with aiosqlite.connect('main.db') as db:
            await db.execute("UPDATE Transacciones SET Status = ?, TimestampApproved = ? WHERE TransactionID = ?", ('Completed', current_timestamp, self.transaction_id))
            await db.commit()
        await interaction.followup.send(f"Your request for the {self.transaction_id} role was accepted.", ephemeral=True)


class RejectButton(Button):
    def __init__(self, transaction_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.transaction_id = transaction_id
    async def callback(self, interaction: discord.Interaction):
        # Format the current timestamp
        current_timestamp = datetime.datetime.now().isoformat()
        await interaction.response.defer()
        async with aiosqlite.connect('main.db') as db:
            await db.execute("UPDATE Transacciones SET Status = ?, TimestampRejected = ? WHERE TransactionID = ?", ('Rejected', current_timestamp, self.transaction_id))
            await db.commit()
        await interaction.followup.send(f"your request for the {self.transaction_id} role was rejected.", ephemeral=True)

class TransactionView(View):
    def __init__(self, transaction_id):
        super().__init__()

        approve_button = (ApproveButton(transaction_id, label="Realizada", style=discord.ButtonStyle.success))
        reject_button = (RejectButton(transaction_id, label="Cancelada", style=discord.ButtonStyle.danger))

        self.add_item(approve_button)
        self.add_item(reject_button)

class RegistroTransacciones(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot
        self.monto = None
        self.tasa = None
    
    @slash_command(name="cat",  description="Cierra un batch de transacciones.")
    async def register(self, ctx, monto: float, tasa: float):
        canal = self.bot.get_channel(1207030045936197652)
        user_id = str(ctx.author.id)
        channel_id = str(ctx.channel.id)
        self.monto = monto
        self.tasa = tasa
        timestamp = datetime.datetime.now().isoformat()
        
        await ctx.respond(f"Your transaction is pending now.")
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
        





            print(pais_emisor, pais_receptor, cuenta_emisora, cuenta_receptora, batch_id, transaction_id, monto_total)     
        

        embed2 = discord.Embed(title="Registro de Usuarios", description="Selecciona tu rol:")
        embed2.add_field(name="Usuario", value=str(self.tasa), inline=True)
        embed2.add_field(name="Monto", value=str(self.monto), inline=True)
        embed2.add_field(name="Tasa", value=str(timestamp), inline=True)

        
        embed = discord.Embed(title="Registro de Usuarios", description="Selecciona tu rol:")
        embed.add_field(name="Usuario", value=str(self.tasa), inline=True)
        embed.add_field(name="Monto", value=str(self.monto), inline=True)
        embed.add_field(name="Tasa", value=str(timestamp), inline=True)

        view = TransactionView(transaction_id)

        await ctx.respond(embed=embed)


        # Obtener el canal y el miembro Cajero
        transaction_queue_channel = self.bot.get_channel(1207153726239023175)  # Asegúrate de que el ID del canal es correcto
        cajero_member = ctx.guild.get_member(1176991779208319016)  # Asegúrate de que el ID del miembro es correcto

    # Enviar el embed al canal y al Cajero
        await transaction_queue_channel.send(embed=embed2, view=view)
        await cajero_member.send(embed=embed2)
        await ctx.respond(f"Transacción {transaction_id} registrada en el batch {batch_id} por {ctx.author.mention}")
    










def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(RegistroTransacciones(bot)) # add the cog to the bot
