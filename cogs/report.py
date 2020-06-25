import discord
from discord.ext import commands
from discord.utils import get
#some of the strings are in my native language
class Report(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('cogs report loaded.')

    @commands.command()
    async def report(self, ctx, member: discord.Member, *, arg):
        channel = self.client.get_channel(495597599508922378)
        author = ctx.message.author
        await ctx.send(f'**{member}** sudah dilaporkan.')
        await channel.send(f'**{member}** dilaporkan karena **{arg}** oleh **{author}**')

    @commands.command()
    @commands.has_any_role(481671645808033809)
    async def warn(self, ctx, member: discord.Member, *, arg):
        channel = self.client.get_channel(495597599508922378)
        await ctx.send(f'**{member}** diberikan **peringatan** karena **{arg}**')
        await channel.send(f'**{member}** diberikan **peringatan** karena **{arg}**')


def setup(client):
    client.add_cog(Report(client))