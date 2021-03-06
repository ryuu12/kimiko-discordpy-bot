import discord
from discord.ext import commands
#some of the strings are in my native language
class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('cogs clear loaded.')

    @commands.command()
    @commands.has_any_role('')#Put any role on the string
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount)

def setup(client):
    client.add_cog(Clear(client))