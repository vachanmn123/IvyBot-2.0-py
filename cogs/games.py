import disnake
from disnake.ext import commands
import disnake_together
import enum


class Together_Options(enum.Enum):
    youtube = "youtube"
    poker = "poker"
    betrayal = "betrayal"
    fishing = "fishing"
    chess = "chess"
    letter_tile = "letter-tile"
    word_snack = "word-snack"
    doodle_crew = "doodle-crew"


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = bot.logger
        self.together_control = disnake_together.DisnakeTogether(bot)

    @commands.slash_command(name="games")
    async def games(self, ctx):
        pass

    @games.sub_command(name="together", description="Starts a game together")
    async def together(self, ctx, game: Together_Options):
        """Starts a game together

        Args:
            ctx (disnake.Interaction): interaction object
            game (Together_Options): game to play
        """
        vc = None
        try:
            vc = ctx.author.voice.channel.id
            if not vc:
                return await ctx.send("You are not in a voice channel")
        except:
            return await ctx.send("You are not in a voice channel")
        self.logger.debug(f"Starting {game} game")
        link = await self.together_control.create_link(vc, game)
        return await ctx.send(f"{link}")


def setup(bot):
    bot.add_cog(Games(bot))
