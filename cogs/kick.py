import discord
from discord.ext import commands
#some of the strings are in my native language
class KickUser(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('cogs kick loaded.')

    @commands.command()
    @commands.has_any_role("")#Put the name any role on the string, 
    async def kick(ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'**{member}** telah di **kick** karena **{reason}**')

def setup(client):
    client.add_cog(KickUser(client))