import disnake
from disnake.ext import commands
from enum import Enum
from functions import TruthOrDareFunc


class Rating(Enum):
    r = "r"
    pg13 = "pg13"
    pg = "pg"


class TruthOrDare(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="truthordare")
    async def truthordare(self, ctx):
        pass

    @truthordare.sub_command(name="truth", description="Sends a truth question")
    async def truth(self, ctx, rating: Rating):
        """sends a truth question

        Args:
            ctx (disnake.Interaction): interaction object
        """
        question = await TruthOrDareFunc.get_truth(rating)
        emb = disnake.Embed(
            color=disnake.Color.green(),
            title="Truth",
            description=question["question"],
            timestamp=ctx.created_at,
        )
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        emb.set_footer(text=f"Rating: {question['rating']}")
        return await ctx.send(embed=emb)

    @truthordare.sub_command(name="dare", description="Sends a dare")
    async def dare(self, ctx, rating: Rating):
        """sends a dare

        Args:
            ctx (disnake.Interaction): interaction object
        """
        question = await TruthOrDareFunc.get_dare(rating)
        emb = disnake.Embed(
            color=disnake.Color.green(),
            title="Dare",
            description=question["question"],
            timestamp=ctx.created_at,
        )
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        emb.set_footer(text=f"Rating: {question['rating']}")
        return await ctx.send(embed=emb)

    @truthordare.sub_command(
        name="neverhaveiever", description="Sends a Never Have I ever question"
    )
    async def nhie(self, ctx, rating: Rating):
        """sends a Never Have I ever question

        Args:
            ctx (disnake.Interaction): interaction object
        """
        question = await TruthOrDareFunc.get_neverHaveIEver(rating)
        emb = disnake.Embed(
            color=disnake.Color.green(),
            title="Never Have I ever",
            description=question["question"],
            timestamp=ctx.created_at,
        )
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        emb.set_footer(text=f"Rating: {question['rating']}")
        return await ctx.send(embed=emb)

    @truthordare.sub_command(
        name="wouldyourather", description="Sends a Would You Rather question"
    )
    async def wyr(self, ctx, rating: Rating):
        """sends a Would You Rather question

        Args:
            ctx (disnake.Interaction): interaction object
        """
        question = await TruthOrDareFunc.get_wouldYouRather(rating)
        emb = disnake.Embed(
            color=disnake.Color.green(),
            title="Would You Rather",
            description=question["question"],
            timestamp=ctx.created_at,
        )
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        emb.set_footer(text=f"Rating: {question['rating']}")
        return await ctx.send(embed=emb)

    @truthordare.sub_command(name="paranoia", description="Sends a Paranoia question")
    async def paranoia(self, ctx, rating: Rating):
        """sends a Paranoia question

        Args:
            ctx (disnake.Interaction): interaction object
        """
        question = await TruthOrDareFunc.get_neverHaveIEver(rating)
        emb = disnake.Embed(
            color=disnake.Color.green(),
            title="Paranoia",
            description=question["question"],
            timestamp=ctx.created_at,
        )
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        emb.set_footer(text=f"Rating: {question['rating']}")
        return await ctx.send(embed=emb)


def setup(bot):
    """Loads the cog"""
    bot.add_cog(TruthOrDare(bot))
    bot.logger.info("TruthOrDare cog loaded")
    return bot
