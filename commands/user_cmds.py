import discord
from discord.ext import commands
from config import bot_color, user_icon

# These commands are in the user popout menu


class user_cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # View user avatars
    @discord.user_command(name="View profile picture")
    async def useravatar(self, ctx, member: discord.Member):
        embed = discord.Embed(color=bot_color)
        embed.set_author(name=f"{member.name}'s profile", icon_url=user_icon)
        
        if member.guild_avatar != None: # if member has a guild avatar
            embed.set_image(url=member.guild_avatar)
            embed.set_thumbnail(url=member.avatar)
        else:
            embed.set_image(url=member.avatar)
            embed.set_footer(text=f"{member.name} doesn't have a guild pfp yet")

        await ctx.respond(embed=embed, ephemeral=True)


    # View user banner
    @discord.user_command(name="View banner")
    async def userbanner(self, ctx, member: discord.Member):
        embed = discord.Embed(color=bot_color)
        embed.set_author(name=f"{member.name}'s profile", icon_url=user_icon)
        embed.set_thumbnail(url=member.avatar)

        if member.banner != None:
            embed.set_image(url=member.banner)
        else:
            embed.set_footer(text=f"{member.name} doesn't have a banner yet")

        await ctx.respond(embed=embed, ephemeral=True)
        


    # User perms command
    @discord.user_command(name="View permissions")
    async def userperms(self, ctx, member: discord.Member):
        perms = ', '.join([str(perm[0]).upper() for perm in member.guild_permissions if perm[1]])
        embed = discord.Embed(color=bot_color, description=f"**{member.name}'s permissions**\n```{perms}```")
        embed.set_author(name="User permissions", icon_url=user_icon)
        embed.set_footer(text=f"User ID: {member.id}")
        await ctx.respond(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(user_cmds(bot))