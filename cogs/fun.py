from webbrowser import get
from disnake.ext import commands
import disnake
from functions.RandomStuffApiFunc import (
    get_random_joke,
    get_all_joke_tags,
    get_tag_joke,
    get_random_meme,
)
from datetime import datetime

all_joke_tags = get_all_joke_tags()


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = bot.logger

    async def autocomp_tags(
        inter: disnake.ApplicationCommandInteraction, user_input: str
    ):
        return [tag for tag in all_joke_tags if user_input.lower() in tag]

    @commands.slash_command(name="fun")
    async def fun(self, ctx):
        pass

    @fun.sub_command(name="joke", description="Get a randome joke")
    async def joke(
        self,
        ctx,
        allow_offensive: bool = False,
    ):
        joke, tags = get_random_joke(allow_offensive)
        emb = disnake.Embed(title="Joke", description=joke, color=0x00FF00)
        emb.add_field(name="Tags", value=", ".join(tags))
        emb.set_footer(text="Powered by RandomStuffApi.xyz")
        await ctx.send(embed=emb)

    @fun.sub_command(
        name="custom_joke", description="Get a joke based on selected tag."
    )
    async def customJoke(
        self, ctx, tag: str = commands.param(autocomplete=autocomp_tags)
    ):
        joke, tags = get_tag_joke(tag)
        emb = disnake.Embed(title="Joke", description=joke, color=0x00FF00)
        emb.add_field(name="Tags", value=", ".join(tags))
        emb.set_footer(text="Powered by RandomStuffApi.xyz")
        await ctx.send(embed=emb)

    @fun.sub_command(name="meme", description="Get a random meme")
    async def meme(self, ctx, allow_nsfw: bool = False):
        meme = get_random_meme(allow_nsfw)
        emb = disnake.Embed(title=meme["title"], url=meme["postLink"], color=0x00FF00)
        emb.set_author(name=meme["author"])
        if meme["text"]:
            emb.description = meme["text"]
        emb.set_image(url=meme["image"])
        emb.add_field("Subreddit", meme["subreddit"])
        emb.add_field("Upvotes/Downvotes", f"{meme['upvotes']}/{meme['downvotes']}")
        emb.timestamp = datetime.fromtimestamp(meme["createdUtc"])
        await ctx.send(embed=emb)


def setup(bot):
    bot.add_cog(Fun(bot))
