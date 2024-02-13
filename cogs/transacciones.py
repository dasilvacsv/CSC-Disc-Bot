import discord
from discord.ext import commands
from discord.ui import Button, View
from discord.commands import slash_command, Option
import uuid

import datetime
#Definicion de intents para Prefixed Commands
intents = discord.Intents.all()
# Transaction and Batch handling
class Transaccion:
    def __init__(self, emisor, monto_emisor, tasa, monto_receptor, timestamp):
        self.emisor = emisor
        self.monto_emisor = monto_emisor
        self.tasa = tasa
        self.monto_receptor = monto_receptor
        self.timestamp = timestamp
        self.estado = "pendiente"
        self.custom_id = str(uuid.uuid4())  # Genera un identificador único para cada transacción

class Batch:
    def __init__(self):
        self.transacciones = []
        self.total_emisor = 0
        self.total_receptor = 0

    def agregar_transaccion(self, transaccion):
        self.transacciones.append(transaccion)

    def actualizar_totales(self, transaccion):
        if transaccion.estado == "aprobada":
            self.total_emisor += transaccion.monto_emisor
            self.total_receptor += transaccion.monto_receptor

# Aprobacion y Rejection Handling
class AprobarButton(discord.ui.Button):
    async def callback(self, interaction: discord.Interaction):
        custom_id = interaction.data['custom_id'].split("_")[1]  # Extraer el custom_id de la transacción
        transaccion = self.view.cog.transacciones_pendientes.get(custom_id)  # Acceder a la transacción pendiente
        if transaccion:
            transaccion.estado = "aprobada"
            self.view.cog.batch_actual.actualizar_totales(transaccion)  # Actualizar totales del batch si es necesario
            await interaction.response.send_message("Transacción aprobada.", ephemeral=True)

class RechazarButton(discord.ui.Button):
    async def callback(self, interaction: discord.Interaction):
        custom_id = interaction.data['custom_id'].split("_")[1]
        transaccion = self.view.cog.transacciones_pendientes.get(custom_id)
        if transaccion:
            transaccion.estado = "rechazada"
            await interaction.response.send_message("Transacción rechazada.", ephemeral=True)

#View of Buttons on Transaction
class TransaccionView(discord.ui.View):
    def __init__(self, custom_id):
        super().__init__()
        self.add_item(AprobarButton(custom_id=custom_id))
        self.add_item(RechazarButton(custom_id=custom_id))

class SistemaTransacciones(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot
    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot
        self.batch_actual = Batch()
        self.transacciones_pendientes = {}

    @commands.slash_command(name="registrar", description="Registra una nueva transacción en el batch actual.")
    async def registrar(self, ctx, monto_emisor: float, tasa: str):
        # Asumiendo que 'p' representa la tasa publicada
        if tasa.lower() == 'p':
            tasa_publicada = 9  # Este valor podría variar
            monto_receptor = monto_emisor * tasa_publicada
            transaccion = Transaccion(
                emisor=ctx.author,
                monto_emisor=monto_emisor,
                tasa=tasa_publicada,
                monto_receptor=monto_receptor,
                timestamp=datetime.datetime.now()
            )
            self.transacciones_pendientes[transaccion.custom_id] = transaccion  # Registrar la transacción pendiente}
            
            # Crear el embed para la transacción
            embed = discord.Embed(title="Solicitud de Transacción", description="Una nueva transacción ha sido registrada y está pendiente de aprobación.", color=discord.Color.blue())
            embed.add_field(name="Emisor", value=ctx.author.mention, inline=False)
            embed.add_field(name="Monto Emisor", value=f"{monto_emisor}", inline=True)
            embed.add_field(name="Tasa", value=f"{tasa_publicada}", inline=True)
            embed.add_field(name="Monto Receptor", value=f"{monto_receptor}", inline=True)
            embed.set_footer(text=f"Timestamp: {transaccion.timestamp}")

            view = TransaccionView(custom_id=transaccion.custom_id)
            # Enviar el embed al canal de solicitudes
            canal_solicitudes_id = 1204855842038616154  # Reemplaza esto con el ID real de tu canal de solicitudes
            canal_solicitudes = self.bot.get_channel(canal_solicitudes_id)
            if canal_solicitudes:
                await canal_solicitudes.send(embed=embed, view=view)

            # Enviar el embed al DM del cajero (debes tener el ID del cajero)
            cajero_id = 1176991779208319016  # Reemplaza esto con el ID real del cajero
            cajero = await self.bot.fetch_user(cajero_id)
            if cajero:
                await cajero.send(embed=embed, view=view)

            await ctx.respond("Transacción registrada y enviada para aprobación.", ephemeral=True)
            self.batch_actual.agregar_transaccion(transaccion)


def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(SistemaTransacciones(bot)) # add the cog to the bot
