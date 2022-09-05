import disnake
from disnake.ext import commands
from enum import Enum
from functions import TruthOrDareFunc


class Rating(Enum):
    r = "r"
    pg13 = "pg13"
    pg = "pg"


class TruthOrDare(commands.Cog):
    """Truth or Dare commands"""

    def __init__(self, bot):
        """constructor for the TruthOrDare class

        Args:
            bot (disnake.ext.commands.Bot): The bot instance
        """
        self.bot = bot

    @commands.slash_command(name="truthordare")
    async def truthordare(self, ctx):
        """The truthordare command group

        Args:
            ctx (disnake.ApplicationCommandInteraction): The Interaction object
        """
        pass

    @truthordare.sub_command(name="truth", description="Sends a truth question")
    async def truth(self, ctx, rating: Rating):
        """sends a truth question

        Args:
            ctx (disnake.Interaction): interaction object
        """
        # Get a random truth question
        question = await TruthOrDareFunc.get_truth(rating)
        # Make the embed
        emb = disnake.Embed(
            color=disnake.Color.green(),
            title="Truth",
            description=question["question"],
            timestamp=ctx.created_at,
        )
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        emb.set_footer(text=f"Rating: {question['rating']}")
        # Update the database about the usage stats.
        await self.bot.db.commands.update_one(
            {"category": "truthordare", "command": "truth"}, {"$inc": {"uses": 1}}
        )
        return await ctx.send(embed=emb)

    @truthordare.sub_command(name="dare", description="Sends a dare")
    async def dare(self, ctx, rating: Rating):
        """sends a dare

        Args:
            ctx (disnake.Interaction): interaction object
        """
        # Get a random dare
        question = await TruthOrDareFunc.get_dare(rating)
        # Make the embed
        emb = disnake.Embed(
            color=disnake.Color.green(),
            title="Dare",
            description=question["question"],
            timestamp=ctx.created_at,
        )
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        emb.set_footer(text=f"Rating: {question['rating']}")
        # Update the database about the usage stats.
        await self.bot.db.commands.update_one(
            {"category": "truthordare", "command": "dare"}, {"$inc": {"uses": 1}}
        )
        return await ctx.send(embed=emb)

    @truthordare.sub_command(
        name="neverhaveiever", description="Sends a Never Have I ever question"
    )
    async def nhie(self, ctx, rating: Rating):
        """sends a Never Have I ever question

        Args:
            ctx (disnake.Interaction): interaction object
        """
        # Get a random Never Have I ever question
        question = await TruthOrDareFunc.get_neverHaveIEver(rating)
        # Make the embed
        emb = disnake.Embed(
            color=disnake.Color.green(),
            title="Never Have I ever",
            description=question["question"],
            timestamp=ctx.created_at,
        )
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        emb.set_footer(text=f"Rating: {question['rating']}")
        # Update the database about the usage stats.
        await self.bot.db.commands.update_one(
            {"category": "truthordare", "command": "nhie"}, {"$inc": {"uses": 1}}
        )
        return await ctx.send(embed=emb)

    @truthordare.sub_command(
        name="wouldyourather", description="Sends a Would You Rather question"
    )
    async def wyr(self, ctx, rating: Rating):
        """sends a Would You Rather question

        Args:
            ctx (disnake.Interaction): interaction object
        """
        # Get a random Would You Rather question
        question = await TruthOrDareFunc.get_wouldYouRather(rating)
        # Make the embed
        emb = disnake.Embed(
            color=disnake.Color.green(),
            title="Would You Rather",
            description=question["question"],
            timestamp=ctx.created_at,
        )
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        emb.set_footer(text=f"Rating: {question['rating']}")
        # Update the database about the usage stats.
        await self.bot.db.commands.update_one(
            {"category": "truthordare", "command": "wyr"}, {"$inc": {"uses": 1}}
        )
        return await ctx.send(embed=emb)

    @truthordare.sub_command(name="paranoia", description="Sends a Paranoia question")
    async def paranoia(self, ctx, rating: Rating):
        """sends a Paranoia question

        Args:
            ctx (disnake.Interaction): interaction object
        """
        # Get a random Paranoia question
        question = await TruthOrDareFunc.get_neverHaveIEver(rating)
        # Make the embed
        emb = disnake.Embed(
            color=disnake.Color.green(),
            title="Paranoia",
            description=question["question"],
            timestamp=ctx.created_at,
        )
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        emb.set_footer(text=f"Rating: {question['rating']}")
        # Update the database about the usage stats.
        await self.bot.db.commands.update_one(
            {"category": "truthordare", "command": "paranoia"}, {"$inc": {"uses": 1}}
        )
        return await ctx.send(embed=emb)


def setup(bot):
    """The setup function for the cog

    Args:
        bot (disnake.ext.commands.Bot): The bot instance

    Returns:
        disnake.ext.commands.Bot: The bot instance
    """
    bot.add_cog(TruthOrDare(bot))
    bot.logger.info("TruthOrDare cog loaded")
    return bot
