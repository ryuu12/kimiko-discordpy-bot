import discord
from discord.ext import commands
#some of the strings are in my native language
class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('cogs ping loaded.')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong  {round(self.client.latency * 1000)}ms')

def setup(client):
    client.add_cog(Ping(client))