#
# Report Cogs
# Command to report a user an then send the report to a specific channel.
#
# This cogs is not only for report command, but also for warning user.
#

import discord
from discord.ext import commands
from discord.utils import get

class Report(commands.Cog):

    # Every function that started with this constructor:
    # @commands.command()
    # @commands.has_any_role("role name")
    # would only be used by the specific mentioned role.
    #
    # This is for the specific channel where warns and reposrt would be sent to.
    # channel = self.client.get_channel("channel id")
    #
    # This will be the message that were going to be sent to the specific mentioned channel.    
    # await channel.send("Put the message here")

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('cogs report loaded.')

    # Report command
    @commands.command()
    async def report(self, ctx, member: discord.Member, *, arg):

        channel = self.client.get_channel("")

        author = ctx.message.author

        # You can add your own report message.
        # await ctx.send("your message")

        await ctx.send(f'**{member}** reported.')    

        await channel.send(f'**{member}** reported for **{arg}** by **{author}**')

    # Warn command
    @commands.command()
    @commands.has_any_role("")
    async def warn(self, ctx, member: discord.Member, *, arg):

        channel = self.client.get_channel("")

        await ctx.send(f'**{member}** have been **warned** for **{arg}**')

        await channel.send(f'**{member}** **warned** for **{arg}**')


def setup(client):
    client.add_cog(Report(client))