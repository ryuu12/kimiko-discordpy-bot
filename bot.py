import discord
import os
import json
from discord.ext import commands, tasks
from itertools import cycle
#some of the strings are in my native language
client = commands.Bot(command_prefix='>')
client.remove_command('help')
status = cycle(['Status 1', 'Status 2', 'Status 3'])

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Command invalid.')

@client.event
async def on_ready():
     change_status.start()
     print('Bot siap')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
       client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_member_join(member):
    with open('money.json', 'r') as f:
        users = json.load(f)

    await update_data(users, member)

    with open('money.json', 'w') as f:
        json.dump(users, f)

@client.event
async def on_message(message):
    if message.author.bot == False:
        with open('users.json', 'r') as f:
            users = json.load(f)

        await update_data(users, message.author)
        await add_experience(users, message.author, 5)
        await level_up(users, message.author, message)

        with open('users.json', 'w') as f:
            json.dump(users, f)

        await client.process_commands(message)

async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1


async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += exp


async def level_up(users, user, message):
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1 / 4))
    if lvl_start < lvl_end:
        await message.channel.send(f'{user.mention} sudah naik ke level {lvl_end}')
        users[f'{user.id}']['level'] = lvl_end

@client.command()
@commands.has_any_role(507440134774587415)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} loaded')

@client.command()
@commands.has_any_role(507440134774587415)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} unloaded')

client.run('')