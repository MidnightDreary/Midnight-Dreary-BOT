from discord.ext.commands import when_mentioned_or

from casca.bot import Casca

if __name__ == "__main__":
    bot = Casca(command_prefix=when_mentioned_or("!"))
    bot.run()
