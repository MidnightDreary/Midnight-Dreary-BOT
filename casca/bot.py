# Discord Bot
import logging
import os
import sys

import discord
import logbook
import yaml
from discord.ext.commands import Bot
from logbook import Logger
from logbook import StreamHandler
from logbook.compat import redirect_logging

extensions = ["casca.cogs.mathematics"]

Whitelisted_Servers = ["221708975698083841",  # GERMAN LEARNING AND DISCUSSION
                       "245333247796576257",  # STEAMBOAT
                       "293111771428945920",  # BOT-TESTING
                       "206935992022728704"]  # HYPNOSIS

Whitelisted_Channels = ["221708975698083841",  # GERMAN LEARNING AND DISCUSSION: general
                        "221709483284496394",  # GERMAN LEARNING AND DISCUSSION: learning
                        "222013061886640128",  # GERMAN LEARNING AND DISCUSSION: deutsch-only
                        "259006631185088516",  # GERMAN LEARNING AND DISCUSSION: introductions
                        "251115764680097794",  # GERMAN LEARNING AND DISCUSSION: announcements
                        "252121415912914946",  # GERMAN LEARNING AND DISCUSSION: writing
                        "248530603165614080",  # GERMAN LEARNING AND DISCUSSION: botchannel
                        "260865272292835329",  # GERMAN LEARNING AND DISCUSSION: 0x1-bot

                        "245333247796576257",  # STEAMBOAT: general

                        "293111771428945920",  # BOT-TESTING: general

                        "206935992022728704"]  # HYPNOSIS: main


class Casca(Bot):
    def __init__(self, *args, **kwargs):
        config_file = os.path.join(os.getcwd(), "config.yaml")

        with open(config_file) as f:
            self.config = yaml.load(f)

        super().__init__(*args, **kwargs)

        # Define the logging set up.
        redirect_logging()
        StreamHandler(sys.stderr).push_application()

        self.logger = Logger("Casca_Best_Bot")
        self.logger.level = getattr(logbook, self.config.get("log_level", "INFO"), logbook.INFO)

        # Set the root logger level, too.
        logging.root.setLevel(self.logger.level)

        self._loaded = False

    async def on_ready(self):
        if self._loaded:
            return

        self.logger.info(
            "LOADED Casca | LOGGED IN AS: {0.user.name}#{0.user.discriminator}.\n----------------------------------------------------------------------------------------------------".format(
                self))

        for cog in extensions:
            try:
                self.load_extension(cog)
            except Exception as e:
                self.logger.critical("Could not load extension `{}` -> `{}`".format(cog, e))
                self.logger.exception()
            else:
                self.logger.info("Loaded extension {}.".format(cog))

        self._loaded = True

    async def on_message(self, message):
        if not message.server:
            return

        if message.server.id not in Whitelisted_Servers:
            return

        if message.channel.id not in Whitelisted_Channels:
            return

        self.logger.info(
            "MESSAGE: {message.content}".format(message=message, bot=" [BOT]" if message.author.bot else ""))
        self.logger.info("FROM: {message.author.name}".format(message=message))

        if message.server is not None:
            self.logger.info("CHANNEL: {message.channel.name}".format(message=message))
            self.logger.info(
                "SERVER: {0.server.name}\n----------------------------------------------------------------------------------------------------".format(
                    message))

        await super().on_message(message)

    def run(self):
        try:
            super().run(self.config["bot"]["token"], bot=True)
        except discord.errors.LoginFailure as e:
            self.logger.error("LOGIN FAILURE: {}".format(e.args[0]))
            sys.exit(2)
