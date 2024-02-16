import discord
import os
import dotenv
import aiosqlite
#For prefixed commands
from discord.ext import commands

#Definicion de intents para Prefixed Commands
intents = discord.Intents.all()

# Carga variables de entorno isoladas
dotenv.load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = discord.Bot()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event #Set a listener
async def on_ready(): #async def to start a corroutine
    print(f'Logged in as {bot.user.name}')

# Assign user role as stepped into server
# @bot.event  # Correctly use the @bot.event decorator
# async def on_member_join(member):  # Remove the 'self' parameter
#    user_role_id = 1207029718927544400  # Replace this with your actual "User" role ID
#     user_role = discord.utils.get(member.guild.roles, id=user_role_id)
#    if user_role:
#        await member.add_roles(user_role)

#Calling cogs to work with modules
cogs_list = [
    'cuentas',
    'transacciones',
    'usuarios'
]

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')


bot.run(token)