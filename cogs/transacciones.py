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
# Transaction and Batch handling

class TransaccionesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Comando para iniciar un batch
    @slash_command(name="iniciar_bh", description="Inicia un nuevo batch de transacciones.")
    async def iniciar_bh(self, ctx):
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
    @slash_command(name="cerrar_batch", description="Cierra un batch de transacciones.")
    async def cerrar_batch(self, ctx, batch_id: Option(str, "ID del batch a cerrar", autocomplete=basic_autocomplete(autocomplete_batch_ids))):
        async with aiosqlite.connect('main.db') as db:
            await db.execute("UPDATE Batches SET Status = 'Closed', EndTime = ? WHERE BatchID = ? AND UserID = ?", (datetime.datetime.now().isoformat(), batch_id, str(ctx.interaction.user.id)))
            await db.commit()

        await ctx.respond(f"Batch {batch_id} cerrado correctamente.")
        

# Función para añadir el cog al bot

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(TransaccionesCog(bot)) # add the cog to the bot
