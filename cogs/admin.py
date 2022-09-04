from asyncio.log import logger
import disnake
from disnake.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = bot.logger

    @commands.slash_command(name="admin")
    @commands.default_member_permissions(administrator=True)
    async def admin(self, inter):
        pass

    @admin.sub_command(name="reload", description="Reloads a cog")
    async def reload(self, ctx, extension: str):
        """Reloads an extension"""
        try:
            self.bot.logger.info(f"Reloading {extension}")
            self.bot.unload_extension(f"cogs.{extension}")
            self.bot.load_extension(f"cogs.{extension}")
            await ctx.send(f"Reloaded {extension}")
        except Exception as e:
            await ctx.send(f"Error: {e}")


def setup(bot):
    """Loads the cog"""
    bot.add_cog(Admin(bot))
    bot.logger.info("Admin cog loaded")
    return bot
