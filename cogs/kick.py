#
# Kick Cogs
# Command for kicking user from the server.
#

import discord
from discord.ext import commands

class KickUser(commands.Cog):

    # Every function that started with this constructor:
    # @commands.command()
    # @commands.has_any_role("role name")
    # Would only be used by the specific mentioned role.

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('cogs kick loaded.')

    @commands.command()
    @commands.has_any_role("")
    async def kick(ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'**{member}** have been **kicked** for **{reason}**')
        # You can create your own kick message like this:
        # await ctx.send("put your kick message here.")

def setup(client):
    client.add_cog(KickUser(client))