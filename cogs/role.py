import discord
from discord.ext import commands

class Role(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='role')
    async def _role(self, ctx, role: discord.Role):
        if role in ctx.author.roles:
            await ctx.author.remove_roles(role)
        else:
            await ctx.author.add_roles(role)

def setup(client):
    client.add_cog(Role(client))
    
