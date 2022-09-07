from disnake.ext import commands
import disnake


class Info(commands.Cog):
    """Info commands"""

    def __init__(self, bot: commands.Bot):
        """constructor for the Info cog"""
        self.bot = bot

    @commands.slash_command(name="info", description="Get info about the bot")
    async def info(self, inter: disnake.ApplicationCommandInteraction):
        """info command group"""
        pass

    @info.sub_command(name="ping", description="Get the bot's ping")
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        """Ping command

        Args:
            inter (disnake.ApplicationCommandInteraction): The interaction
        """
        emb = disnake.Embed(
            title="Ping", description="The ping for the bot", color=0x00FF00
        )
        emb.add_field(name="Ping", value=f"{round(self.bot.latency * 1000)}ms")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        return await inter.send(embed=emb)

    @info.sub_command(name="invite", description="Get the bot's invite link")
    async def invite(self, inter: disnake.ApplicationCommandInteraction):
        """Invite command

        Args:
            inter (disnake.ApplicationCommandInteraction): The interaction
        """
        emb = disnake.Embed(
            title="Invite", description="The invite link for the bot", color=0x00FF00
        )
        inv_link = f"https://discord.com/api/oauth2/authorize?client_id={self.bot.user.id}&permissions=415068712001&scope=bot%20applications.commands"
        emb.add_field(name="Invite Link", value=f"[Click Here]({inv_link})")
        emb.set_footer(text="Clicking on the link will open a discord modal.")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        return await inter.send(embed=emb)

    @info.sub_command(name="about", description="Get info about the bot")
    async def about(self, inter: disnake.ApplicationCommandInteraction):
        """About command

        Args:
            inter (disnake.ApplicationCommandInteraction): The interaction
        """
        emb = disnake.Embed(title="About the Bot", color=0x00FF00)
        emb.add_field(name="Name", value=self.bot.user.name)
        emb.add_field(name="ID", value=self.bot.user.id)
        emb.add_field(name="Owner", value=f"{self.bot.owner.name}")
        emb.add_field(
            name="Github Link",
            value="[Click Here](https://github.com/vachanmn123/IvyBot-2.0-py)",
        )
        emb.add_field(
            name="Developer", value="[vachanmn123](https://vachanmn.is-a.dev)"
        )
        return await inter.send(embed=emb)


def setup(bot: commands.Bot):
    """setup function for the Info cog

    Args:
        bot (commands.Bot): The bot instance

    Returns:
        commands.Bot: The bot instance
    """
    bot.add_cog(Info(bot))
    bot.logger.info("Loaded Info cog")
    return bot
