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
    async def report(self, ctx, member: discord.Member, *, arg):
        channel = self.client.get_channel(495597599508922378)
        await channel.send(f'@{member} reported for {arg}')

def setup(client):
    client.add_cog(Report(client))