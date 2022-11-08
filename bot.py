#
# Kimiko Discord Bot 
# Made using DIscord.py
#
# Created for Kinokura Discord Server.
# To use the template, please remove the "Kinnokura" branding.
#

import discord
import os
import json
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix='>')
# Removing the default help command (from Discord.py).
client.remove_command('help')
# Cycled Discord status.
status = cycle(['Status 1', 'Status 2', 'Status 3'])

#For catching errors
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Command invalid.')

@client.event
async def on_ready():
     change_status.start()
     print('Bot ready')

#Looping the status
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
       client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
@commands.has_any_role("")#The role that has permission to load and unload the cogs
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} loaded')

@client.command()
@commands.has_any_role("")#Same as above
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} unloaded')

#Put your bot token here
client.run('')