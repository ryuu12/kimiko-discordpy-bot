#
# Nasib Cogs
# Command for playing a 'nasib' game.
#
# Nasib means 'destiny' in Indonesian.
# This is a fun command to answer a question with a positive, neutral, or negative responses. Remember to ask a yes/no question.
# Not only a yes/no question, but you can also play a little lottery (without any prizes tho).
#

import discord
from discord.ext import commands
import random

class Nasib(commands.Cog):

    # Every function that started with this constructor:
    # @commands.command()
    # @commands.has_any_role("role name")
    # Would only be used by the specific mentioned role.

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('cogs nasib loaded')

    # Nasib command.
    # The name of the command is in Indonesian.
    @commands.command()
    async def nasib(self, ctx, *, question):
        # List of possible answer.
        answer = ['Yes',
                   'For sure',
                   'Surely',
                   'It must be',
                   'Hell yeah',
                   'Nah',
                   'Impossible',
                   'No',
                   'Nope',
                   'Never',
                   'Maybe',
                   'Possible',
                   'Not impossible',
                   'Dunno',
                   'Please ask again']

        await ctx.send(f'{random.choice(answer)}')

    # Lottery command
    @commands.command()
    async def lotre(self, ctx):
        await ctx.send(f'Nomor lotre {ctx.message.author} adalah ```{random.randint(1, 999999999)}```')

    # To see "today's" lottery number
    @commands.command()
    @commands.has_any_role("")
    async def ceklotre(self, ctx):
        await ctx.send(f'Nomor lotre hari ini adalah ```{random.randint(1, 999999999)}```')

def setup(client):
    client.add_cog(Nasib(client))
