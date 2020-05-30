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
    async def report(self, ctx):
        channel = client.get_channel(549717043671334913)
        await ctx.channel.send('hello')

def setup(client):
    client.add_cog(Report(client))