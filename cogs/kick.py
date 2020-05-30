import discord
from discord.ext import commands

class KickUser(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('cogs kick loaded.')

    @commands.command()
    @commands.has_any_role('Admins')
    async def kick(ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

def setup(client):
    client.add_cog(KickUser(client))