#
# Help Cogs
# Command for showing list of available commands.
#

import discord
from discord.ext import commands

class Help(commands.Cog):

    # Every function that started with this constructor:
    # @commands.command()
    # @commands.has_any_role("role name")
    # Would only be used by the specific mentioned role.

    def __int__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('cogs help loaded')

    #Help Command
    @commands.command()
    async def help(self, ctx):
        author = ctx.message.author

        embed = discord.Embed(
            colour = discord.Color.red()
        )

        #Showing list of command using embedded message.
        embed.set_author(name='Help')
        embed.add_field(name='>ping', value='Cek ping.', inline=False)
        embed.add_field(name='>help', value='Melihat daftar perintah.', inline=False)
        embed.add_field(name='>nasib', value='Menanyakan nasib.', inline=False)
        embed.add_field(name='>lotre', value='Mengundi nomor lotre', inline=False)
        embed.add_field(name='>role', value='Menambahkan role', inline=False)
        embed.add_field(name='>report', value='Melaporkan anggota yang melanggar peraturan (Hanya boleh digunakan di channel #staff-support).')
        embed.set_footer(text="For more detailed help, use >help(name of command)")

        await ctx.send(author, embed=embed)

    ### This are commands to show more detailed information about each commands ###
    @commands.command()
    async def helpping(self, ctx):
        await ctx.send('```>ping: \nMemeriksa ping anda.```')

    @commands.command()
    async def helpnasib(self, ctx):
        await ctx.send('```>nasib:\nMelihat nasib anda. Pertanyaan harus berupa Ya/Tidak.\nContoh: >nasib Apakah saya hari ini bisa makan?```')

    @commands.command()
    async def helplotre(self, ctx):
        await ctx.send('```>lotre:\nMengundi nomor lotre anda. Bila nomor lotre anda sesuai dengan nomor lotre hari ini  (hanya admin yang bisa menggunakan perintah untuk memeriksa lotre hari ini), maka selamat.```')

    @commands.command()
    async def helpreport(self, ctx):
        await ctx.send('```>report:\nMelaporkan anggota yang melanggar peraturan server. Perintah ini hanya boleh digunakan di channel #staff-support.\nContoh: >report {user} {alasan} ```')

    @commands.command()
    @commands.has_any_role("")#Put the name of the role on the string
    async def helpadmin(self, ctx):
        await ctx.send('```Daftar Perintah Khusus Admin. \n >ban\n  Perintah untuk melakukan ban terhadap member tertentu.\n  contoh: >ban {user} {alasan} \n >kick\n  Perintah untuk melakukan kick terhadap member tertentu.\n  contoh: >kick {user} {alasan}\n >ceklotre\n  Untuk memerika nomor lotre hari ini.\n >clear\n  Untuk menghapus pesan di dalam channel.\n  contoh: >clear {jumlah pesan yang akan dihapus}\n >warn\n  Untuk memberikan peringatan kepada anggota tertentu.\n  Contoh: >warn {user} {alasan} ```')

    @commands.command()
    @commands.has_any_role("")#Put the name of the role on the string
    async def devtools(self, ctx):
        await ctx.send('```Developer Tools\n >load:\n  Load a cogs to the bot.\n  Example: >load {extension}\n >unload:\n  Unload a cogs from the bot.\n  Example: >unload {extension}\nList of Cogs\n ban\n  ban\n  unban\n kick\n  kick\n ping\n  ping\n nasib\n  nasib\n  lotre\n  ceklotre\n report\n  report\n  warn\n help\n  help\n  helpping\n  helpnasib\n  helplotre\n  helpreport\n  helpadmin\n  devtools   ```')

def setup(client):
    client.add_cog(Help(client))
