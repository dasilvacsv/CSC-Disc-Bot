import nextcord
from nextcord.ext import commands
# Mapeo de sistema para encontrar carpetas raíces
import os
from dotenv import load_dotenv

# Carga variables de entorno isoladas
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# Configuración de los intents del bot, necesaria
intents = nextcord.Intents.default()
intents = nextcord.Intents().all()
# Instanciar el bot con los intents para ser llamado
bot = commands.Bot(command_prefix='!', intents=intents)

# Task 3 un comando que interactúe con el usuario
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Task 4 Crear un evento que confirma que el bot está listo para empezar
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    
#Llamar al token isolado a través de .env
bot.run(token)