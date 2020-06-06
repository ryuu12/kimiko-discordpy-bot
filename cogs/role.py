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

    @commands.command()
    @commands.has_any_role(481671645808033809)
    async def listrole(self, ctx):
        author = ctx.message.author

        embed = discord.Embed(
            colour = discord.Color.red()
        )

        embed.set_author(name='List of role')
        embed.add_field(name='Color Role', value='@Green @Orange @Yellow @Pink @Red @Violet @Blue @Grey', inline=False)

        await ctx.send(author, embed=embed)

def setup(client):
    client.add_cog(Clear(client))
    
