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

    @commands.command()
    async def helpping(self, ctx):
        await ctx.send('```>ping: \nMemeriksa ping anda.```')

    @commands.command()
    async def helpnasib(self, ctx):
        await ctx.send('```>nasib:\nMelihat nasib anda. Pertanyaan harus berupa Ya/Tidak.\nContoh: >nasib Apakah saya hari ini bisa makan?```')

    @commands.command()
    async def helplotre(self, ctx):
        await ctx.send('```>lotre:\nMengundi nomor lotre anda. Bila nomor lotre anda sesuai dengan nomor lotre hari ini  (hanya admin yang bisa menggunakan perintah untuk memeriksa lotre hari ini), maka selamat.```')


def setup(client):
    client.add_cog(Help(client))