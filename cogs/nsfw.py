from socket import SO_PRIORITY
from urllib import request
from disnake.ext import commands
from functions.NSFWFunc import getRealBooru, get_realbooru_tags
import disnake
import requests

realbooru_tags = get_realbooru_tags()


class NSFW(commands.Cog):
    """The nsfw command group"""

    def __init__(self, bot):
        """constructor for the NSFW class

        Args:
            bot (disnake.ext.commands.Bot): The bot instance
        """
        self.bot = bot
        self.logger = bot.logger

    async def realbooru_autcomplete_tags(
        inter: disnake.ApplicationCommandInteraction, user_input: str
    ):
        """autocomplete realbooru tags

        Args:
            inter (disnake.ApplicationCommandInteraction): the interaction object
            user_input (str): the user's input while they type

        Returns:
            list: list of autocomplete options
        """
        # Check the user input against all joke tags
        tags = [tag for tag in realbooru_tags if user_input.lower() in tag]
        return tags[:25]

    @commands.slash_command(name="nsfw", description="The nsfw command group")
    async def nsfw(self, inter: disnake.ApplicationCommandInteraction):
        """The NSFW command group

        Args:
            inter (disnake.ApplicationCommandInteraction): The Interaction object
        """
        pass

    @nsfw.sub_command(name="realbooru", description="Searches realbooru")
    async def realbooru(
        self,
        ctx: disnake.ApplicationCommandInteraction,
        tag: str = commands.param(
            name="tag",
            description="The tag to search for",
            autocomplete=realbooru_autcomplete_tags,
        ),
    ):
        """Searches realbooru

        Args:
            ctx (disnake.ApplicationCommandInteraction): interaction object
            tag (str): tag to search for
        """
        if not ctx.channel.nsfw:
            # if the channel is not nsfw, return
            return await ctx.send("This command can only be used in NSFW channels")
        # get a post
        resp = getRealBooru(tag)
        if resp is None:
            # if the response is none, return
            return await ctx.send("No results found")
        emb = disnake.Embed(title="Realbooru", color=0x00FF00, description=resp["tags"])
        # make the link
        link = f"https://realbooru.com//images/{resp['directory']}/{resp['image']}"
        # Update the database with usage stats
        self.bot.db.commands.update_one(
            {"category": "nsfw", "command": "realbooru"}, {"$inc": {"uses": 1}}
        )
        # First send the embed, then send the image link so it is shown
        await ctx.send(embed=emb)
        await ctx.channel.send(link)


def setup(bot):
    """The setup function for the cog

    Args:
        bot (disnake.ext.commands.Bot): The bot instance

    Returns:
        disnake.ext.commands.Bot: The bot instance
    """
    bot.add_cog(NSFW(bot))
    bot.logger.info("NSFW cog loaded")
    return bot
