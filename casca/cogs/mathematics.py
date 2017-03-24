import random
import time

import discord
from discord.ext import commands

from casca.constants import faces, compliments, brawl, victor_message, facts
from casca.poetry import poems, poetry_index


class FunctionMathematics:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["pong", "test"], pass_context=True)
    async def ping(self, ctx):
        """Checks for a connection. Returns \"Pong\" if one is found."""
        await self.bot.delete_message(ctx.message)
        await self.bot.say("Pong!")

    @commands.command(aliases=["poem"], pass_context=True)
    async def poetry(self, ctx, poem: str, stanza: int = 1):
        """
        Displays the stanza of the chosen poem
        """
        for entry in poems:
            if poem.lower() == entry.syntax:
                receive = entry.retrieve(stanza)
                await self.bot.delete_message(ctx.message)
                await self.bot.say(receive["header"])
                await self.bot.say(receive["text"])

    @commands.command(aliases=["emoji", "face", "ascii"], pass_context=True)
    async def draw(self, ctx, choice: str):
        """Allows for the sending of ASCII emoji"""
        await self.bot.delete_message(ctx.message)
        try:
            await self.bot.say(faces[choice])
        except:
            await self.bot.say("ERROR OCCURRED")

    @commands.command(name="p_index", pass_context=True)
    async def p_index(self, ctx):
        """
        Displays information on available poems.
        """
        await self.bot.delete_message(ctx.message)
        await self.bot.say(poetry_index)

    @commands.command(aliases=["praise"], pass_context=True)
    async def compliment(self, ctx, target: discord.Member):
        """
        Share some love.
        """
        smile = str(compliments[random.randint(0, len(compliments) - 1)])
        await self.bot.delete_message(ctx.message)
        await self.bot.say(target.mention + " " + smile)

    @commands.command(aliases=["fight"], pass_context=True)
    async def gladiator(self, ctx, brawler: discord.Member, challenger: discord.Member):
        """
        A fight to the death.
        """
        await self.bot.delete_message(ctx.message)
        await self.bot.say(brawl % (str(brawler.display_name), str(challenger.display_name)))
        time.sleep(3)
        await self.bot.say("```The first few blows are falling!```")
        time.sleep(3)
        await self.bot.say("```The sand is turning pink as the fight wages on...```")
        time.sleep(5)
        winner = random.choice([brawler, challenger])
        await self.bot.say(victor_message + winner.mention)

    @commands.command(aliases=["cointoss", "headsortails", "coin"], pass_context=True)
    async def coinflip(self, ctx):
        "Flips a coin"
        await self.bot.delete_message(ctx.message)
        await self.bot.say(random.choice(["```Heads```", "```Tails```"]))

    @commands.command(aliases=["request"], pass_context=True)
    async def suggest(self, ctx, suggestion: str):
        "Permits for the suggestion of new features / changes"
        await self.bot.delete_message(ctx.message)
        suggestion_file = open("suggestion.txt", "a+")
        if "\n" not in suggestion:
            suggestion_file.write("[{}] {} \n".format(time.strftime("%d.%m.%y %H:%M:%S"), suggestion))
        else:
            suggestion_file.write("[{}] {}".format(time.strftime("%d.%m.%y %H:%M:%S"), suggestion))
        suggestion_file.close()

    @commands.command(aliases=["learn"], pass_context=True)
    async def fact(self, ctx, number: int = 0):
        "Displays a random fact"
        if number == 0:
            await self.bot.delete_message(ctx.message)
            await self.bot.say("```{}```".format(random.choice(facts)))
        else:
            if number in range(1, len(facts) + 1):
                await self.bot.delete_message(ctx.message)
                await self.bot.say("```{}```".format(facts[number - 1]))

    @commands.command(name="rich", pass_context=True)
    async def special(self, ctx, title: str, name: str, *, value: str):
        """
        Embeds text.
        """
        embed = discord.Embed()
        embed.colour = 0x738bd7

        await self.bot.delete_message(ctx.message)
        embed.title = title
        embed.add_field(name=name, value=value)

        await self.bot.say(embed=embed)

    @commands.command(name="info", pass_context=True)
    async def special(self, ctx):
        """
        Displays information on MidnightDreary.
        """
        embed = discord.Embed()
        embed.colour = 0x738bd7

        await self.bot.delete_message(ctx.message)

        embed.title = "INFORMATION PERTAINING TO THIS BOT"
        embed.add_field(name="NAME", value="MidnightDreary")
        embed.add_field(name="OWNER", value="Casca")
        embed.add_field(name="LOCATION", value=":flag_de:")
        embed.set_thumbnail(url=ctx.message.server.me.avatar_url)

        await self.bot.say(embed=embed)

    @commands.command(alises=["upcoming"], pass_context=True)
    async def pending(self, ctx):
        """
         Shows current suggestions
        """
        await self.bot.delete_message(ctx.message)
        suggestion_file = open("suggestion.txt", "r")
        suggestion_text = suggestion_file.read()
        await self.bot.say("```{}```".format(suggestion_text ))
        suggestion_file.close()


def setup(bot):
    bot.add_cog(FunctionMathematics(bot))