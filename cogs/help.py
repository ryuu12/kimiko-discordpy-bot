import discord
from discord.ext import commands

class Help(commands.Cog):
    def __int__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('cogs help loaded')

    @commands.command()
    async def help(self, ctx):
        author = ctx.message.author

        embed = discord.Embed(
            colour = discord.Color.red()
        )

        embed.set_author(name='Help')
        embed.add_field(name='>ping', value='Cek ping.', inline=False)
        embed.add_field(name='>help', value='Melihat daftar perintah.', inline=False)
        embed.add_field(name='>nasib', value='Menanyakan nasib.', inline=False)
        embed.add_field(name='>lotre', value='Mengundi nomor lotre', inline=False)
        embed.set_footer(text="For more detailed help, use >help(name of command)")

        await ctx.send(author, embed=embed)



def setup(client):
    client.add_cog(Help(client))