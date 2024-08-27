import settings
import discord
from discord.ext import commands
from botcommands import botSetup  # Importing the bot functions

def run(): # Main program

    # Bot settings and intents
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='!', intents=intents)

    # Set up the bot with the commands and events from bot_commands.py
    botSetup(bot)

    bot.run(settings.token)

if __name__ == "__main__":
    run()