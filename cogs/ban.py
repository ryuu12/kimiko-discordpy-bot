#
# Ban Cogs.
# Command for banning user from server.
#

import discord
from discord.ext import commands

class BanUser(commands.Cog):

    # Every function that started with this constructor:
    # @commands.command()
    # @commands.has_any_role("role name")
    # Would only be used by the specific mentioned role.

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('cogs ban loaded.')

    #Ban command
    @commands.command()
    @commands.has_any_role("")
    async def ban(ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'**{member}** have been **banned** for **{reason}**')
        # You can create your own ban message like this:
        # await ctx.send("put your ban message here.")

    #Unban command
    @commands.command()
    @commands.has_any_role("")
    async def unban(ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                return

def setup(client):
    client.add_cog(BanUser(client))