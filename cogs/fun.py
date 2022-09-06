from disnake.ext import commands
import disnake
from functions.RandomStuffApiFunc import (
    get_random_joke,
    get_all_joke_tags,
    get_tag_joke,
    get_random_meme,
)
from datetime import datetime

# Make a list of all the joke tags when the bot starts.
all_joke_tags = get_all_joke_tags()


class Fun(commands.Cog):
    """Fun commands"""

    def __init__(self, bot):
        """constructor for the Fun class

        Args:
            bot (disnake.Bot): The bot instance
        """
        self.bot = bot
        self.logger = bot.logger

    async def autocomp_tags(
        inter: disnake.ApplicationCommandInteraction, user_input: str
    ):
        """autocomplete joke tags

        Args:
            inter (disnake.ApplicationCommandInteraction): the interaction object
            user_input (str): the user's input while they type

        Returns:
            list: list of autocomplete options
        """
        # Check the user input against all joke tags
        return [tag for tag in all_joke_tags if user_input.lower() in tag][:25]

    @commands.slash_command(name="fun", description="The fun command group")
    async def fun(self, ctx):
        """The fun command group

        Args:
            ctx (disnake.ApplicationCommandInteraction): The Interaction object
        """
        # Do nothing with it. This is just a group.
        pass

    @fun.sub_command(name="joke", description="Get a randome joke")
    async def joke(
        self,
        ctx,
        allow_offensive: bool = False,
    ):
        """joke command

        Args:
            ctx (disnake.ApplicationCommandInteraction): The Interaction object
            allow_offensive (bool, optional): Allow NSFW or offensive jokes. Defaults to False.
        """
        # Get a random joke and its tags
        joke, tags = get_random_joke(allow_offensive)
        # Make the embed.
        emb = disnake.Embed(title="Joke", description=joke, color=0x00FF00)
        emb.add_field(name="Tags", value=", ".join(tags))
        emb.set_footer(text="Powered by RandomStuffApi.xyz")
        # Update the database about the usage stats.
        if allow_offensive:
            # If the user allowed offensive jokes, update the offensive joke stats.
            await self.bot.db.commands.update_one(
                {"category": "fun", "command": "joke"}, {"$inc": {"nsfw_uses": 1}}
            )
        await self.bot.db.commands.update_one(
            {"category": "fun", "command": "joke"}, {"$inc": {"uses": 1}}
        )
        await ctx.send(embed=emb)

    @fun.sub_command(
        name="custom_joke", description="Get a joke based on selected tag."
    )
    async def customJoke(
        self, ctx, tag: str = commands.param(autocomplete=autocomp_tags)
    ):
        """joke command using a tag

        Args:
            ctx (disnake.ApplicationCommandInteraction): The Interaction object
            tag (str, optional): The tag.
        """
        # Get a joke based on the tag
        joke, tags = get_tag_joke(tag)
        # Make the embed.
        emb = disnake.Embed(title="Joke", description=joke, color=0x00FF00)
        emb.add_field(name="Tags", value=", ".join(tags))
        emb.set_footer(text="Powered by RandomStuffApi.xyz")
        # Update the database about the usage stats.
        await self.bot.db.commands.update_one(
            {"category": "fun", "command": "custom_joke"}, {"$inc": {"uses": 1}}
        )
        await ctx.send(embed=emb)

    @fun.sub_command(name="meme", description="Get a random meme")
    async def meme(self, ctx, allow_nsfw: bool = False):
        """meme command

        Args:
            ctx (disnake.ApplicationCommandInteraction): The Interaction object
            allow_nsfw (bool, optional): Allow NSFW memes. Defaults to False.
        """
        # Get a random meme
        meme = get_random_meme(allow_nsfw)
        # Make the embed.
        emb = disnake.Embed(title=meme["title"], url=meme["postLink"], color=0x00FF00)
        emb.set_author(name=meme["author"])
        if meme["text"]:
            # If the post has text, add it.
            emb.description = meme["text"]
        emb.set_image(url=meme["image"])
        emb.add_field("Subreddit", meme["subreddit"])
        emb.add_field("Upvotes/Downvotes", f"{meme['upvotes']}/{meme['downvotes']}")
        emb.timestamp = datetime.fromtimestamp(meme["createdUtc"])
        # Update the database about the usage stats.
        if allow_nsfw:
            # If the user allowed NSFW memes, update the NSFW meme stats.
            await self.bot.db.commands.update_one(
                {"category": "fun", "command": "meme"}, {"$inc": {"nsfw_uses": 1}}
            )
        await self.bot.db.commands.update_one(
            {"category": "fun", "command": "meme"}, {"$inc": {"uses": 1}}
        )
        await ctx.send(embed=emb)


def setup(bot):
    """The setup function of the cog.

    Args:
        bot (disnake.ext.commands.Bot): The Bot object

    Returns:
        disnake.ext.commands.Bot: The Bot object
    """
    bot.add_cog(Fun(bot))
    bot.logger.info("Fun cog loaded")
    return bot
