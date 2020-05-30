import discord
from discord.ext import commands

class BanUser(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('cogs ban loaded.')

    @commands.command()
    @commands.has_any_role('Admins')
    async def ban(ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)

    @commands.command()
    @commands.has_any_role('Admins')
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