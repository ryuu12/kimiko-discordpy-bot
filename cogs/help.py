import discord
from discord.ext import commands

class Help(commands.Cog):
    def __int__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('cogs help loaded')

    @commands.command(pass_context=True)
    async def help(self, ctx):
        author = ctx.message.author

        embed = discord.Embed(
            colour = discord.Color.red()
        )

        embed.set_author(name='Help')
        embed.add_field(name='>ping', value='Check the ping.', inline=False)
        #embed.add_field(name='>help', value='List of commands', inline=False)

        await ctx.send(author, embed=embed)

def setup(client):
    client.add_cog(Help(client))