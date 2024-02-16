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

async def autocomplete_moneda(ctx: discord.AutocompleteContext):
    monedas = []
    async with aiosqlite.connect('main.db') as db:
        async with db.execute("SELECT DISTINCT Moneda FROM Paises") as cursor:
            async for row in cursor:
                monedas.append(row[0])
    return [moneda for moneda in monedas if ctx.value.lower() in moneda.lower()]

async def autocomplete_paises(ctx: discord.AutocompleteContext):
    paises = []
    async with aiosqlite.connect('main.db') as db:
        async with db.execute("SELECT DISTINCT Nombre FROM Paises") as cursor:
            async for row in cursor:
                paises.append(row[0])
    return [paise for paise in paises if ctx.value.lower() in paise.lower()]


async def autocomplete_usuarios(ctx: discord.AutocompleteContext):
    usuarios = []
    async with aiosqlite.connect('main.db') as db:
        async with db.execute("SELECT DISTINCT Username FROM UserRoles") as cursor:
            async for row in cursor:
                usuarios.append(row[0])
    return [usuario for usuario in usuarios if ctx.value.lower() in usuario.lower()]

class CuentasCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="cuent",  description="Cierra un batch de transacciones.")
    @commands.has_role(1205983428001013770)  # O el ID del rol si no es un nombre
    
    async def registrar_cuenta(self, ctx, pais: Option(str, "Elige un país", autocomplete=basic_autocomplete(autocomplete_paises)), moneda: Option(str, "Elige una moneda", autocomplete=basic_autocomplete(autocomplete_moneda)), usuario: Option(str, "Elige un usuario", autocomplete=basic_autocomplete(autocomplete_usuarios)), nombre_cuenta: str, valor_inicial: float): #type: ignore
        current_timestamp = datetime.datetime.now().isoformat()
        # Prepara los datos a insertar
        datos_cuenta = (
        pais,  # País seleccionado
        moneda,  # Moneda seleccionada
        usuario, #usuario seleccionado
        nombre_cuenta,  # Nombre de la cuenta
        valor_inicial,  # Valor actual es el mismo al crear la cuenta
        current_timestamp  # Timestamp de registro 
        )

        async with aiosqlite.connect('main.db') as db:
            await db.execute('''
                INSERT INTO Cuentas (Country, Moneda, Usuario, NombreCuenta, ValorActual, TimestampRegistro)
                VALUES (?, ?, ?, ?, ?, ?)
        ''', datos_cuenta)
            await db.commit()

    # Envía una confirmación al usuario
        await ctx.respond(f"Cuenta {nombre_cuenta} registrada con éxito.") 


# Función para añadir el cog al bot

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(CuentasCog(bot)) # add the cog to the bot
