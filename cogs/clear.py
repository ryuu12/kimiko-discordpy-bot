#
# Clear Cogs.
# Command for clearing messages.
#

import discord
from discord.ext import commands

class Clear(commands.Cog):

    # Every function that started with this constructor:
    # @commands.command()
    # @commands.has_any_role("role name")
    # Would only be used by the specific mentioned role.
    
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('cogs clear loaded.')

    # Clear command
    @commands.command()
    @commands.has_any_role('')
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount)

def setup(client):
    client.add_cog(Clear(client))