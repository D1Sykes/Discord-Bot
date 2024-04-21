import settings
import discord

from discord.ext import commands

badwords = ['cs', 'cs2']

def run():
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user} er live')

    @bot.event
    async def on_message(message):
        for i in badwords:
            if i in message.content.lower():
                await message.channel.send('Nei.')
            return

    bot.run(settings.token)

if __name__ == "__main__":
    run()