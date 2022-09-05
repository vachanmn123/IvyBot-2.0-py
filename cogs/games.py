import disnake
from disnake.ext import commands
import disnake_together
import enum


class Together_Options(enum.Enum):
    """enum for the together options"""

    youtube = "youtube"
    poker = "poker"
    betrayal = "betrayal"
    fishing = "fishing"
    chess = "chess"
    letter_tile = "letter-tile"
    word_snack = "word-snack"
    doodle_crew = "doodle-crew"


class Games(commands.Cog):
    """The games command group"""

    def __init__(self, bot):
        """constructor for the Games class

        Args:
            bot (disnake.ext.commands.Bot): The bot instance
        """
        self.bot = bot
        self.logger = bot.logger
        self.together_control = disnake_together.DisnakeTogether(bot)

    @commands.slash_command(name="games")
    async def games(self, ctx):
        """The games command group

        Args:
            ctx (disnake.ApplicationCommandInteraction): The Interaction object
        """
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
            # Check if the user is in a voice channel, if they are, use it. If they aren't it will raise an exception.
            vc = ctx.author.voice.channel.id
            if not vc:
                return await ctx.send("You are not in a voice channel")
        except:
            # If the user isn't in a voice channel, reply with this message.
            return await ctx.send("You are not in a voice channel")
        self.logger.debug(f"Starting {game} game")
        # Get a link to start the game.
        link = await self.together_control.create_link(vc, game)
        db_obj = await self.bot.db.commands.find_one(
            {"category": "games", "command": "together"}
        )
        try:
            # increment the uses counter. But if it doesn't exist, set it to 1.
            db_obj["uses"][game] += 1
        except KeyError:
            db_obj["uses"][game] = 1
        # Update the database.
        await self.bot.db.commands.update_one(
            {"category": "games", "command": "together"},
            {"$set": {"uses": db_obj["uses"]}},
        )
        return await ctx.send(f"{link}")


def setup(bot):
    """The setup function for the cog

    Args:
        bot (disnake.ext.commands.Bot): The bot instance

    Returns:
        disnake.ext.commands.Bot: The bot instance
    """
    bot.add_cog(Games(bot))
    bot.logger.info("Games cog loaded")
    return bot
