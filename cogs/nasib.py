import discord
from discord.ext import commands
import random
#some of the strings are in my native language
#nasib means like your destiny, thi is more into like 8ball command
class Nasib(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('cogs nasib loaded')

    @commands.command()
    async def nasib(self, ctx, *, question):
        jawaban = ['Iya',
                   'Sudah pasti',
                   'Tentu saja',
                   'Sudah pasti',
                   'Ya iyalah',
                   'Tidak mungkin',
                   'Mustahil',
                   'Ngaco, ya kagak lah',
                   'Tidak',
                   'Gak akan pernah',
                   'Bisa jadi',
                   'Mungkin saja',
                   'Kayaknya',
                   'Gak tau juga',
                   'Coba tanya lagi']

        await ctx.send(f'{random.choice(jawaban)}')

    #For lottery
    @commands.command()
    async def lotre(self, ctx):
        await ctx.send(f'Nomor lotre {ctx.message.author} adalah ```{random.randint(1, 999999999)}```')

    #To see today's lottery number
    @commands.command()
    @commands.has_any_role("")
    async def ceklotre(self, ctx):
        await ctx.send(f'Nomor lotre hari ini adalah ```{random.randint(1, 999999999)}```')

def setup(client):
    client.add_cog(Nasib(client))
