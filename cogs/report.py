import discord
from discord.ext import commands
from discord.utils import get

class Report(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('cogs report loaded.')

    @commands.command()
    @commands.has_any_role(481671645808033809)
    async def report(self, ctx, *, message):
        await ctx.send(discord.Object(id='495597599508922378'), "{}".format(message))
    
def setup(client):
    client.add_cog(Report(client))