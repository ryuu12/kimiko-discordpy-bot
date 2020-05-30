import discord
from discord.ext import commands
import random

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
                   'Sudah mutlak',
                   'Tidak mungkin',
                   'Mustahil',
                   'Ngaco, ya kagak lah',
                   'Tidak',
                   'g',
                   'Bisa jadi'
                   'Mungkin saja',
                   'Kayaknya',
                   'Gak tau juga']

        await ctx.send(f'{random.choice(jawaban)}')

def setup(client):
    client.add_cog(Nasib(client))