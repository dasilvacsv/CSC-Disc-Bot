import discord
from discord.ext import commands
from discord.ui import Button, View
import datetime
import aiosqlite
import asyncio
#Definicion de intents para Prefixed Commands
intents = discord.Intents.all()

class ApproveButton(Button): # Approve button logic
    def __init__(self, user, role_id, role_name, timestamp_registered, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.role_id = role_id
        self.role_name = role_name
        self.timestamp_registered = timestamp_registered


    async def callback(self, interaction: discord.Interaction):
        # Assign the role to the user
        role = interaction.guild.get_role(int(self.role_id))
        current_timestamp = datetime.datetime.now().isoformat()  # Format the current timestamp
        await interaction.response.defer() 

        # Retrieve the "Pending" role by its ID and remove it if the user has it
        pending_role_id = "1207037302379909190"  # Replace with your actual "Pending" role ID
        pending_role = interaction.guild.get_role(int(pending_role_id))
        if pending_role in self.user.roles:
            await self.user.remove_roles(pending_role)

        if role:
            await self.user.add_roles(role)
            # Db operation, insert or update role record
            async with aiosqlite.connect('main.db') as db:
                await db.execute(
                '''INSERT INTO UserRoles (UserID, Username, RoleID, RoleName, TimestampRegistered, TimestampApproved) 
                   VALUES (?, ?, ?, ?, ?, ?) 
                   ON CONFLICT(UserID) DO UPDATE SET 
                       TimestampApproved=?,
                       RoleName=?,
                       RoleID=?''',
                 (str(self.user.id), self.user.name, str(self.role_id), self.role_name, self.timestamp_registered, current_timestamp, current_timestamp, self.role_name, str(self.role_id))
            )            
                await db.commit()
            # Desactivar todos los botones en la vista
            for item in self.view.children:
                if isinstance(item, Button):
                    item.disabled = True
            await interaction.edit_original_response(view=self.view)
            await interaction.followup.send(f"Role {role.name} assigned to {self.user.mention}", ephemeral=True)
        else:
            await interaction.response.send_message("Role not found.", ephemeral=True)

class RejectButton(Button):
    def __init__(self, user, role_id, role_name, timestamp_registered, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.role_id = role_id
        self.role_name = role_name
        self.timestamp_registered = timestamp_registered

    async def callback(self, interaction: discord.Interaction):
        # Format the current timestamp
        current_timestamp = datetime.datetime.now().isoformat()
        await interaction.response.defer() 

        # Record the rejection in the database
        async with aiosqlite.connect('main.db') as db:
            await db.execute(
                '''INSERT INTO UserRoles (UserID, Username, RoleID, RoleName, TimestampRegistered, TimestampRejected) 
                   VALUES (?, ?, ?, ?, ?, ?) 
                   ON CONFLICT(UserID) DO UPDATE SET 
                       TimestampRejected=?,
                       RoleName=?,
                       RoleID=?''',
                 (str(self.user.id), self.user.name, str(self.role_id), self.role_name, self.timestamp_registered, current_timestamp, current_timestamp, self.role_name, str(self.role_id))
            )            
            await db.commit()
            # Desactivar todos los botones en la vista
        for item in self.view.children:
            if isinstance(item, Button):
                item.disabled = True
        await interaction.edit_original_response(view=self.view)
        # Send a rejection message to the user
        await interaction.followup.send(f"{self.user.mention}, your request for the '{self.role_name}' role was rejected.", ephemeral=True)

class RoleSelectionView(View): # maneja la desactivación de los botones
    def disable_all_buttons(self):
        for item in self.children:
            if isinstance(item, Button):
                item.disabled = True

class CustomButton(Button): #Button Class
    def __init__(self, role_name, role_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.role_name = role_name
        self.role_id = role_id

    async def callback(self, interaction: discord.Interaction):
        # Use the interaction object to get the bot instance
        bot = interaction.client
        for item in self.view.children:  # maneja la desactivación de los botones
            if isinstance(item, Button):    # maneja la desactivación de los botones
                item.disabled = True    # maneja la desactivación de los botones
        await interaction.response.edit_message(view=self.view)

        await asyncio.sleep(3)

        for item in self.view.children:
            if isinstance(item, Button):
                item.disabled = False
        await interaction.edit_original_response(view=self.view)
        
          # Retrieve the "Pending" role by its ID
        pending_role_id = "1207037302379909190"  # Replace with your actual "Pending" role ID
        pending_role = interaction.guild.get_role(int(pending_role_id))

        # Remove current roles if the user has them
        roles_to_remove_ids = ["1207029718927544400"]  # Role IDs for "Cliente", "Cajero", "Asociado"
        for role_id in roles_to_remove_ids:
            role = interaction.guild.get_role(int(role_id))
            if role in interaction.user.roles:
                await interaction.user.remove_roles(role)

        # Assign the "Pending" role to the user
        if pending_role:
            await interaction.user.add_roles(pending_role)
        else:
            await interaction.followup.send("Pending role not found. Please contact an administrator.", ephemeral=True)
        # Now, to send a message to another channel, get the channel by its ID
        apro_channel_id = 1207036034412445766 # Replace with your actual request channel ID
        apro_channel = bot.get_channel(apro_channel_id)
        if apro_channel:
            await apro_channel.send(f"Your request has been sent for approval, {interaction.user.mention}")

        # Prepare the embed to be sent to the request channel
        embed = discord.Embed(title="Registration Request", description=f"{interaction.user.mention} requested the '{self.role_name}' role.")
        embed.add_field(name="User ID", value=str(interaction.user.id))
        embed.add_field(name="Role", value=self.role_name)
        embed.add_field(name="Timestamp", value=datetime.datetime.now().isoformat())
        timestamp_registered = datetime.datetime.now().isoformat()

        # Create the view with Approve and Reject buttons classes
        view = View()
        view.add_item(ApproveButton(label="Aprobar", style=discord.ButtonStyle.success, user=interaction.user, role_id=self.role_id, role_name=self.role_name, timestamp_registered=timestamp_registered))
        view.add_item(RejectButton(label="Rechazar", style=discord.ButtonStyle.danger, user=interaction.user, role_id=self.role_id, role_name=self.role_name, timestamp_registered=timestamp_registered))

        request_channel_id = 1207048176272416849  # Replace with your actual request channel ID
        request_channel = bot.get_channel(request_channel_id)
        if request_channel:
            await request_channel.send(embed=embed, view=view)
        
class RegistroUsuarios(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        canal = self.bot.get_channel(1207030045936197652)
        embed = discord.Embed(title="Registro de Usuarios", description="Selecciona tu rol:")
        view = RoleSelectionView() # Maneja la desactivación de los botones

        # Define roles and create custom buttons
        roles = [("Cliente", "1206777791656239155"), ("Cajero", "1205982581418500176"), ("Asociado", "1205982695058841601")]
        for nombre, id in roles:
            button = CustomButton(role_name=nombre, role_id=id, label=nombre, style=discord.ButtonStyle.primary, custom_id=id)
            view.add_item(button)

        await canal.send(embed=embed, view=view)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(RegistroUsuarios(bot)) # add the cog to the bot
